""" Problem Class
"""
import random
import math
from node import Node

class Problem:
    """ Problem Class
    """

    def __init__(self):
         # holds possible actions the agent can do
        self.possible_cities = list(range(10))
        self.distance_table = []

        self.distance_table.append(['0', '30', '84', '56', '-', '-', '-', '75', '-', '80'])
        self.distance_table.append(['30', '0', '65', '-', '-', '-', '70', '-', '-', '40'])
        self.distance_table.append(['84', '65', '0', '74', '52', '55', '-', '60', '143', '48'])
        self.distance_table.append(['56', '-', '74', '0', '135', '-', '-', '20', '-', '-'])
        self.distance_table.append(['-', '-', '52', '135', '0', '70', '-', '122', '98', '80'])
        self.distance_table.append(['70', '-', '55', '-', '70', '0', '63', '-', '82', '35'])
        self.distance_table.append(['-', '70', '-', '-', '-', '63', '0', '-', '120', '57'])
        self.distance_table.append(['75', '-', '135', '20', '122', '-', '-', '0', '-', '-'])
        self.distance_table.append(['-', '-', '143', '-', '98', '82', '120', '-', '0', '-'])
        self.distance_table.append(['80', '40', '48', '-', '80', '35', '57', '-', '-', '0'])


    def start_state(self) -> list:
        array = self.possible_cities.copy()
        random.shuffle(array)

        index = array.index(0)
        array[0], array[index] = array[index], array[0]
        return array


    def evaluate_state(self, state: list) -> int:
        score = 0
        for i in range(len(state) - 1):
            # get the distance from the actual city to it's neighbor
            distance = self.distance_table[state[i]][state[i + 1]]
            if distance == '-':
                score = -math.inf
                return score
            else:
                score += int(distance)
        distance = self.distance_table[state[-1]][state[0]]
        if distance == '-':
            score = math.inf
        else:
            score += int(distance)

        return -score

    def possible_moves(self, state: list) -> list:
        moves = []
        for i in range(1,len(state) - 1):
            state_copy = state.copy()
            state_copy[i], state_copy[i+1] = state_copy[i+1], state_copy[i]
            if self.distance_table[state_copy[i]][state_copy[i-1]] == '-':
                continue
            moves.append(state_copy)

        return moves
    
    def best_move_from_state(self, state: list) -> Node:
        best_move = Node()

        for move in self.possible_moves(state):
            score = self.evaluate_state(move)
            if score > best_move.score:
                best_move.score = score
                best_move.content = move

        return best_move