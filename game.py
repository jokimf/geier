from player import RandomPlayer
import random

def win_draw_loss(bets:list):
    pass

class Game:
    def __init__(self) -> None:
        self.players = [RandomPlayer(), RandomPlayer(), RandomPlayer()]
        self.cards = [-5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.bets = [0, 0, 0]
        self.active_value = 0
        random.shuffle(self.cards)
        self.active_player_index = -1
        self.ended = False
        #print(f"Game started.")

    def __repr__(self) -> str:
        return str([p for p in self.players])
    
    def results(self):
        return [p.points for p in self.players]

    def step(self) -> float: # TODO: cycle round start player
        if self.active_player_index == -1:
            self.active_value += self.cards.pop()
            #print(f'Next value: {self.active_value}')
            self.active_player_index += 1

        game_state = [self.active_value, self.players]
        action = self.players[self.active_player_index].action(game_state)
        #print(f'{self.active_player_index} bets {action}')
        self.bets[self.active_player_index] = action
        self.active_player_index = self.active_player_index + 1 if len(self.players) -1 != self.active_player_index else -1

        # Every player set a card
        if self.active_player_index == -1:
            min_or_max = min if self.active_value < 0 else max
            lowest_or_highest_value = min_or_max(self.bets)

            # Check if winner can be determined
            if self.bets.count(lowest_or_highest_value) == 1:
                winner = self.bets.index(lowest_or_highest_value)
                #print(f'P{winner} gets: {self.active_value}.')
                self.players[winner].points += self.active_value
                self.active_value = 0

        if not self.cards and self.active_player_index == -1:
            #print(f"Game ended.")
            self.ended = True
