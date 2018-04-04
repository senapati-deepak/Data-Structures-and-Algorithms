# Uses python3
import sys
def gcd_fast(a, b):
    if b == 0:
        return a
    aa = a%b
    return gcd_fast(b, aa)

b, a = map(int, input().split())
l = int((a*b)//gcd_fast(a,b))

print(l)

