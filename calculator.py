

print("SIMPLE CALCULATOR")
print("1. ADDITION")
print("2. SUBTRACTION")
print("3. MULTIPLICATION")
print("4. DIVISION")
num=int(input("Enter the operation you want to perform:"))
num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))
if(num==1):
    print(num1,"+",num2,"= ",num1+num2)
elif(num==2):
    print(num1,"-",num2,"= ",num1-num2)
elif(num==3):
    print(num1,"*",num2,"= ",num1*num2)
elif(num==4):
    if(num2==0):
        print("ERROR...Division by 0 not possible:")
    else:
        print(num1,"/",num2,"= ",num1/num2)
else:
    print("INVALID INPUT")
    
