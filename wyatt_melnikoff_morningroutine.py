import random
import os

#a message put up if the computer wins rock, paper, scissors.
bot_win_message = '''
           /$$$$$$                                                /$$                               /$$      /$$ /$$                    
 /$$__  $$                                              | $$                              | $$  /$ | $$|__/                    
| $$  \__/  /$$$$$$  /$$$$$$/$$$$   /$$$$$$  /$$   /$$ /$$$$$$    /$$$$$$   /$$$$$$       | $$ /$$$| $$ /$$ /$$$$$$$   /$$$$$$$
| $$       /$$__  $$| $$_  $$_  $$ /$$__  $$| $$  | $$|_  $$_/   /$$__  $$ /$$__  $$      | $$/$$ $$ $$| $$| $$__  $$ /$$_____/
| $$      | $$  \ $$| $$ \ $$ \ $$| $$  \ $$| $$  | $$  | $$    | $$$$$$$$| $$  \__/      | $$$$_  $$$$| $$| $$  \ $$|  $$$$$$ 
| $$    $$| $$  | $$| $$ | $$ | $$| $$  | $$| $$  | $$  | $$ /$$| $$_____/| $$            | $$$/ \  $$$| $$| $$  | $$ \____  $$
|  $$$$$$/|  $$$$$$/| $$ | $$ | $$| $$$$$$$/|  $$$$$$/  |  $$$$/|  $$$$$$$| $$            | $$/   \  $$| $$| $$  | $$ /$$$$$$$/
 \______/  \______/ |__/ |__/ |__/| $$____/  \______/    \___/   \_______/|__/            |__/     \__/|__/|__/  |__/|_______/ 
                                  | $$                                                                                         
                                  | $$                                                                                         
                                  |__/
'''
#a message put up if the user wins Rock, paper, scissors.
user_win_message = '''
          /$$   /$$                                     /$$      /$$ /$$                    
| $$  | $$                                    | $$  /$ | $$|__/                    
| $$  | $$  /$$$$$$$  /$$$$$$   /$$$$$$       | $$ /$$$| $$ /$$ /$$$$$$$   /$$$$$$$
| $$  | $$ /$$_____/ /$$__  $$ /$$__  $$      | $$/$$ $$ $$| $$| $$__  $$ /$$_____/
| $$  | $$|  $$$$$$ | $$$$$$$$| $$  \__/      | $$$$_  $$$$| $$| $$  \ $$|  $$$$$$ 
| $$  | $$ \____  $$| $$_____/| $$            | $$$/ \  $$$| $$| $$  | $$ \____  $$
|  $$$$$$/ /$$$$$$$/|  $$$$$$$| $$            | $$/   \  $$| $$| $$  | $$ /$$$$$$$/
 \______/ |_______/  \_______/|__/            |__/     \__/|__/|__/  |__/|_______/          
                  '''
#a message put up if the friends wins Rock, Paper, Scissors
friend_win_message = ''' 
$$$$$$        /$$                           /$$       /$$      /$$ /$$                    
| $$_____/       |__/                          | $$      | $$  /$ | $$|__/                    
| $$     /$$$$$$  /$$  /$$$$$$  /$$$$$$$   /$$$$$$$      | $$ /$$$| $$ /$$ /$$$$$$$   /$$$$$$$
| $$$$$ /$$__  $$| $$ /$$__  $$| $$__  $$ /$$__  $$      | $$/$$ $$ $$| $$| $$__  $$ /$$_____/
| $$__/| $$  \__/| $$| $$$$$$$$| $$  \ $$| $$  | $$      | $$$$_  $$$$| $$| $$  \ $$|  $$$$$$ 
| $$   | $$      | $$| $$_____/| $$  | $$| $$  | $$      | $$$/ \  $$$| $$| $$  | $$ \____  $$
| $$   | $$      | $$|  $$$$$$$| $$  | $$|  $$$$$$$      | $$/   \  $$| $$| $$  | $$ /$$$$$$$/
|__/   |__/      |__/ \_______/|__/  |__/ \_______/      |__/     \__/|__/|__/  |__/|_______/ 
                    '''                                                                                    

#users score if they win the round.
p1_score=0
#computer score if they win the round.
p2_score=0
#My list
RPS = ["Rock", "paper", "scissors"]
#forever loop
while True:
#Enter Player 1 name
    p1_name = input("Player 1, enter your name: ")
#do you want to play a friend or a bot in Rock, Paper, Scissors
    two_player = input("Play the bot or a friend? ").lower()
#Chose two player or not two player

    if two_player == "bot":
#Display message player 2 win message or bot win message depending on what you chose
        p2_win_message = bot_win_message
#Chose a name depending if you chose player 2 as a bot or friend 
        p2_name = "bot"
#Chose two player or not two player
    elif two_player == "friend":
#Display message player 2 win message or bot win message depending on what you chose
        p2_win_message = friend_win_message
#Player 2 name is equal to player 2, enter your name
        p2_name = input("Player 2, enter your name: ")
#another if statment 
    else:
#display message Please enter bot or friend 
        print("Please enter bot or friend")
#within loop
        continue
#highest score user and bot can get to is 50 points
    score_limit = 50
#

    while p1_score < score_limit and p2_score < score_limit:
            #user chooses either rock,paper or scissors.
        p1_rps=input(f"{p1_name}, Rock paper scissors? ").lower()

        if two_player == "bot":
        #computer generates a random choiuce from my list. 
            p2_rps = random.choice(RPS)
        else:
            os.system("cls")
            p2_rps=input(f"{p2_name}, Rock paper scissors? ").lower()
            os.system("cls")
    #if the user and computer pick the same element it ends in a tie.
        print(f"{p1_name} chose {p1_rps} and {p2_name} chose {p2_rps}")

        if p1_rps == p2_rps:
            print("tie")
    #if the user picks paper and the computer picks scissors.
        elif p1_rps =="paper" and p2_rps == "scissors":
    #display message computer wins (bot message).
            print(p2_win_message)
    #add 10 points to the computers score.
            p2_score+=10
    #if user picks scissors and computer picks paper.
        elif p1_rps =="scissors" and p2_rps == "paper":
    #display message user wins (user_win_message). 
            print(user_win_message)
    #add 10 points to user score.
            p1_score+=10
    #if user picks paper and computer picks rock.
        elif p1_rps =="paper" and p2_rps == "rock" :
    #display message user wins (user_win_message).
            print(user_win_message)
    #add 10 points to users score.
            p1_score+=10
    #is user pick rock and computer picks paper.
        elif p1_rps =="rock" and p2_rps == "paper":
    #display message computer wins (bot_win_message).
            print(p2_win_message)
    #add 10 points to computers score.
            p2_score+=10
    #if user picks rock and computer picks scissors.
        elif p1_rps =="rock" and p2_rps == "scissors":
    #display message user wins (user_win_message).
            print(user_win_message)
    #add 10 points to users score.
            p1_score+=10
    #if user picks scissors and computer picks rock.
        elif p1_rps =="scissors" and p2_rps == "rock" :
    #display message computer wins (bot_win_message).
            print(p2_win_message)
    #add 10 points to computers score.
            p2_score+=10
    #display user final score.
        print(f"{p1_name} score: {p1_score}")
    #display computers final score.
        print(f"{p2_name} score: {p2_score}")

        play_again = input("Would you like to play again? y/n: ").lower()

        if play_again == "n":
            break
