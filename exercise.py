#Given two integer numbers return their product only if the product is equal to or lower than 1000, else return their sum.
num1=input("enter first number: ")
num2=input("enter second number: ")
num= num1*num2
if (num<=100):
    print(num)
else:
    print(num1+num2)