import numpy

from game import Game
from player import RandomPlayer

players = [RandomPlayer(), RandomPlayer(), RandomPlayer(), RandomPlayer()]
summed_player_points = numpy.zeros(len(players), dtype=int)

for _ in range(10000):
    game = Game(players)
    while not game.ended:
        game.step()
    # Total game points by all players do not always amount to 40, because there might be a tie in the last round.
    summed_player_points += numpy.array(game.results())

print(summed_player_points)
