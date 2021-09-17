#!/usr/bin/env python3

L = [int(i) for i in input().split()]
ans = ""
for l in L:
  ans += chr(l+96)
print(ans)