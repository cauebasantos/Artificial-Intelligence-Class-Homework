""" Searchs Algorithms
"""

from node import Node
from problem import Problem



def hill_climbing(problem:Problem, max_attempt=1000, restarts=5000) -> list:
    best_solution = Node()
    
    while restarts:
        max_local = find_local_max(problem, max_attempt)
        if max_local.score > best_solution.score:
            best_solution = max_local

        restarts -= 1
    
    return best_solution

def find_local_max(problem:Problem, max_attempt: int) -> Node:
    attempts = 0

    initial_state = Node()
    initial_state.content = problem.start_state()
    initial_state.score = problem.evaluate_state(initial_state.content)

    while attempts <= max_attempt:
        next_state = problem.best_move_from_state(initial_state.content)
            
        if next_state.score < initial_state.score:
            break
        
        attempts += 1
        initial_state = next_state

    return initial_state