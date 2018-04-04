# Uses python3
n = int(input())
a = 0
b = 1
z = 1
if n <= 1:
    print(n)
else :
    for i in range(2, n+1):
        c = (a + b) % 10
        a = b
        b = c
        z = (z + c) % 10
    print(z)
