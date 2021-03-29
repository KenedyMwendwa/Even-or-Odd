#Ask the user to enter a number and check whether is an integer
num1=int(input("Enter num1:"))
x = num1 % 2
if x == 0:
    print("num1 is even")
else:
    print("num1 is Odd")