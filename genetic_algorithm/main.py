""" Main code
"""

import time
from searchs import genetic_algorithm
from problem import Problem

START_TIME = time.time()

PROBLEM = Problem()

max_attempt = 1000

print(f'Running genetic algorithm with {max_attempt} generations. It could take some time. Please wait.')
print(f'Estimated time on my computer: {max_attempt*2.1/100} seconds\n')

best_solution = genetic_algorithm(PROBLEM, max_attempt)

print('--- A solution was found! ---\n')
print(f'Best configuration: {best_solution.chromosome}, fitness: {best_solution.fitness}\n')
print(f"--- {(time.time() - START_TIME)} seconds ---")
