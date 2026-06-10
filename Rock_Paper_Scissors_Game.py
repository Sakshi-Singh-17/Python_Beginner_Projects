import random

list=[ '✊', '🖐', '✌']

while True:

    user_choice=int(input("Enter '0' for rock, '1' for paper,'2' for scissor : "))
    print(user_choice)
    print(list[user_choice])
    comp_choice=random.randint(0,2)
    print(comp_choice)
    print(list[comp_choice])
    
    if comp_choice==2 and  user_choice==0:
        print("You win :) ")
    elif comp_choice==0 and  user_choice==2:
        print("You loose :( ")
    elif comp_choice> user_choice:
        print("You loose :( ")
    elif comp_choice < user_choice:
        print("You win :) ")
    elif comp_choice == user_choice :
        print("Game Draw :| ")
    else:
        print("ENTER CORRECT NUMBER : ")
        
    check= input("Enter your choice for further play type 'yes' or if you want to quit the game type 'no' : ").lower()
    if check== "no":
        break
