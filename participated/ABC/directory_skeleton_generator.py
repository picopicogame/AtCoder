#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
標準出力から解く予定の問題とフォルダ名を受け取る。
AtCoderコンテスト用のフォルダとpythonファイルを出力する。
フォルダが既にある場合、プログラムを終了する。上書きはしない。
指定された問題までのpythonファイルとテストファイルを生成する
ファイル名の例：
A.py test_A.py

各pythonファイルにも必要なコードを書いておく。
プロダクションコード側
if __name__ == "__main__":などのお決まりの文
テストコード側
プロダクションコードのimport文まで
"""

import os
import re

# ソースコードの内容の文字列
source_code_string = """\
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

# 再帰のリミットをあげる
sys.setrecursionlimit(10**6)

def input():
    return sys.stdin.readline()


def resolve():
    pass


if __name__ == "__main__":
    resolve()

"""

# テストコードの内容
test_code_string = """\
#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

def write_python_file(problem, folder_path):
    """pythonファイル作成関数"""

    # アルファベットでイテレーションする
    for char_code in range(ord('A'), ord(problem)+1):
        # pythonファイル名
        python_file_name = folder_path + chr(char_code) + ".py"
        # ファイル作成と内容書き込み
        f = open(python_file_name, "w", encoding="UTF-8")
        f.write(source_code_string)
        f.close()
        # テストコードファイル名
        testcode_file_name = folder_path + "test_" + chr(char_code) + ".py"

        # テストコードもファイル作成と書き込み
        f = open(testcode_file_name, "w", encoding="UTF-8")
        content = test_code_string + "\nfrom " + chr(char_code) + " import resolve\n\n\n"
        f.write(content)
        f.close

# カレントフォルダのパス
current_folder_path = r"C:\Pico_Programming_Project\002AtCoder\participated\ABC"


# 入力部
print("どの問題まで解きますか？:A～F")
while True:
    problem_difficulty = input()
    # A~F一文字のみ　一文字と指定したい場合は末尾に$
    pattern = re.compile('[A-F]$')
    if pattern.match(problem_difficulty):
        break
    else:
        print("A~Fのアルファベット一文字で入力してください\n 終了はctrl+c")

print("フォルダ名入力してください:")
folder_name = input()

# 新たに作成したフォルダのパス
new_folder_path = current_folder_path + "\\" + folder_name + "\\"

# フォルダとファイル生成
for dirpath, dirnames, filenames in os.walk(current_folder_path):

    if current_folder_path == dirpath:
        # 新たにフォルダを作る
        try:
            os.mkdir(folder_name)
        except FileExistsError:
            print("すでに同じフォルダが存在します。\n終了します。")
            exit()

# ファイルの作成、書き込み
write_python_file(problem_difficulty, new_folder_path)
