import os

def operate(num1, num2, operation):
    if operation =='+':
        return num1+num2
    elif operation =='-':
        return num1-num2
    elif operation =='/':
        return num1/num2
    elif operation =='*':
        return num1*num2
    elif operation =='**':
        return num1**num2
    else:
        return 


exit_program=False
while True:
    num1= int(input("Enter the first number on which you want to perform the operation: "))
    operation=input("Enter the operation you want to perform '+', '-', '/', '*', '**' : ")
    num2=int(input("Enter the second number on which you want to perform the operation: "))

    result=operate(num1, num2, operation)
    print(f"Result of the given numbers are {result}")
    
    choice=input("Enter your choice type 'yes' for continuing or 'quit' for exit :").lower()
    if choice== "quit":
        break
    else:
        
        choose_num=input("YOU want further processing of the result 'y' for yes or 'n' for no :")
        if choose_num=='y':
            while True:
                operation=input("Enter the operation you want to perform '+', '-', '/', '*', '**': ")
                num2=int(input("Enter the second number"))
                result=operate(result, num2, operation)
                print(f"Result of the given numbers are {result}")
                
                choose_num=input("YOU want further processing of the result 'y' for yes or 'n' for no :")
                if choose_num=='n':
                    choice=input("Enter your choice type 'yes' for continuing or 'quit' for exit :").lower()
                    if choice =="quit":
                        exit_program=True
                        break
                    os.system('cls')
                    break
                
        else:
            os.system('cls')


    if exit_program:
        break
