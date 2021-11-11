#!/usr/bin/env python3

from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN

N = Decimal(input())
print(N.quantize(Decimal("0"), rounding=ROUND_HALF_UP))