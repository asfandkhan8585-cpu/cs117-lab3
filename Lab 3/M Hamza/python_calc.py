print("----------CALCULATOR-----------")

num1 = float(input ("Enter first Number : " , ))
operator = +
selcet_operator = str(input("Select the operator among: + , - , * , / , // , % : " ))

if slecet_operator == "+":
    operator = +
elif select_operator == "-":
    operator = -
elif select_operator == "*":
    operator = *
elif select_operator == "/":
    operator = /
elif select_operator == "//":
    operator = //
elif select_operator == "%":
    operator = %
else:
    print("Select the operator among: + , - , * , / , // , % ")
    
num2 = float(input("Enter the 2nd Number" )) 
result = num1 + operator + num2
print("Result = ", result)