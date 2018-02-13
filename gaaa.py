from random import *
sum=0
counter = 0
rand = False

print ("Choose: \n 1-VS PC \n 2-VS Human")
p=int(input())
while True and p==2:
    print ("sum=" , sum)
    p1=int(input("Player 1 : \n"))
    while (p1>10 or p1==0):
        print("Choose number Between 1-10")
        p1=int(input("Player 1 : \n"))
    while (p1+sum>100):
        c=100-sum
        print("Choose number between (1-" , c ,")")
        p1=int(input("Player 1 : "))
    sum=sum+p1
    if sum==100:
        print("player 1 is ther winner!!!!")
        break
    print ("sum=" , sum)
    p1=int(input("Player 2 : "))
    while (p1>10):
        print("Choose number Between 1-10")
        p1=int(input("Player 2 : "))
    while (p1+sum>100):
        c=100-sum
        print("Choose number between (1-" , c ,")")
        p1=int(input("Player 2 : "))
    sum=sum+p1
    if sum==100:
        print("player 2 is ther winner!!!!")
        break
while True and p==1:
    
    print ("sum= " , sum)
    p1=int(input("Player 1 : "))
    while (p1>10 or p1==0):
        print("Choose number Between 1-10")
        p1=int(input("Player 1 : "))
    while (p1+sum>100):
        c=100-sum
        print("Choose number between (1-" , c ,")")
        p1=int(input("Player 1 "))
    sum=sum+p1
    counter+=1
    if sum==100:
        print("player 1 is ther winner!!!!")
        break
    u=0
    pc = 0
    if (counter==1 and p1 !=1):
        pc = 12-p1
        counter +=1
    elif (counter ==1 and p1==1):
        pc = randint(1,10)
        rand = True
    elif(rand == False):
        pc = 11-p1
    else :
        pc = randint(1,10)
    sum+=pc
    if (sum>100):
        sum-=pc
        pc = 100-sum
        sum = 100
    print ("pc : " , pc)
    if (sum==100):
        print("You Lost")
        break

        
    
        
    
        
        
