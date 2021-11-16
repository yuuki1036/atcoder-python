#!/usr/bin/env python3

n = int(input())
ans = "No"
if n > 0 and n % 100 == 0:
  ans = "Yes"
print(ans)