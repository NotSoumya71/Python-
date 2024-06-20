#!/usr/bin/env python
# coding: utf-8

# In[1]:


def rock_paper_scissors(computer,score):
    player = input("Rock, Paper, Scissors?  ")
    if player.lower() == computer:
        print("Tie! You & the computer both chose",player)
    elif player.lower() == "rock":
        if computer == "scissors":
            print("You get a point! \n computer chose",computer)
            score+=1
        else:
            print("You lost!\n computer chose",computer)
    elif player.lower() == "paper":
        if computer == "rock":
            print("You get a point! \n computer chose",computer)
            score+=1
        else:
            print("You lost!\n computer chose",computer)
    elif player.lower() == "scissors":
        if computer == "paper":
            print("You get a point! \n computer chose",computer)
            score+=1
        else:
            print("You lost!\n computer chose",computer)
    else:
        print("Wrong spelling :(")
        
        
game = ["rock","paper","scissors"]
score = 0
import random
for _ in range(5):
    random_index = random.randint(0, 2)
    comp = game[random_index]
    rock_paper_scissors(comp, score)


# In[ ]:




