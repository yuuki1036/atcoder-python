#!/usr/bin/env python3

s = input()
l = len(s)

if l == 1:
  print(s)
  print(s)
  exit()

S = [s]
for _ in range(l-1):
  s = s[1:] + s[0]
  S.append(s)

S.sort()
print(S[0])
print(S[-1])
