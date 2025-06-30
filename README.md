# What the heck?
This project searches for the best [what-the-heck](https://boardgamegeek.com/boardgame/175/what-the-heck)-bot there is. 

Game rules can be found [here](https://en.wikipedia.org/wiki/What_the_Heck%3F#Gameplay).
## Participating & Documentation
### Player
When contributing your own `Player`, only the `action` method must be implemented. During one round in the game, each `Player`'s implementation is executed once. It acts as the interface to the game.
```python
class YourNamePlayer(Player):
    def action(self, active_value: int, other_players: list[Player]) -> int
```

`active_value: int` -> The value of the points currently in play. Might be higher than the highest mouse value (10) in case of a draw in the previous round.

`other_players: list[Player]` -> The player interface offers these self-explanatory methods:
- `cards() -> list[int]`: List of cards that player can still play this game
- `points() -> int`: Current amount of points in the  game
- `identity() -> int`: ID to identify your opponent at any stage  in the game

### Helper methods
Your `Player` superclass comes with helper methods:
- `_highest_card() -> int` and `_lowest_card() -> int`
- `_highest_but_not_higher_than(value: int) -> int`: Returns `-1` if no card matches the criteria.
- `_lowest_but_not_lower_than(value: int) -> int`: Returns `-1` if no card matches the criteria.


### Example in-built Players
These two aren't very smart. It's up to you to beat these clowns:
```python 
class RandomPlayer(Player):
    def action(self, active_value: int, other_players: list[Player]) -> int:
        return random.choice(self._cards)

class StaticPlayer(Player):
    def action(self, active_value: int, other_players: list[Player]) -> int:
        main_card = self._highest_but_not_higher_than(active_value + 5)
        return main_card if main_card != -1 else self._highest_card()

```

Measure your performance against them by setting up a game with them.
```python

from game import Game
from player import RandomPlayer, StaticPlayer

players = [StaticPlayer(), RandomPlayer(), RandomPlayer(), RandomPlayer()]
game = Game(players)
while not game.ended:
    game.step()
print(game.results())
```
Why not put it in a while loop and save the score to see how they match up long-term? Go wild...