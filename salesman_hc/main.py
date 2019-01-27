""" Main code
"""

import time
from searchs import hill_climbing
from problem import Problem

START_TIME = time.time()

PROBLEM = Problem()

max_attempt = 1000
restarts = 5000

print(f'Running hill climbing with {max_attempt} attempts and {restarts} '\
'restarts. It could take some time. Please wait.\n')

best_solution = hill_climbing(PROBLEM)

print('--- A solution was found! ---\n')

print(f'Best path: {best_solution.content}, distance: {-best_solution.score}\n')

print(f"--- {(time.time() - START_TIME)} seconds ---")
