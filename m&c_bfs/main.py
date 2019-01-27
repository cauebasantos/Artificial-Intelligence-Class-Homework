""" Main code
"""

import time
from agent import Agent
from environment import Environment
from problem import Problem

START_TIME = time.time()

PROBLEM = Problem()
INITIAL_STATE = [3,3,0,0,0]
ENVIRONMENT = Environment(INITIAL_STATE)
AGENT = Agent(ENVIRONMENT)
print('Estado atual:')
ENVIRONMENT.print_state()
AGENT.do_action(PROBLEM)
print('Resolução:')
while AGENT.solve_stack:
    AGENT.do_action(PROBLEM)
print('End')
print('Sim, é uma boa ideia verificar a existência de estados repetidos.')
print('O tempo saiu de aproximadamente 0.32 segundos para o a seguir')
print(f"--- {(time.time() - START_TIME)} seconds ---")
