n=input("Enter the operation:")
num1=(int)(input("Enter the first number:"))
num2=(int)(input("Enter the second number:"))

if(n=="*"):
    result=num1 * num2
elif(n=="/"):
    result=num1/num2
elif(n=="+"):
    result=num1+num2
elif(n=="-"):
    result=num1-num2
else:
    pass

print(result)
