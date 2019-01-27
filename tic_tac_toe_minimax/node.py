""" Node class
"""

class Node:
    """ Node class for AI search algorithms
    """
    def __init__(self, content, parent=None, score=0, depth=0):
        self.content = content
        self.parent = parent
        self.score = score
        self.depth = depth


    def __repr__(self):
        return f'<Node Object> state: {self.content}, score: {self.score}\n'
