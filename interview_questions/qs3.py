"""
fibonnaci series (recursion)
"""

def fibonacci(n):
    if n<=1:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)
n=10
if n<=0:
    print('invalid')
else:
    for i in range(n):
        print(fibonacci(i))