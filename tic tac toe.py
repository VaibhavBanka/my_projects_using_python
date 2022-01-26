import sys
board=[[0,0,0],
      [0,0,0],
      [0,0,0]]
print("   0, 1, 2")
count=0
for i in board:
    print(count,i)
    count+=1
pl=[0]
while True:
    
    player=int(input("Enter the player number (1 or 2):"))
    row=int(input("Enter the row in which you want to enter:"))
    column=int(input("Enter the column in which you want to enter:"))
    pl.append(player)

    if row==0 and column==0:
        board[0][0]=player
        for i in board:
            for j in range(0,len(pl)-1):
              if pl[j]==pl[j+1]:
                print("***NO CHEATING***IT'S NOT YOUR TURN!!!")
                continue
                
            else:
                print(i)  
                if board[0][0]==board[0][1]==board[0][2]!=0 or board[1][0]==board[1][1]==board[1][2]!=0 or board[2][0]==board[2][1]==board[2][2]!=0 or board[0][0]==board[1][0]==board[2][0]!=0 or board[0][1]==board[1][1]==board[2][1]!=0 or board[0][2]==board[1][2]==board[2][2]!=0 or board[0][0]==board[1][1]==board[2][2]!=0 or board[0][2]==board[1][1]==board[2][0]!=0:
                   print("Player",player,"Wins!!!!!!\nCongratulations Player",player)
                   sys.exit()
               
                
        
    

    elif row==0 and column==1:
        board[0][1]=player
        for i in board:
            for j in range(0,len(pl)-1):
              if pl[j]==pl[j+1]:
                print("***NO CHEATING***IT'S NOT YOUR TURN!!!")
                continue
                
            else:
                print(i)  
                if board[0][0]==board[0][1]==board[0][2]!=0 or board[1][0]==board[1][1]==board[1][2]!=0 or board[2][0]==board[2][1]==board[2][2]!=0 or board[0][0]==board[1][0]==board[2][0]!=0 or board[0][1]==board[1][1]==board[2][1]!=0 or board[0][2]==board[1][2]==board[2][2]!=0 or board[0][0]==board[1][1]==board[2][2]!=0 or board[0][2]==board[1][1]==board[2][0]!=0:
                   print("Player",player,"Wins!!!!!!\nCongratulations Player",player)
                   sys.exit()
        

    elif row==0 and column==2:
        board[0][2]=player
        for i in board:
            for j in range(0,len(pl)-1):
              if pl[j]==pl[j+1]:
                print("***NO CHEATING***IT'S NOT YOUR TURN!!!")
                continue
                
            else:
                print(i)  
                if board[0][0]==board[0][1]==board[0][2]!=0 or board[1][0]==board[1][1]==board[1][2]!=0 or board[2][0]==board[2][1]==board[2][2]!=0 or board[0][0]==board[1][0]==board[2][0]!=0 or board[0][1]==board[1][1]==board[2][1]!=0 or board[0][2]==board[1][2]==board[2][2]!=0 or board[0][0]==board[1][1]==board[2][2]!=0 or board[0][2]==board[1][1]==board[2][0]!=0:
                   print("Player",player,"Wins!!!!!!\nCongratulations Player",player)
                   sys.exit() 
        

    elif row==1 and column==0:
        board[1][0]=player
        for i in board:
            for j in range(0,len(pl)-1):
              if pl[j]==pl[j+1]:
                print("***NO CHEATING***IT'S NOT YOUR TURN!!!")
                continue
                
            else:
                print(i)  
                if board[0][0]==board[0][1]==board[0][2]!=0 or board[1][0]==board[1][1]==board[1][2]!=0 or board[2][0]==board[2][1]==board[2][2]!=0 or board[0][0]==board[1][0]==board[2][0]!=0 or board[0][1]==board[1][1]==board[2][1]!=0 or board[0][2]==board[1][2]==board[2][2]!=0 or board[0][0]==board[1][1]==board[2][2]!=0 or board[0][2]==board[1][1]==board[2][0]!=0:
                   print("Player",player,"Wins!!!!!!\nCongratulations Player",player)
                   sys.exit() 
        

    elif row==1 and column==1:
        board[1][1]=player
        for i in board:
            for j in range(0,len(pl)-1):
              if pl[j]==pl[j+1]:
                print("***NO CHEATING***IT'S NOT YOUR TURN!!!")
                continue
                
            else:
                print(i)  
                if board[0][0]==board[0][1]==board[0][2]!=0 or board[1][0]==board[1][1]==board[1][2]!=0 or board[2][0]==board[2][1]==board[2][2]!=0 or board[0][0]==board[1][0]==board[2][0]!=0 or board[0][1]==board[1][1]==board[2][1]!=0 or board[0][2]==board[1][2]==board[2][2]!=0 or board[0][0]==board[1][1]==board[2][2]!=0 or board[0][2]==board[1][1]==board[2][0]!=0:
                   print("Player",player,"Wins!!!!!!\nCongratulations Player",player)
                   sys.exit() 
        

    elif row==1 and column==2:
        board[1][2]=player
        for i in board:
            for j in range(0,len(pl)-1):
              if pl[j]==pl[j+1]:
                print("***NO CHEATING***IT'S NOT YOUR TURN!!!")
                continue
                
            else:
                print(i)  
                if board[0][0]==board[0][1]==board[0][2]!=0 or board[1][0]==board[1][1]==board[1][2]!=0 or board[2][0]==board[2][1]==board[2][2]!=0 or board[0][0]==board[1][0]==board[2][0]!=0 or board[0][1]==board[1][1]==board[2][1]!=0 or board[0][2]==board[1][2]==board[2][2]!=0 or board[0][0]==board[1][1]==board[2][2]!=0 or board[0][2]==board[1][1]==board[2][0]!=0:
                   print("Player",player,"Wins!!!!!!\nCongratulations Player",player)
                   sys.exit()
        

    elif row==2 and column==0:
        board[2][0]=player
        for i in board:
            for j in range(0,len(pl)-1):
              if pl[j]==pl[j+1]:
                print("***NO CHEATING***IT'S NOT YOUR TURN!!!")
                continue
                
            else:
                print(i)  
                if board[0][0]==board[0][1]==board[0][2]!=0 or board[1][0]==board[1][1]==board[1][2]!=0 or board[2][0]==board[2][1]==board[2][2]!=0 or board[0][0]==board[1][0]==board[2][0]!=0 or board[0][1]==board[1][1]==board[2][1]!=0 or board[0][2]==board[1][2]==board[2][2]!=0 or board[0][0]==board[1][1]==board[2][2]!=0 or board[0][2]==board[1][1]==board[2][0]!=0:
                   print("Player",player,"Wins!!!!!!\nCongratulations Player",player)
                   sys.exit() 
        
            
    elif row==2 and column==1:
        board[2][1]=player
        for i in board:
            for j in range(0,len(pl)-1):
              if pl[j]==pl[j+1]:
                print("***NO CHEATING***IT'S NOT YOUR TURN!!!")
                continue
                
            else:
                print(i)  
                if board[0][0]==board[0][1]==board[0][2]!=0 or board[1][0]==board[1][1]==board[1][2]!=0 or board[2][0]==board[2][1]==board[2][2]!=0 or board[0][0]==board[1][0]==board[2][0]!=0 or board[0][1]==board[1][1]==board[2][1]!=0 or board[0][2]==board[1][2]==board[2][2]!=0 or board[0][0]==board[1][1]==board[2][2]!=0 or board[0][2]==board[1][1]==board[2][0]!=0:
                   print("Player",player,"Wins!!!!!!\nCongratulations Player",player)
                   sys.exit() 
      

    elif row==2 and column==2:
        board[2][2]=player
        for i in board:
            for j in range(0,len(pl)-1):
              if pl[j]==pl[j+1]:
                print("***NO CHEATING***IT'S NOT YOUR TURN!!!")
                continue
                
            else:
                print(i)  
                if board[0][0]==board[0][1]==board[0][2]!=0 or board[1][0]==board[1][1]==board[1][2]!=0 or board[2][0]==board[2][1]==board[2][2]!=0 or board[0][0]==board[1][0]==board[2][0]!=0 or board[0][1]==board[1][1]==board[2][1]!=0 or board[0][2]==board[1][2]==board[2][2]!=0 or board[0][0]==board[1][1]==board[2][2]!=0 or board[0][2]==board[1][1]==board[2][0]!=0:
                   print("Player",player,"Wins!!!!!!\nCongratulations Player",player)
                   sys.exit()

    else:
        print("Incorrect input....Please play wisely")



        

    
    
