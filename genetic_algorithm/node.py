""" Node class
"""
import math

class Node:
    def __init__(self, chromosome=[]):
        self.chromosome = chromosome
        self.fitness = 0

    def __repr__(self):
        return f'<Node Object> state: {self.chromosome}, score: {self.fitness}\n'
