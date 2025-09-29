num1 = float(input("enter first number"))
num2 = float(input("enter the second number"))

choice = input("enter the operator" )
if choice == "+":
    result = num1+num2
elif choice =="-":
    result = num1-num2
elif choice == "/":
    result = num1/num2
elif choice =="*":
    result = num1*num2
elif choice =="%":
    result = num1%num2
elif choice == "//":
    result = num1//num2
else:
    print("invalid choice")

print("result of the operation is =",result)