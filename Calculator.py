print("1.Addition")
print("2.Substraction")
print("3.Multiplication")
print("4.Division")
print("5.Factorial")
ch=int(input("Enter what operation:"))
match ch:
    case 1:
        a=int(input("Enter first num:")) 
        b=int(input("Enter second num:"))  
        print(a+b)

    case 2:
        a=int(input("Enter first num:"))
        b=int(input("Enter second num:"))
        print(a-b)

    case 3:
        a=int(input("Enter first num:")) 
        b=int(input("Enter second num:")) 
        print(a*b)

    case 4:
        a=int(input("Enter first num:")) 
        b=int(input("Enter second num:"))
        if b==0:
            print("denominator can't be 0")
        else:
            print(a/b)
    case 5:
        a=int(input("Enter a number:"))
        fact=1
        i=1
        while i<=a:
            fact=fact*i
            i+=1
        print("Factorial",fact)
    case _:
        print("Invalid case!")