#!/usr/bin/env python3

n = int(input())
a1, b1 = input().split()
arr2 = input().split()
t = 0
if a1 in arr2:
  t = a1
elif b1 in arr2:
  t = b1

ans = "Yes"

for i in range(n-3):
  narr = input().split()
  if not t in narr:
    ans = "No"
    break

print(ans)
