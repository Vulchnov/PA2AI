import random
import time
import math
from copy import deepcopy

class Node:
    def __init__(self, move, parent):
        self.move = move
        self.parent = parent
        self.N = 0
        self.Q = 0
        self.children = {}

    def add_children(self, children: dict) -> None:
        for child in children:
            self.children[child.move] = child
    
    def value(self, explore):
        if self.N==  0:
            return 0 if explore == 0 else math.inf
        else:
            return self.Q/self.N + explore * math.sqrt(math.log(self.parent.N)/self.N)
        
class MCTS:
    def __init__(self, state):
        self.root_state = deepcopy(state)
        self.root = Node(None, None)
        self.run_time = 0
        self.node_count = 0
        self.num_rollouts = 0

    def select_node(self)->tuple:
        node = self.root
        state = deepcopy(self.root_state)
        
        while len(node.children) != 0:
            children = node.children.values()
            max_value = max(children, key=lambda n: n.value()).value()
            max_nodes = [n for n in children if n.value() == max_value]

            node = random.choice(max_nodes)
            state.move(node.move)

            if node.N == 0:
                return node, state
        
        if self.expand(node, state):
            node = random.choice(list(node.children.values()))
            state.move(node.move)

        return node, state
    
    def expand(self, parent, state) -> bool:
        if state.isDraw() or state.getWinner() != 0:
            return False
        
        children = [Node(move, parent) for move in state]