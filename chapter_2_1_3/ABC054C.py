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
r_edge_list = edge_list[:, ::-1]

edge_list = np.concatenate([edge_list, r_edge_list])

# print(edge_list)

footprint = collections.deque()
res = 0

def rec(node, res):
    if len(footprint) == N:
        res += 1
        return
    else:
        for edge in edge_list:
            if edge[0] == node and edge[1] not in footprint:
                print(edge)
                footprint.append(edge[1])
                rec(edge[1], res)
                footprint.pop()

    return res

print(rec(1, 0))




