myVar = input("Does it move? (yes/no): ")  
if myVar == "yes":
    
    myNextVar = input("Should it? (yes/no): ")
    if myNextVar == "yes":
        print ('no problem')
    
    elif myNextVar == "no":
        print('Then use duct tape!!!')
        
    else:
        print("Answer my question! You didn't type yes or no.")
        

elif myVar == "no":
    myNextVar = input("Should it? (yes/no): ")

    if myNextVar == "yes":
        print ('Use WD-40!!')
    
    elif myNextVar == "no":
        print ('no problem')
    else:
        print("Answer my question! You didn't type yes or no.")
else:
        print("Answer my question! You didn't type yes or no.")

