""" Searchs Algorithms
"""

from node import Node
from problem import Problem

def search_solution(state:list, problem:Problem, keep_history=False, history_len=100) -> list:
    "" """ Search the sequence of actions that leads to the goal state and puts
    it on self.solve_stack variable 
    """
    # keep up a history of most recent states viseted
    history = [] 
    # create the root node with the current state
    root = Node(state, 'None', None)  
    frontier = [root]  # create the frontier queue and append the root to it
    # holds the stack sequence of actions the agent is going to do to 
    # achieve his goal
    solve_stack = []

    while frontier:  # while frontier is not empty
        node = frontier.pop(0)  # pop the first node on the frontier
        # if this node is the goal state
        if node.content == problem.define_goal(state):
            # append all the nodes parents while it's not the root node
            solve_stack.append(node)  
            while node.parent != None and node.parent.parent != None:  
                node = node.parent
                solve_stack.append(node)
            # since we found a solution
            print(f'Steps needed: {len(solve_stack)}')
            return solve_stack

        # if the state is not the goal state and we keep history
        if keep_history:
            # if the state is not in the history
            if node.content not in history:
                history.append(node.content)
                if len(history) > history_len:
                    history.pop(0)
                problem.apply_operators(node, frontier)
                
        else:
            problem.apply_operators(node, frontier)

    # if we don't found any soluction
    return []
