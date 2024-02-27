#code for password generator program
# importing all methods from random class
from random import *

# list of all characters in lower case
l_case=[]
for i in range(97,123):
    l_case.append(chr(i))

#print(l_case)

# list of all characters in upper case
u_case=[]
for i in range(65,91):
    u_case.append(chr(i))

#print(u_case)

# list of all numbers from 0 to 9
numbers=[]
for i in range(0,10):
    numbers.append(i)

#print(num)

# list of all special character
sp_chr=[]
for i in range(33,42):
    sp_chr.append(chr(i))
# sp_chr.append("?")
# print(sp_chr)

# function to generate password
def passgen(lc,uc,num,sp):
    passw=[]
    for i in range(0,lc):
        passw.append(str(choice(l_case)))
    for i in range(0,uc):
        passw.append(str(choice(u_case)))
    for i in range(0,num):
        passw.append(str(choice(numbers)))
    for i in range(0,sp):
        passw.append(str(choice(sp_chr)))
    
    shuffle(passw)
    
    print("Password:",end=" ")
    print("".join(map(str,passw)))
    

# function to initialize the program
def start():
    print("Welcome to Python password generator!")
    lc=int(input("how much lower case character you want:"))
    uc=int(input("how much upper case character you want:"))
    num=int(input("how much digits you want:"))
    sp=int(input("how much special character you want:"))

    passgen(lc,uc,num,sp)

# function call
start()
