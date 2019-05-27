import sys

num1 = int(sys.argv[1])
num2 = int(sys.argv[2])

def add(a, b):
    out = a+b
    return out

print(add(num1, num2))