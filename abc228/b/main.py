#!/usr/bin/env python3

n, x = [int(i) for i in input().split()]
T = [int(i) - 1 for i in input().split()]
F = [0] * n
x -= 1
F[x] = 1

while True:
  x = T[x]
  if F[x] == 0:
    F[x] = 1
  else:
    break

print(F.count(1))