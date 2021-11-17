# -*- coding: utf-8 -*-
# @Time    : 
# @Author  : huoyanyang
# @Site    : 
# @File    : 
# @Software: PyCharm
import importlib
# import random

choices =["Rock","Paper","Scissors"]
class computerplayer(object):
     player=False
     cpu_score=0
     player_score=0
     def  __init__(self,computer="Paper"):
         self.ran=importlib.import_module( "random" )
         self.computer =computer
         # self.computer = random.choice(computerplayer.choices)

     def tou(self):
       while True:
         self.computer = self.ran.choice( choices )
         player =input("Rock,Paper or Scissors?").capitalize()
         if player == self.computer:
             print("Tie!")
         elif player == "Rock":
             if self.computer=="Paper":
                 print("You lose!",self.computer,"covers",player)
                 computerplayer.cpu_score+=1
             elif self.computer == "Scissors":
                 print("You Win!",player,"samshes",self.computer)
                 computerplayer.player_score+=1
         elif player =="Paper":
              if self.computer =="Scissors":
                  print("You lose",self.computer,"cut",player)
                  computerplayer.cpu_score+=1
              else:
                  print("You win",player,"covers",self.computer)
                  computerplayer.player_score+=1
         elif player=="Scissors":
             if self.computer == "Rock":
                 print("You lose",self.computer,"smashes",player)
                 computerplayer.cpu_score+=1
             else:
                 print("You win",player,"covers",self.computer)
                 computerplayer.player_score+=1
         elif player =="E":
             print("Final Scores:")
             print(f"CPU:{computerplayer.cpu_score}")
             print(f"player:{computerplayer.player_score}")
         else:
             print("That is not a valid play.please,check you spelling")

if __name__ =="__main__":
    computerplayer().tou()
