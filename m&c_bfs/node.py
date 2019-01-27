""" Node class
"""

class Node:
    """ Node class for AI search algorithms
    """
    def __init__(self, content, action, parent, path_cost=0, depth=0):
        self.content = content
        self.action = action
        self.parent = parent
        self.path_cost = path_cost
        self.depth = depth


    def __repr__(self):
        return f'<Node Object> state: {self.content}, action: {self.action},' \
            f'path_cost: {self.path_cost}'
