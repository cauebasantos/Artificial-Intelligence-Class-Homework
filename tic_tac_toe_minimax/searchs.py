""" Searchs Algorithms
"""

from node import Node
from problem import Problem

def search_solution(state: list, problem: Problem, threshold=1000, \
interactive=False, history_len=100) -> list:
    """ Return a sequence of actions that leads to the goal state
    """
    # keep up a history of most recent states viseted
    history = []
    # create the root node with the current state
    root = Node(state, 'None', None)
    frontier = [root]  # create the frontier stack and append the root to it
    # holds the stack sequence of actions the agent is going to do to
    # achieve his goal
    solve_stack = []

    while frontier:  # while frontier is not empty
        node = frontier.pop(-1)  # pop the last node on the frontier

        # if this node is the goal state
        if node.content == problem.define_goal(state):
            # append all the nodes parents while it's not the root node
            solve_stack.append(node)
            while node.parent is not None and node.parent.parent is not None:
                node = node.parent
                solve_stack.append(node)
            # since we found a solution
            print(f'Steps needed: {len(solve_stack)}')
            return solve_stack

        # if we've crossed the threshold and there is any node on the frontier
        if node.depth >= threshold and frontier:
            continue

        # if the state is not the goal state
        if node.content not in history:
            problem.apply_operators(node, frontier)
            history.append(node.content)
            if len(history) > history_len:
                history.pop(0)

        # if we are doing a interactive search
        if interactive and not frontier:
            print(f'No answer was found on a node of depth less than ' \
            f'{threshold}, We are gonna keep looking')
            frontier = [root]
            threshold += 2
            history.clear()
            continue
        elif not interactive and not frontier:
            print(f'No answer was found on a node of depth less than \
            {threshold}')
            return []

    # if we don't found any soluction
    return []

def sort_node(node: Node) -> int:
    return node.score

def minimax(problem: Problem, node: Node, player = 0) -> Node:
    (is_game_over, final_state) = problem.is_game_over(node)
    if is_game_over:
        return final_state
    
    moves = problem.possible_moves(node, player)
    for move in moves:
        next_player = (player + 1) % 2
        move.score = minimax(problem, move, next_player).score
    
    best_moves = sorted(moves, key = lambda n: n.score, reverse = True)

    if player == 0: # me
        return best_moves[0] # get the best move for myself
    else:   # the adversary
        return best_moves[-1] # get the worst move for me
