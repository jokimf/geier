from player import Player, PublicPlayerInfo

class CheaterPlayer(Player):
    """Plays random moves."""
    def action(self, active_value: int, other_players: list[PublicPlayerInfo]) -> int:
        return 15