# Uses python3
n = int(input())
a = [int(x) for x in input().split()]
f=0
s=0

f = max(a)
a.remove(f)
s = max(a) 

print(f*s)


