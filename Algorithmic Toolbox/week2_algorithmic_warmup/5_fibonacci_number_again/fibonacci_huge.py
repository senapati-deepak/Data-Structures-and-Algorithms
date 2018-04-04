# Uses python3
def pisano(m):
    a=0
    b=1
    for i in range(1, (m*m)+1):
        c = (a+b) % m
        a = b
        b = c
        if a == 0 and b==1:
            return i


a, b = map(int, input().split())
l = pisano(b)
n = a%l
x = 0
y = 1
if n <= 1 :
    print(n)
else :
    for i in range(2,n+1):
        z = x+y
        x = y
        y = z
    print(z%b)

