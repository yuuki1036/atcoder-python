#!/usr/bin/env python3

N = int(input())
S = set()

for _ in range(N):
  s = tuple(input().split())
  S.add(s)

print(len(S))