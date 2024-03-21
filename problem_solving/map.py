import sys
sys.stdout = open('output.txt', 'w')

sys.stdin = open('input.txt', 'r')

def myfunc(a,b):
    return a+b

def addition(n):
    return n*n




x=map(myfunc,("apple","komola","malta"),("orange","lemon"))

print(x)

print(list(x))

#addition

numbers=(1,2,3,4)
print(type(numbers))

y=map(addition,numbers)
print(list(y))