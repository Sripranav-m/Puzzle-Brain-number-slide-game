from random import choice
from os import system
from time import sleep
from readchar import readkey
system('cls')
system('color E0')
print('This game is created by \"Sripranav Mannepalli\"....')
sleep(1)
system('cls')
print("THE NUMBER PUZZLE GAME....")
sleep(1)
system('cls')
a=[[' 1',' 2',' 3',' 4'],[' 5',' 6',' 7',' 8'],[' 9','10','11','12'],['13','14','15','  ']]
def display():
    for i in range(0,4):
        for j in range(0,4):
            print("|| "+a[i][j],end=" ")
        print("||"+"\n")
char=''
steps=0
while char!='c':
    system('cls')
    print('press \"a\",\"w\",\"d\",\"s\"  to move left,up,right,down respectively')
    print('press "q" to quit')
    print("You should be able to change the puzzle to the following form to win the game.....")
    display()
    print("press \"c\" to continue......")
    char=readkey()
system('cls')
b=['  ',' 1',' 2',' 3',' 4',' 5',' 6',' 7',' 8',' 9','10','11','12','13','14','15']
a=[[' ' for i in range(0,4)] for j in range(0,4)]
for i in range(0,4):
    for j in range(0,4):
        a[i][j]=choice(b)
        b.remove(a[i][j])
for i in range(0,4):
    for j in range(0,4):
        if a[i][j]=="  ":
            m=i
            n=j
            break
print(f"Number of steps taken::{steps}",end="\n\n")
display()
c=readkey()
p=0
while p==0:
    if c=='w' and m<3:
        t=a[m+1][n]
        a[m+1][n]=a[m][n]
        a[m][n]=t
        steps+=1
    elif c=='s' and m>0:
        t=a[m-1][n]
        a[m-1][n]=a[m][n]
        a[m][n]=t
        steps+=1
    elif c=='d' and n>0:
        t=a[m][n]
        a[m][n]=a[m][n-1]
        a[m][n-1]=t
        steps+=1
    elif c=='a' and n<3:
        t=a[m][n]
        a[m][n]=a[m][n+1]
        a[m][n+1]=t
        steps+=1
    elif c=='q':
        p=1
        break
    else:
        print("enter a valid input,,,wait for a second to enter the input....")
        sleep(1)
    system("cls")
    print(f"Number of steps taken::{steps}",end="\n\n")
    display()
    for i in range(0,4):
        for j in range(0,4):
            if a[i][j]=="  ":
                m=i
                n=j
                break
    if a==[[' 1',' 2',' 3',' 4'],[' 5',' 6',' 7',' 8'],[' 9','10','11','12'],['13','14','15','  ']]:
        p=2
        break
    c=readkey()
if p==1:
    system('cls')
    print("you quitted the game...")
elif p==2:
    print("you win!!!")
