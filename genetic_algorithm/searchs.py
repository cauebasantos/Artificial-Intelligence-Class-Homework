""" Searchs Algorithms
"""
from node import Node
from problem import Problem

def genetic_algorithm(problem:Problem, max_attempt=1000) -> list:
    attempt = 0

    problem.initialize_population()

    while attempt < max_attempt:
        problem.selection()
        problem.mutation()
        attempt += 1
    
    problem.selection()

    return problem.population[0]
