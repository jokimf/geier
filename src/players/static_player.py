from player import Player, PublicPlayerInfo

class StaticPlayer(Player):
    """Always tries to play the same value for a specific card."""
    def action(self, active_value: int, other_players: list[PublicPlayerInfo]) -> int:
        card = self._highest_but_not_higher_than(abs(active_value) + 5)
        return card if card != -1 else self._highest_card()