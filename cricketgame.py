import random
import time
def bat():
    score=0
    wicket=0
    while wicket!=n:
        f=int(input("enter your run choice:"))
        g=random.choice(a)
        print("Computer chose:",g)
        if f!=g:
            score+=f
            print("Runs scored:",score,'fall of wickets:',wicket)
        else:
            wicket+=1
            print("Runs scored:",score,'fall of wickets:',wicket)
    print("\nTarget for computer is\n",score+1)
    scc=0
    wcc=0
    while scc!=score and wcc!=n:
        j=int(input("enter your choice:"))
        k=random.choice(a)
        print("Computer chose:",k)
        if j!=k:
            scc+=k
            print("Runs left:",((score+1)-scc),"Wickets left:",(n-wcc))
        else:
            wcc+=1
            print("Runs left:",((score+1)-scc),"wickets left:",(n-wcc))
    if scc==score:
        print("Computer wins by",(n-wcc),"wickets")
    elif wcc==n:
        print("You win by",(score-scc),'runs')

def bowl():
    sc=0
    wc=0
    while wc!=n:
        h=int(input("Enter your choice:"))
        i=random.choice(a)
        print("Computer chose:",i)
        if h!=i:
            sc+=i
            print("Runs scored:",sc,'fall of wickets:',wc)
        else:
            wc+=1
            print("Runs scored:",sc,'fall of wickets:',wc)

    print("\nTarget for you is\n",sc+1)
    chase=0
    cw=0
    while chase!=sc and cw!=n:
        l=int(input("Enter your choice:"))
        m=random.choice(a)
        print("Computer chose:",m)
        if l==m:
            cw+=1
            print("Runs left:",((sc+1)-chase),"Wickets left:",(n-cw))
        else:
            chase+=l
            print("Runs left:",((sc+1)-chase),"Wickets left:",(n-cw))
    if chase==sc:
        print("You won by",(n-cw),'wickets')
    elif cw==n:
        print("Computer won by",(sc-chase),'runs')

a=[1,2,3,4,5,6,10,20,40,50,100]
print("WELCOME TO THE WORLD OF CRICKET (ROCK AND ROLL CRICKET)")
toss=["Heads","Tail"]
print("Here there are 11 types of runs (1,2,3,4,5,6,10,20,40,50,100)\nYou can choose any")
n=int(input("Enter the number of wickets you want to play for(1,3,5):"))
print("ITS TIME FOR THE TOSS NOW")
b=input("enter your choice for toss (Heads or Tail):")
c=random.choice(toss)
print("Your call is",b,end='')
time.sleep(2)
print(" and the coin shows",c)
d=["Bat",'Bowl']
if b==c:
    print("congrats you won the toss. ",end='')
    e=input("what would you like to do first(Bat or Bowl):")
    if e=='Bat':
        bat()
    else:
        bowl()
else:
    print("Computer won the toss and chose to:",random.choice(d))
    z=random.choice(d)
    if z=="Bat":
        bat()
    else:
        bowl()



