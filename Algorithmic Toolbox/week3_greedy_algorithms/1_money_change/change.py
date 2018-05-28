# Uses python3

n = int(input())
c = 0
c = c + n//10
n = n%10
c = c + n//5
n = n%5
print(c + n//1)
