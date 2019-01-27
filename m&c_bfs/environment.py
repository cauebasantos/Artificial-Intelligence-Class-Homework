""" Environment Class
"""

from problem import Problem

class Environment:
    """ Environment class
    """

    def __init__(self, state):
        self.state = state

    def get_state(self):
        """ Return the actual state
        """
        return self.state

    def modify_state(self, direction: str):
        """ Set the actual state by applying one operator
        """
        self.state = Problem.move_boat(self.state, direction)

    def print_state(self):
        """ Prints the actual state
        """
        print(f"{self.state[0]}M, {self.state[1]}C ____ " \
            f"{self.state[3]}M, {self.state[4]}C")
