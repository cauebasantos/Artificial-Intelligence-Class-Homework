""" Main code
"""

import time
from agent import Agent
from environment import Environment
from problem import Problem

START_TIME = time.time()

INITIAL_STATE = int(input("Type the initial state: "))
FINAL_STATE = int(input("Type the final state: "))
print()

if INITIAL_STATE == FINAL_STATE:
    print('You\'re already here\n')
else: 
    PROBLEM = Problem(FINAL_STATE)

    ENVIRONMENT = Environment(INITIAL_STATE)
    AGENT = Agent(ENVIRONMENT)
    
    print('Actual Station:')
    ENVIRONMENT.print_state()
    
    print()
    
    AGENT.do_action(PROBLEM)
    print('Stations to go:')
    while AGENT.solve_stack:
        AGENT.do_action(PROBLEM)

print('\nThank you for using our system.')
print(f"--- {(time.time() - START_TIME)} seconds ---")
