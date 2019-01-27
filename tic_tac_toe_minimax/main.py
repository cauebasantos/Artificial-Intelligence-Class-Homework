""" Main code
"""

import time
from agent import Agent
from environment import Environment
from problem import Problem
from searchs import minimax
from node import Node

START_TIME = time.time()

PROBLEM = Problem()
INITIAL_STATE = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
ENVIRONMENT = Environment(INITIAL_STATE)

print('--- WELCOME TO TIC-TAC-TOE GAME! ---')
print('YOU WILL PLAY AS THE \'X\', YOU GO FIRST')
print('PLEASE, TYPE WHERE YOU WANT TO PLAY AS FOLLOW')
print('0 | 1 | 2 \n' \
      '--------- \n' \
      '3 | 4 | 5 \n' \
      '--------- \n' \
      '6 | 7 | 8 \n')

while not PROBLEM.is_game_over(Node(ENVIRONMENT.get_state()))[0]:
    move_p1 = int(input('YOUR MOVE: '))
    while move_p1 < 0 or move_p1 > 8 or ENVIRONMENT.get_state()[move_p1] != ' ':
        print('PLEASE TYPE A VALID DIGIT')
        move_p1 = int(input('YOUR MOVE: '))

    ENVIRONMENT.get_state()[move_p1] = 'X'
    move_p1 = ENVIRONMENT.get_state()
    print('PLAY ONE PLAYED:')
    print(ENVIRONMENT)

    move_p2 = minimax(PROBLEM, Node(ENVIRONMENT.get_state()), player=1).content
    ENVIRONMENT.modify_state(move_p2)
    print('THE MACHINE PLAYED:')
    print(ENVIRONMENT)

game_end = PROBLEM.is_game_over(Node(ENVIRONMENT.get_state()))[1].score
if game_end == 0:
    game_end = 'DRAW'
elif game_end > 0:
    game_end = 'YOU WON'
else:
    game_end = 'MACHINE WON'

print(f'--- GAME OVER: {game_end} ---\n')
print('Thank you for playing!\n')

print(f'--- {(time.time() - START_TIME)} seconds ---')