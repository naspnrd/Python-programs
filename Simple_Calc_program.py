#add operation

def Add(num1,num2):
    return num1+num2

#subtract operation

def Subtract(num1, num2):
    return num1-num2

#multiply operation

def Multiply(num1, num2):
    return num1*num2

#divide Operation

def Divide(num1, num2):
    return num1/num2

print("Enter Your Choice From the Given Options Below:\n ",
  "1. Addition of two numbers \n"
     "2. Subtraction of two numbers \n"
        "3. Multiplication of two numbers \n"
            "4. Division of two numbers \n")

ch = int(input("Enter your choice "))

num1 =int(input("Enter Your First Number "))
num2 =int(input("Enter Your Second Number "))

if ch == 1:
    print(num1, '+' , num2, '=' ,Add(num1,num2))

elif ch == 2:
    print(num1, '+' , num2, '=' ,Subtract(num1,num2))

elif ch == 3:
    print(num1, '+' , num2, '=' ,Multiply(num1,num2))

elif ch == 4:
    print(num1, '+' , num2, '=' ,Divide(num1,num2))

else:
    print("invalid choice")

    
          
