""" Problem Class
"""

from node import Node

class Problem:
    """ Problem Class
    """

    def __init__(self, goal: int):
         # holds possible actions the agent can do
        self.possible_actions = list(range(14))
        self.goal = goal - 1
        # the next two tables I get from 
        # https://github.com/cgdesousaf/metro-problem/blob/master/problem2/graph.cpp
        # I already had the idea how to do it , but I was feeling lazy '-'

        self.heuristic_table = []
        self.heuristic_table.append([0, 11, 20, 27, 40, 43, 39, 28, 18, 10, 18, 30, 30, 32])
        self.heuristic_table.append([11, 0, 9, 16, 29, 32, 28, 19, 11, 4, 17, 23, 21, 24])
        self.heuristic_table.append([20, 9, 0, 7, 20, 22, 19, 15, 10, 11, 21, 21, 13, 18])
        self.heuristic_table.append([27, 16, 7, 0, 13, 16, 12, 13, 13, 18, 26, 21, 11, 17])
        self.heuristic_table.append([40, 29, 20, 13, 0, 3, 2, 21, 25, 31, 38, 27, 16, 20])
        self.heuristic_table.append([43, 32, 22, 16, 3, 0, 4, 23, 28, 33, 41, 30, 17, 20])
        self.heuristic_table.append([39, 28, 19, 12, 2, 4, 0, 22, 25, 29, 38, 28, 13, 17])
        self.heuristic_table.append([28, 19, 15, 13, 21, 23, 22, 0, 9, 22, 18, 7, 25, 30])
        self.heuristic_table.append([18, 11, 10, 13, 25, 28, 25, 9, 0, 13, 12, 12, 23, 28])
        self.heuristic_table.append([10, 4, 11, 18, 31, 33, 29, 22, 13, 0, 20, 27, 20, 23])
        self.heuristic_table.append([18, 17, 21, 26, 38, 41, 28, 18, 12, 20, 0, 15, 35, 39])
        self.heuristic_table.append([30, 23, 21, 21, 27, 30, 28, 7, 12, 27, 15, 0, 31, 37])
        self.heuristic_table.append([30, 21, 13, 11, 16, 17, 13, 25, 23, 20, 35, 31, 0, 5])
        self.heuristic_table.append([32, 24, 18, 17, 20, 20, 17, 30, 28, 23, 39, 37, 5, 0])


        self.connection_table = []
        self.connection_table.append([0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        self.connection_table.append([1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0])
        self.connection_table.append([0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0])
        self.connection_table.append([0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0])
        self.connection_table.append([0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0])
        self.connection_table.append([0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        self.connection_table.append([0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        self.connection_table.append([0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0])
        self.connection_table.append([0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0])
        self.connection_table.append([0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        self.connection_table.append([0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0])
        self.connection_table.append([0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0])
        self.connection_table.append([0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1])
        self.connection_table.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0])

    def define_goal(self, state: int) -> list:
        """ Return the goal state
        """
        return self.goal

    def apply_operators(self, node:Node, frontier:list):
        for action in self.possible_actions:
            if 0 <= node.content <= 13 and self.connection_table[node.content][action] == 1:
                node_content = action
                node_parent = node
                node_path_cost = node.path_cost + 1
                node_action = action
                node_depth = node.depth + 1
                if node_content != None:
                    new_node = Node(node_content, node_action, node_parent, 
                        node_path_cost, node_depth)
                    
                    new_node.cost_with_heuristic = self.calculate_astar(new_node)
                    frontier.insert(new_node, new_node.cost_with_heuristic)


    def calculate_heuristic(self, node:Node):
        state = node.content
        goal = self.define_goal(state)
        
        return self.heuristic_table[state][goal]

    def calculate_astar(self, node:Node):
        return node.path_cost + \
        self.calculate_heuristic(node)