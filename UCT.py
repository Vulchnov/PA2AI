import random
import time
import math
from copy import deepcopy

class Node:
    def __init__(self, move, parent, player):
        self.move = move
        self.parent = parent
        self.player = player
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
        
class UCT:
    def __init__(self, state, player, explore, mode):
        self.root_state = deepcopy(state)
        self.root = Node(None, None, player)
        self.player = player
        self.explore = explore
        self.mode = mode
        self.run_time = 0
        self.node_count = 0
        self.num_rollouts = 0

    def select_node(self)->tuple:
        node = self.root
        state = deepcopy(self.root_state)
        if(self.mode == 2):
                print("wi: " + str(node.Q))
                print("ni: "+ str(node.N))
        
        while len(node.children) != 0:
            children = node.children.values()
            if(self.mode == 2):
                for child in children:
                    print("V"+str(child.move)+ ": " + str(round(child.value(self.explore), 2)))
            max_value = max(children, key=lambda n: n.value(self.explore)).value(self.explore)
            max_nodes = [n for n in children if n.value(self.explore) == max_value]

            node = random.choice(max_nodes)
            if(self.mode == 2):
                print("Move Selected: " + str(node.move))
                print()
            state.insertPiece(node.player, node.move)

            if node.N == 0:
                return node, state
        
        if self.expand(node, state):
            node = random.choice(list(node.children.values()))
            state.insertPiece(node.player, node.move)

        return node, state
    
    def expand(self, parent, state) -> bool:
        if state.gameOver():
            return False
        
        if(self.player=='R'):
            ply = 'Y'
        else:
            ply = 'R'
        children = [Node(move, parent, ply) for move in state.getValidMoves()]
        parent.add_children(children)

        return True
    
    def roll_out(self, state, ply) -> int:
        if ply == 'R':
            opPly = 'Y'
        else:
            opPly = 'R'
        while not state.gameOver():
            moved = random.choice(state.getValidMoves())
            if(self.mode == 2):
                print("Move Selected: "+ str(moved))
            state.insertPiece(ply, moved)
            if state.gameOver():
                break
            moved = random.choice(state.getValidMoves())
            if(self.mode == 2):
                print("Move Selected: "+ str(moved))
            state.insertPiece(opPly, moved)

        if(self.mode == 2):
            print("TERMINAL NODE VALUE "+ str(state.getWinner()))
            print()
        return state
    
    def back_propagate(self, node, turn, outcome):
        reward = 0 if outcome.getWinner() == turn else 1
        if(self.mode == 2):
            print("Updated Values:")
            print("wi " + str(reward))
            print("ni 1")
            print()

        while node is not None:
            node.N +=1
            node.Q += reward
            if(self.mode == 2):
                print("Updated Values:")
                print("wi "+ str(node.N))
                print("ni "+ str(node.Q))
                print()
            node = node.parent
            if outcome.isDraw():
                reward = 0
            else:
                reward = 1-reward

    def search(self, time_limit: int):
        start_time = time.process_time()

        num_rollouts = 0
        while time.process_time()-start_time<time_limit:
            node, state = self.select_node()
            outcome = self.roll_out(state, node.player)
            if(node.player == 'R'):
                ply = 1
            else:
                ply = -1
            self.back_propagate(node, ply, outcome)
            num_rollouts +=1

        run_time = time.process_time()-start_time
        self.run_time=run_time
        self.num_rollouts=num_rollouts
        if(self.mode > 0):
            for child in self.root.children.values():
                print("Column " + str(child.move+1) + ": " + str(round(child.Q/child.N, 2)))

    def best_move(self):
        if self.root_state.gameOver():
            return -1
        
        max_value = max(self.root.children.values(), key=lambda n: n.N).N
        max_nodes = [n for n in self.root.children.values() if n.N ==max_value]
        best_child = random.choice(max_nodes)

        if(self.mode < 0):
            print("FINAL Move selectd "+ str(best_child.move))
        return best_child.move
    
    def move(self, move):
        if move in self.root.children:
            self.root_state.move(move)
            self.root = self.root.children[move]
            return
        
        self.root_state.move(move)
        self.root = Node(None, None, self.root.player)

    