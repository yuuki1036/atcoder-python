#!/usr/bin/env python3

N = int(input())
S = [int(i) for i in input().split()]

ans = 0
for s in S:
  ok = False
  for i in range(1, 201):
    for j in range(1, 201):
      if s == (4*i*j) + (3*i) + (3*j):
        ok = True
        break
    if ok:
      break
  else:
    ans += 1

print(ans)
