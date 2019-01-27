""" Node class
"""

class Node:
    def __init__(self, content, action, parent, path_cost=0, depth=0, 
    heuristic=0, cost_with_heuristic=0):
        self.content = content
        self.action = action
        self.parent = parent
        self.path_cost = path_cost
        self.depth = depth
        self.heuristic = heuristic
        self.cost_with_heuristic = cost_with_heuristic

    def __repr__(self):
        return f'<Node Object> state: {self.content}, action: {self.action}, \
        path_cost: {self.path_cost}, depth: {self.depth}, astar={self.cost_with_heuristic}'

