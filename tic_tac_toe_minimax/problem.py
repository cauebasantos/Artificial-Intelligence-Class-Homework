""" Problem Class
"""

from node import Node

class Problem:
    """ Problem Class
    """

    def __init__(self):
         # holds possible actions the agent can do
        self.winning_positions = [[0, 1, 2], [3, 4, 5], [6, 7, 8],
                                  [0, 3, 6], [1, 4, 7], [2, 5, 8],
                                  [0, 4, 8], [6, 4, 2]]

    @staticmethod
    def play(state: list, direction: str) -> list:
        """ Return the state after we apply the operator on the state
        """
        state = state.copy()

        return None

    def is_game_over(self, node: Node)  -> tuple:
        state = node.content
        x_indices = [i for i, e in enumerate(state) if e == "X"]
        o_indices = [i for i, e in enumerate(state) if e == "O"]

        for w_pos in self.winning_positions:
            if all(pos in x_indices for pos in w_pos):
                node.score = 10 # i won
                return (True, node) 
            
            if all(pos in o_indices for pos in w_pos):
                node.score = -10 # i lost
                return (True, node) 

        if len(x_indices) + len(o_indices) == 9:
            node.score = 0 # draw
            return (True, node) 
        
        return (False, node) # game is not over

    def possible_moves(self, node: Node, player: int) -> list:
        """ Return the possible moves
        """

        piece = ''
        if player == 0:
            piece = 'X'
        elif player == 1:
            piece = 'O'

        possibilites = []

        indices = [i for i, e in enumerate(node.content) if e == " "]
        
        for i in indices:
            state = node.content.copy()
            state[i] = piece
            node_content = state
            node_parent = node
            node_score = node.score
            node_depth = node.depth + 1
            new_node = Node(node_content, node_parent, node_score, node_depth)
            possibilites.append(new_node)

        return possibilites