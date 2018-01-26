#!/usr/bin/env python3
#-*- coding: utf-8 -*-


from functools import cmp_to_key
import sys
from math import sqrt


dist = lambda x1, x2: (x1[0] - x2[0]) ** 2 + (x1[1] - x2[1]) ** 2

def closest_pair(p, left, right):
    if right - left  == 0:
        return sys.maxsize
    if right - left == 1:
        return dist(p[left], p[right])
    mid = (left + right) >> 1
    l_closest = closest_pair(p, left, mid-1)
    r_closest = closest_pair(p, mid , right)

    d = min(l_closest, r_closest)

    for i in range(mid-1, left-1, -1):
        if (p[mid][0] - p[i][0]) ** 2 >= d:
            break
        for j in range(mid, right+1, 1):
            if (p[j][0] - p[mid][0]) ** 2 >= d:
                break
            if (p[j][1] - p[i][1]) ** 2 >= d:
                continue
            n_dist  = dist(p[i], p[j])
            if n_dist < d:
                d = n_dist
    return d


def points_cmp(p1, p2):
    if p1[0] == p2[0]:
        return p1[1] - p2[1]
    return p1[0] - p2[0]

fin = open('assignment1_9.in')
fout = open('assignment1_9.out', 'w')
while True:
    n = int(fin.readline())
    if n == 0:
        break
    p = []
    for i in range(n):
        x, y = map(float, fin.readline().split())
        p.append([x, y])
    p.sort(key=cmp_to_key(points_cmp))
    ans = sqrt(closest_pair(p, 0, len(p)-1))
    print('%.4f' % ans, file=fout)

fin.close()
fout.close()
