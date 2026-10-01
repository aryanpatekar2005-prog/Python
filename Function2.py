#Addition with function
def num(a,b):
    print(a+b)
num(12,12)
num(2,3)
#Experimentation
def pi():
    return 3.14
print(pi())
pi=pi()
print(pi)

def add(a,b):
    return a+b
print(add(12,13))

def name(name):
    print("Hello",name)
name()
#Calculator in function
print("1.Addition")
print("2.Substraction")
print("3.Multiplication")
print("4.Division")
ch=int(input("Enter your choice:"))
match ch:
    case 1:
        def add(a,b):
            a=input("Enter 1st number:")
            b=input("Enter 2nd number:")
            return(a+b)
    case 2:
          def sub(a,b):
            a=input("Enter 1st number:")
            b=input("Enter 2nd number:")
            return(a-b)
    case 3:
          def Mul(a,b):
            a=input("Enter 1st number:")
            b=input("Enter 2nd number:")
            return(a*b)
    case 4:
          def div(a,b):
            a=input("Enter 1st number:")
            b=input("Enter 2nd number:")
            return(a/b)
    case _:
          print("Invalid Choice")

def num(n):
    print(n)
    num(n-1)
#Factorial in function
def fact(a):
    if a==0 or a==1:
        return 1
    else:
        return a*fact(a-1)
a=int(input("Enter a number:"))
fc=fact(a)
print(fc)

square=lambda n:n*n
print(square(2))
