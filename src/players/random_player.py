from player import Player, PublicPlayerInfo
import random

class RandomPlayer(Player):
    """Plays random moves."""
    def action(self, active_value: int, other_players: list[PublicPlayerInfo]) -> int:
        return random.choice(self._cards)