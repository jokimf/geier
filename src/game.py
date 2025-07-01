import random


class Game:
    def __init__(self, players) -> None:
        self.players = players
        self.cards = [-5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        random.shuffle(self.cards)
        self.player_bets = [0] * len(players)
        self.active_value = 0
        self.actv_player_index = -1
        self.ended = False
        self.public_info = None

    def __repr__(self) -> str:
        return f"{self.active_value}|{self.player_bets}|{[p.points for p in self.players]}|{self.cards}"

    def results(self):
        return [p.points for p in self.players]

    def step(self):

        # Check if new card must be drawn.
        if self.actv_player_index == -1:
            self.active_value += self.cards.pop()
            self.actv_player_index += 1

            # Refresh public info only at the start of a new round.
            self.public_info = [p.opponent_info() for p in self.players]

        # Retrieve player action by giving him public info.
        action: int = self.players[self.actv_player_index].action(self.active_value, self.public_info)
        self.players[self.actv_player_index].cards.remove(action) # TODO: check if card played was valid
        self.player_bets[self.actv_player_index] = action

        # Set active player to next in line.
        self.actv_player_index = self.actv_player_index + 1 if len(self.players) - 1 != self.actv_player_index else -1

        # Every player sets a card.
        if self.actv_player_index == -1:
            min_or_max = min if self.active_value < 0 else max
            lowest_or_highest_value = min_or_max(self.player_bets)

            # Check if winner can be determined, if not, the round is a draw.
            if self.player_bets.count(lowest_or_highest_value) == 1:
                winner = self.player_bets.index(lowest_or_highest_value)
                self.players[winner]._points += self.active_value
                self.active_value = 0

        if not self.cards and self.actv_player_index == -1:
            self.ended = True

class VerboseGame(Game):
    def step(self):
        super().step()
        print(self)
        return