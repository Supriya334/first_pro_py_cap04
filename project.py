#MY FIRST PROJECT OF PYTHON😃



import random
options=("rock","paper","scissors")

running= True

while running:
    player=None
    computer=random.choice(options)


    while player not in options:
        player=input("enter a choice(rock,paper,scissors): ")




    print(f"Player:{player}")

    print(f"Computer:{computer}")

    if (player==computer):
        print("Tie🎀")

    elif(player==   "rock⛰️"   and computer==   "scissors✂️"   ):
        print("You Win! 😎")

    elif(player==   "paper📝"    and computer==     "rock⛰️"      ):
        print("You Win!😎 ")



    elif(player==   "scissors✂️" and computer==     "paper📝"    ):
        print("You Win! 😎")


    else:

        print("You Loose! 😐")    

    play_again= input("play again?(y/n):").lower()
    if not play_again=="y":
        running=False




print("Thanks For Playing❤️")        










    #Made By:-
    #Supriya
    #Cap04_146
    

    