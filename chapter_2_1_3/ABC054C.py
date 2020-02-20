# %%
# VScodeで入力をテキストから読み込んで標準入力に渡す
import sys
import os
f=open(r'.\chapter_2_1_3\ABC054C_input.txt', 'r', encoding="utf-8")
# inputをフルパスで指定
# win10でファイルを作るとs-jisで保存されるため、読み込みをutf-8へエンコードする必要あり
# VScodeでinput file開くとutf8になってるんだけど中身は結局s-jisになっているらしい
sys.stdin=f

#
# 入力スニペット
# num = int(input())
# num_list = [int(item) for item in input().split()]
# num_list = [input() for _ in range(3)]
##################################
# %%
# 以下ペースト可
import collections
import numpy as np

N, M = [int(item) for item in input().split()]
edge_list = np.array([[int(item) for item in input().split()] for _ in range(M)])

node_cnt = 0
res_cnt = 0


def rec(start_node):
    if start_node in edge_list[:, 0]:
        node_cnt += 1
        for to_node in edge_list[:, 1]:
            rec(to_node)

    else:
        if node_cnt == N:
            res_cnt += 1
            return

    return res_cnt

print(rec(1))