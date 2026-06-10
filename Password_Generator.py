import random

pass_letter=int(input("Enter the letters you want to insert in the password"))
pass_symbols=int(input("Enter the symbols you want to insert in the password"))
pass_num=int(input("Enter the numbers you want to insert in the password"))

letter=['a','b' , 'c','d','e','f', 'g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M']
numbers=[1,2,3,4,5,6,7,8,9,0]
symbols=['!', '@','#','$', '%','^','&','*','(',')','?']

password=[]

for i in range(pass_letter):
    
    choice_l=random.choice(letter)
    password.append(choice_l)
         
for i in range(pass_symbols):
    choice_n=random.choice(symbols)
    password.append(choice_n)

for i in range(pass_num):
    choice_s=str(random.choice(numbers))
    password.append(choice_s)   

#print(password)

random.shuffle(password)
#print(password)

password_str="".join(password)

print("Generated Password is : ",password_str)
