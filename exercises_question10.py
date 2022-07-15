# marks = [[45, 21, 42, 63], [12, 42, 42, 53], [42, 90, 78, 13], [94, 89, 78, 76], [87, 55, 98, 99]]
# # def my_func(max_marks):
# i=0
# while i<len(marks):
#     j=0
#     max=0
#     max_marks=[]
#     while j<len(marks[i]):
#         if max<marks[i][j]:
#             max=marks[i][j]
#             max_marks.append(max)
#         j=j+1
#     i=i+1
# print(max_marks)
# # print(my_func(max_marks))




from optparse import Option
import random

from click import option


def win():
 print ('You win!')
def lose():
 print ('You lose!')
while True:
 player_choice = input('What do you pick? (rock, paper, scissors)')
 player_choice.strip()
 random_move = random.randint(0, 2)
 moves = ['rock', 'paper', 'scissors']
 computer_choice = moves[random_move]
 if player_choice == computer_choice:
  print ('Draw!')
 elif  player_choice == 'rock' and computer_choice == 'scissors':
  win()
 elif player_choice  == 'paper' and computer_choice == 'scissors':
  lose()
 elif player_choice  == 'scissors' and computer_choice == 'paper':
  win()
 elif player_choice  == 'scissors' and computer_choice == 'rock':
  lose()
 elif player_choice  == 'paper' and computer_choice == 'rock':
  win()
#  elif player_choice  ==  and computer_choice == :
#   lose()
 again = input('Do you want to play again? (y or n)').strip()
 if again == 'n':
  break



