#!/usr/bin/env python3

s, t, x = [int(i) for i in input().split()]

if s == t:
  print("No")
  exit()

A = [s]
while True:
  s += 1
  if s > 23:
    s = 0
  if s == t:
    break
  A.append(s)

ans = "Yes" if x in A else "No"
print(ans)