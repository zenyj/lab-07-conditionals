number1= int(input("Give me a number:"))
number2= int(input("Give me another number:"))
operation= str(input("Give me a operation:"))
    
if operation =="mul":
    print(number1 * number2)
    
elif operation =="div":
    print(number1 / number2)
    
elif operation =="mod":
    print(number1 % number2)

else: 
    print('***Invalid operation***')