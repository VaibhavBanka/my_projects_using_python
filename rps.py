import random
a=['R','P','S']
s=0
sc=0
d=0
while s+sc!=5:
    n=input('Enter your choice(R,P,S):'.upper())
    b=random.choice(a)
    print('Computer choice:',b)
    if (n=='R' and b=='P'):
        sc+=1
    elif (n=='P' and b=="S"):
        sc+=1
    elif (n=='S' and b=='R'):
        sc+=1
    elif (n=='P' and b=='R'):
        s+=1
    elif (n=='S' and b=="P"):
        s+=1
    elif (n=='R' and b=='S'):
        s+=1
    elif n==b:
        d+=1
    else:
        print('Invalid input, please try again')
print('Your score:',s)
print('Computer score:',sc)
print('Draws:',d)
if s>sc:
    print('You won by',(s-sc),'points')
elif s<sc:
    print('Computer won by',(sc-s),'points')
    
