import random
print("ROCK PAPER SCISSORS")
print("INSTRUCTIONS:")
print("ROCK beats SCISSORS\n SCISSORS beats PAPER\n PAPER beats ROCK")
comp_point=0
your_point=0
play=True
while play:
    print("Enter ROCK,PAPER or SCISSORS :")
    u=input()
    o=("ROCK","PAPER","SCISSORS")
    c=random.choice(o)
    print("COMPUTER CHOICE :",c)
    if(c==u):
        print("PLAY AGAIN")
        continue
    elif(c=="ROCK" and u=="PAPER"):
        print("YOU WIN")
        your_point+=1
    elif(c=="ROCK" and u=="SCISSORS"):
        print("YOU LOSE")
        comp_point+=1
    elif(c=="PAPER" and u=="SCISSORS"):
        print("YOU WIN")
        your_point+=1
    elif(c=="PAPER" and u=="ROCK"):
        print("YOU LOSE")
        comp_point+=1
    elif(c=="SCISSORS" and u=="ROCK"):
        print("YOU WIN")
        your_point+=1
    else:
        print("YOU LOSE")
        comp_point+=1
    print("DO YOU WANT TO PLAY AGAIN (Y/N): ")
    yn=input()
    if yn=="Y":
        continue
    else:
        print("GAME OVER")
        play=False
print("SCORECARD:")
print("YOU: ",your_point)
print("COMPUTER: ",comp_point)
