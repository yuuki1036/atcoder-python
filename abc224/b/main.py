#!/usr/bin/env python3

H, W = [int(i) for i in input().split()]
M = [[int(i) for i in input().split()] for j in range(H)]
idxs = []

for i1 in range(H):
  for i2 in range(H):
    if i1 >= i2:
      continue
    for j1 in range(W):
      for j2 in range(W):
        if j1 < j2:
          idxs.append((i1, i2, j1, j2))

ans = "Yes" if idxs else "No"

for idx in idxs:
  i1, i2, j1, j2 = idx
  if M[i1][j1] + M[i2][j2] > M[i2][j1] + M[i1][j2]:
    ans = "No"
    break

print(ans)