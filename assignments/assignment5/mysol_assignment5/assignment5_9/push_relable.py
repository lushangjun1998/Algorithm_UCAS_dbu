#!/usr/bin/env python3
#-*- coding: utf-8 -*-

"""
@author: Eadren
@date: 08/01/2018

The solution for algorithm assignment5_9.
"""

_PROMPT = """
For a matrix filled with 0 and 1, you know the
sum of every row and column. You are asked to
give such a matrix which satisfys the conditions.

INPUT:  There rows.
        The first row is M, N which are matrix size
        The second row is each sum of each row of matrix
        The third row is each sum of each column of matrix


OUTPUT: The matrix which satisfys the conditions


e.g.

INPUT:
3 3
1 2 2
1 1 3

OUTPUT:
[0 0 1]
[0 1 1]
[1 1 1]

Now Input:
"""


def print_G(G):
    for row in G:
        print(row)

def read_matrix():
    """
    the first row contain two numbers, M, N

    M: the rows of matrix
    N: the column of matrix
    return G: the network graphy
    """

    M, N = list(map(int, input().split()))

    s = 0
    t = M + N + 1
    G = [ [0] * (M+N+2) for _ in range(M+N+2) ] # add s, t node to graph G

    for i, row_sum in enumerate(map(int, input().split())):
        G[s][1+i] = row_sum
    for j, col_sum in enumerate(map(int, input().split())):
        G[1+M+j][t] = col_sum
    for i in range(1, 1+M):
        for j in range(1+M, 1+M+N):
           G[i][j] = 1
    return G, M, N


def push_relabel(G, M, N):
    s = 0
    t = M + N + 1
    height = [0] * (M + N + 2)
    height[s] = M + N + 2
    Ef = {} # using dict to maintain the all node v for Ef(v) > 0

    # f(e) = C(e) for all e = (s, u) f(e) = 0 for other edges
    # Ef(u) = C(e)
    for u in range(1, 1+M):
        G[u][s] = G[s][u]
        Ef[u] = G[s][u]
        G[s][u] = 0
    while Ef:
        print('The G now is')
        print_G(G)
        print('Ef(v): ', Ef)
        print('height(v): ', height)
        v, Ef_v = Ef.popitem()
        exists = False
        for u in range(M + N + 2):
            if Ef_v and G[v][u] and height[v] > height[u]:
                # push excess from v to u
                bottleneck = min(G[v][u], Ef_v)
                G[v][u] -= bottleneck
                G[u][v] += bottleneck
                Ef_v -= bottleneck
                print('Push: from %d with bottleneck %d to %d' % (v, bottleneck, u))
                if u != s and u != t:
                    Ef_u = Ef.get(u, 0)
                    Ef_u += bottleneck
                    Ef[u] = Ef_u
                exists = True
        if Ef_v:
            Ef[v] = Ef_v
        if not exists:
            print('Relabel: %d' % v)
            Ef[v] = Ef_v
            height[v] += 1

        print('=' * 20, end='\n\n\n')

def _main():
    print(_PROMPT)
    G, M, N = read_matrix()
    push_relabel(G, M, N)
    transposed_matrix = []
    for i in range(1+M, 1+M+N):
        transposed_matrix.append(G[i][1: 1+M])
    # transponse
    orignal_matrix = list(map(list, zip(*transposed_matrix)))
    print('The matrix which satisfys the conditions:')
    for row in orignal_matrix:
        print(row)


if __name__ == '__main__':
    _main()
