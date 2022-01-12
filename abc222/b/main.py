#!/usr/bin/env python3

N, P = [int(i) for i in input().split()]
A = [int(i) for i in input().split()]
ans = 0

for a in A:
  if a < P:
    ans += 1

print(ans)