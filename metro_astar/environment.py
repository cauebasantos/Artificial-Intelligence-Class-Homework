""" Environment Class
"""

from problem import Problem

class Environment:
    """ Environment class
    """

    def __init__(self, state):
        self.state = state - 1

    def get_state(self):
        """ Return the actual state
        """
        return self.state

    def modify_state(self, direction: int):
        """ Set the actual state by applying one operator
        """
        self.state = direction

    def print_state(self):
        """ Prints the actual state
        """
        print(f'E{self.state + 1}')