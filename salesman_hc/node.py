""" Node class
"""
import math

class Node:
    def __init__(self, content=[], score=-math.inf):
        self.content = content
        self.score = score

    def __repr__(self):
        return f'<Node Object> state: {self.content}, score: {-self.score}'

