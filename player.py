import random
from abc import ABC

class Player(ABC):
    def __init__(self) -> None:
        self.cards = [x for x in range(1, 16)]
        self.points = 0
    
    def __repr__(self) -> str:
        return f'P:{self.points}'
    
    def action(self, game_state):
        raise NotImplementedError

class RandomPlayer(Player):
    def action(self, game_state) -> int:
        return random.choice(self.cards)
