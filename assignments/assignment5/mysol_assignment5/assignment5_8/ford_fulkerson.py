#!/usr/bin/env python3
#-*- coding: utf8 -*-

"""
@author: Eadren
@date: 07/01/2018

The solution for algorithm assignment5_8
"""

_PROMT = """
You have some different computers and jobs. For each job,
it can only be done on one of two specified computers.
The load of a computer is the number of jobs which have
been done on the computer. Give the number of jobs and
two computer ID for each job. You task is to minimize the max load.
(hint: binary search)


INPUT:  The first row has two number, M, N  which are the number
        of jobs and the number of computers.
        The following M rows contains two number C1, C2 which means
        The jobi can be done in computer C1 and C2.

OUTPUT: The minimum cost of the max load

e.g.

INPUT
4 2
1 2
1 2
1 2
1 2

OUTPUT:
2

Now Input:
"""
from queue import Queue
from copy import deepcopy


def print_G(G):
    for row in G:
        print(row)


def BFS(Gf):
    """
    Gf is the redisual Gfrpah for flow f
    """

    s = 0
    t = len(Gf) - 1
    q = Queue()
    visited = [False] * (t+1)
    reverse_path = [ i for i in range(t+1) ]


    # put the node s(here means 0) into the queue
    q.put(0)
    visited[0] = True

    while not q.empty():
        node = q.get()
        for neighbor, edge in enumerate(Gf[node]):
            if edge and not visited[neighbor]:
                reverse_path[neighbor] = node
                visited[neighbor] = True
                q.put(neighbor)
                if neighbor == t:
                    break

    if not visited[t]:
        return None
    return reverse_path


def augment(Gf, reverse_path, current_flow):
    # find the bottleneck in the reverse_path
    t = len(Gf) - 1
    bottleneck = Gf[ reverse_path[t] ][t] # flow(v -> t)
    v = reverse_path[t]
    while reverse_path[v] != v:
        bottleneck = min( bottleneck, Gf[ reverse_path[v] ][v])
        v = reverse_path[v]

    # udpate the redisual graphy
    v = t
    while reverse_path[v] != v:
        if Gf[ reverse_path[v] ][v] == bottleneck:
            Gf[v][ reverse_path[v] ] = bottleneck # backward edge
        Gf[ reverse_path[v] ][v] -= bottleneck
        v = reverse_path[v]

    # increase flow
    return current_flow + bottleneck


def ford_fulkerson(Gf):
    """
    Gf: the original network grahy
    """
    current_flow = 0

    # get the max flow
    while True:
        print('before BFS Gf: ')
        print_G(Gf)
        print('-' * 10)
        reverse_path = BFS(Gf)
        if not reverse_path:
            print('No s-t path founded, the current_flow is max_flow')
            print('*' * 30, end='\n\n\n\n')
            break
        current_flow = augment(Gf, reverse_path, current_flow)
        print('find reverse_path =', reverse_path)
        print('current_flow =', current_flow)
        print('=' * 20, end='\n\n')
    return current_flow


def binary_search(G, n, m):
    """
    G: the orignal graphy
    n: the number of jobs
    m: the number of computers
    """
    t = len(G) - 1
    begin = 1
    end = n

    while begin < end:
        C = (begin + end) // 2
        Gf = deepcopy(G)
        for i in range(1+n, t):
            Gf[i][t] = C

        # V(f) != n
        if ford_fulkerson(Gf) != n:
            begin = C + 1
        else:
            end = C

    return begin


def read_graph():
    N, M = list(map(int, input().split()))
    G = [[0] * (N + M + 2) for i in range(N + M +2)]
    for i in range(1, N+1):
        u, v = list(map(int, input().split()))
        G[0][i] = G[i][u + N] = G[i][v + N] = 1
    return G, N, M

def _main():
    print(_PROMT)
    G, N, M = read_graph()
    print('inital G:', G)
    C = binary_search(G, N, M)
    print("The minimum cost of max load is %d" % C)


if __name__ == '__main__':
    _main()
