marks=int(input("Enter marks:"))
if marks>=90 and marks<=100:
    print("Grade:O")
elif marks>=80 and marks<=90:
    print("Grade:A")
elif marks>=65 and marks<=80:
    print("Grade:B")
elif marks>=35 and marks<=65:
    print("Grade:C")
else:
    print("Failed")