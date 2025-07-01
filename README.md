# What the heck?

This project searches for the best [what-the-heck](https://boardgamegeek.com/boardgame/175/what-the-heck)-bot there is.

Game rules can be found [here](https://en.wikipedia.org/wiki/What_the_Heck%3F#Gameplay).

## Participating & Documentation

### Player

When contributing your own `Player`, only the `action` method must be implemented. During one round in the game, each `Player`'s implementation is executed once. It acts as the interface to the game.

```python
from player import Player, PublicPlayerInfo
class YourNamePlayer(Player):
    def action(self, active_value: int, other_players: list[PublicPlayerInfo]) -> int
```

`active_value: int` -> The value of the points currently in play. Might be higher than the highest mouse value (10) in case of a draw in the previous round.

`other_players: list[PublicPlayerInfo]` -> The `PublicPlayerInfo` dataclass offers these fields:

- `cards: list[int]`: List of cards that player can still play this game
- `points: int`: Current amount of points in the game

### Helper methods

Your `Player` superclass comes with helper methods:

- `_highest_card() -> int` and `_lowest_card() -> int`.
- `_highest_but_not_higher_than(value: int) -> int`: Returns `-1` if no card matches the criteria.
- `_lowest_but_not_lower_than(value: int) -> int`: Returns `-1` if no card matches the criteria.

### Example in-built Players

These two are not very smart. It is up to you to beat these clowns:

```python
class RandomPlayer(Player):
    """Plays random moves."""
    def action(self, active_value: int, other_players: list[PublicPlayerInfo]) -> int:
        return random.choice(self._cards)

class StaticPlayer(Player):
    """Always tries to play the same value for a specific card."""
    def action(self, active_value: int, other_players: list[PublicPlayerInfo]) -> int:
        card = self._highest_but_not_higher_than(abs(active_value) + 5)
        return card if card != -1 else self._highest_card()

```

Measure your performance by setting up a game against them.

### Setting up a game

`simulation.py` offers `simulate(games: int, game_class: Game, players: tuple[Player]) -> numpy.array`

- `games: int`: Amount of games to simulate.
- `game_class`: Two options available: `Game` for the normal what-the-heck, `VerboseGame` for console spam. Not recommended with higher game amount.
- `players: tuple[Player]`: Spefify which players participate in the game. No player limit.
- Returns a `numpy.array` with player scores after all `games` have been played.
