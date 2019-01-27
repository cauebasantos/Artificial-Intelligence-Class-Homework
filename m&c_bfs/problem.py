""" Problem Class
"""

from node import Node

class Problem:
    """ Problem Class
    """

    def __init__(self):
         # holds possible actions the agent can do
        self.possible_actions = ['M','C','2M','2C', 'MC']

    @staticmethod
    def define_goal(state: list) -> list:
        """ Return the goal state
        """
        return [0,0,1,3,3]

    @staticmethod
    def can_move(state: list, operator: str) -> bool:
        """ Return True only if we can apply a given operator to a given state
        """
        state_copy = state.copy()
        # defines where the boat is (0 is left, 1 is right)
        boat_side = state_copy[2]
        # a variable that makes the calculus works for the boat in both sides
        boat_side_op = boat_side * 3

        if operator == 'M':
            if state_copy[0 + boat_side_op] < 1:
                return False
        elif operator == 'C':
            if state_copy[1 + boat_side_op] < 1:
                return False
        elif operator == '2M':
            if state_copy[0 + boat_side_op] < 2:
                return False
        elif operator == '2C':
            if state_copy[1 + boat_side_op] < 2:
                return False
        elif operator == 'MC':
            if state_copy[0 + boat_side_op] < 1 or state_copy[1 + boat_side_op] < 1:
                return False
        # if there will be more cannibals then missionaries
        if (state_copy[0] < state_copy[1] and state_copy[0] != 0) or \
        (state_copy[3] < state_copy[4] and state_copy[3] != 0):
            return False
            
        # otherwise the move is valid
        return True

    @staticmethod
    def move_boat(state: list, operator: str) -> list:
        """ Return the state after we apply the operator on the state
        """
        state_copy = state.copy()
        # defines where the boat is (0 is left, 1 is right)
        boat_side = state_copy[2]
        # a variable that makes the calculus works for the boat in both sides
        boat_side_op = boat_side * 3
        complement = 3 - boat_side_op

        if Problem.can_move(state_copy, operator):
            if operator == 'M':
                state_copy[0 + boat_side_op] -= 1
                state_copy[0 + complement] += 1
            elif operator == 'C':
                state_copy[1 + boat_side_op] -= 1
                state_copy[1 + complement] += 1
            elif operator == '2M':
                state_copy[0 + boat_side_op] -= 2
                state_copy[0 + complement] += 2
            elif operator == '2C':
                state_copy[1 + boat_side_op] -= 2
                state_copy[1 + complement] += 2               
            elif operator == 'MC':
                state_copy[0 + boat_side_op] -= 1
                state_copy[1 + boat_side_op] -= 1
                state_copy[0 + complement] += 1
                state_copy[1 + complement] += 1
                
            state_copy[2] = (state_copy[2] + 1)%2

            return state_copy

        return None

    def apply_operators(self, node: Node, frontier: list):
        """ Try to apply all the operators on the actual state and push them
        into the frontier
        """
        for action in self.possible_actions:
            if Problem.can_move(node.content, action):
                node_content = Problem.move_boat(node.content, action)
                node_parent = node
                node_path_cost = node.path_cost + 1
                node_action = action
                node_depth = node.depth + 1
                if node_content is not None:
                    new_node = Node(node_content, node_action, node_parent, \
                        node_path_cost, node_depth)
                    frontier.append(new_node)

"""
@staticmethod
    def can_move(state: list, operator: str) -> bool:

        state_copy = state.copy()
        # defines where the boat is (0 is left, 1 is right)
        boat_side = state_copy[2]

        if boat_side == 0:
            if operator == 'M':
                if state_copy[0] < 1:
                    return False
            elif operator == 'C':
                if state_copy[1] < 1:
                    return False
            elif operator == '2M':
                if state_copy[0] < 2:
                    return False
            elif operator == '2C':
                if state_copy[1] < 2:
                    return False
            elif operator == 'MC':
                if state_copy[0] < 1 or state_copy[1] < 1:
                    return False
        else:
            if operator == 'M':
                if state_copy[3] < 1:
                    return False
            elif operator == 'C':
                if state_copy[4] < 1:
                    return False
            elif operator == '2M':
                if state_copy[3] < 2:
                    return False
            elif operator == '2C':
                if state_copy[4] < 2:
                    return False
            elif operator == 'MC':
                if state_copy[3] < 1 or state_copy[4] < 1:
                    return False
        # if there will be more cannibals then missionaries
        if state_copy[0] < state_copy[1] or state_copy[3] < state_copy[4]:
            return False
            
        # otherwise the move is valid
        return True

    @staticmethod
    def move_boat(state: list, operator: str) -> list:
        
        state_copy = state.copy()
        # defines where the boat is (0 is left, 1 is right)
        boat_side = state_copy[2]

        if Problem.can_move(state_copy, operator):
            if boat_side == 0:
                if operator == 'M':
                    state_copy[0] -= 1
                    state_copy[3] += 1
                elif operator == 'C':
                    state_copy[1] -= 1
                    state_copy[4] += 1
                elif operator == '2M':
                    state_copy[0] -= 2
                    state_copy[3] += 2
                elif operator == '2C':
                    state_copy[1] -= 2
                    state_copy[4] += 2
                elif operator == 'MC':
                    state_copy[0] -= 1
                    state_copy[1] -= 1
                    state_copy[3] += 1
                    state_copy[4] += 1

                state_copy[2] = 1
            else:
                if operator == 'M':
                    state_copy[3] -= 1
                    state_copy[0] += 1
                elif operator == 'C':
                    state_copy[4] -= 1
                    state_copy[1] += 1
                elif operator == '2M':
                    state_copy[3] -= 2
                    state_copy[0] += 2
                elif operator == '2C':
                    state_copy[4] -= 2
                    state_copy[1] += 2
                elif operator == 'MC':
                    state_copy[3] -= 1
                    state_copy[4] -= 1
                    state_copy[0] += 1
                    state_copy[1] += 1
                
                state_copy[2] = 0

            return state_copy

        return None

"""