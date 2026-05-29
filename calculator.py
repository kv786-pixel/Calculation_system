#functions for operations
# user input
# print result

#function to add two numbers
def addition(num1,num2):
    return num1+num2

def subtraction(num1,num2):
    return num1-num2

def multiply(num1,num2):
    return num1*num2

def division(num1,num2):
    return num1/num2

def modulus(num1,num2):
    return num1%num2

def avrage(num1,num2):
    return (num1+num2)/2

# user input
print("please select a operation:\n " \
    "1.addion \n" \
    "2.subtraction \n" \
    "3.multiply \n" \
    "4.division \n" \
    "5.modulus \n" \
    "6.avrage \n")
select=int(input("select a operation from 1 to 6: "))
number1=int(input("enter first number "))
number2=int(input("enter second number "))

# print result
if select==1:
    print(number1, "+", number2, "=", \
          addition(number1,number2))
    
elif select==2:
    print(number1, "-", number2, "=", \
          subtraction(number1,number2))
    
elif select==3:
    print(number1, "*", number2, "=", \
          multiply(number1,number2))
    
elif select==4:
    print(number1, "/", number2, "=", \
          division(number1,number2))
    
elif select==5:
    print(number1, "%", number2, "=", \
          modulus(number1,number2))
    
elif select==6:
    print("(",number1, "+", number2,")","/" ,"2", "=", \
          avrage(number1,number2))
else:
    print("invalid operation")