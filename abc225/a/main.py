#!/usr/bin/env python3

S = set(input())
l = len(S)
ans = 1
if l == 3:
  ans = 6
elif l == 2:
  ans = 3

print(ans)
