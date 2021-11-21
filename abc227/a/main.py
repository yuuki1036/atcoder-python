#!/usr/bin/env python3

N, K, A = [int(i) for i in input().split()]
ans = A

for _ in range(K-1):
  if ans >= N:
    ans = 1
  else:
    ans += 1

print(ans)