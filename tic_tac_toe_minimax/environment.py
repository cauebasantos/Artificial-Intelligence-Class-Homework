""" Environment Class
"""

from problem import Problem

class Environment:
    """ Environment class
    """

    def __init__(self, state: list):
        self.state = state

    def get_state(self):
        """ Return the actual state
        """
        return self.state

    def modify_state(self, state: list):
        """ Set the actual state by applying one operator
        """
        self.state = state

    def __repr__(self):
        g = self.state
        return  f'{g[0]} | {g[1]} | {g[2]}\n' \
                f'---------\n' \
                f'{g[3]} | {g[4]} | {g[5]}\n' \
                f'---------\n' \
                f'{g[6]} | {g[7]} | {g[8]}\n'
