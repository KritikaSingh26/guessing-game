from random import *
L=int(input('Enter the low limit'))
H=int(input('Enter the high limit'))
r=randint(L,H)
count=0
while(True):
    print('is it',r)
    t=(input())
    count+=1
    if(t=='low'):
        L=r+1
        r=randint(L,H)
    elif(t=='high'):
        H=r-1
        r=randint(L,H)
    else:
        print('right guess u won')
        break

print('number of attempts are',count)
