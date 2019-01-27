""" Agent Class
"""

from environment import Environment
from problem import Problem
from searchs import search_solution

class Agent:
    """ Agent class that implements the AI Agent form Draughts Game
    """
    def __init__(self, environment: Environment):
        # holds the environment the agent is going to manipulate
        self.environment = environment
        # holds the stack sequence of actions the agent is going to do to
        # achieve his goal
        self.solve_stack = []

    def do_action(self, problem: Problem):
        """ Performs the agent action, it might be search for a solve sequence
        or execute some state
        """

        state = self.environment.get_state()

        # if we already have a solution
        if self.solve_stack:
            # pop the next step
            node = self.solve_stack.pop(-1)
            # get the operation needed to get to this state
            operation = node.action
            # apply the operator on environment
            self.environment.modify_state(operation)
            # print the current state
            self.environment.print_state()
        else:
            # search for a solution
            self.solve_stack = search_solution(state, problem)
