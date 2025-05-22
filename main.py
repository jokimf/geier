import numpy
from game import Game

summed_player_points = numpy.array([0, 0, 0])
for _ in range(1000):
    game = Game()
    while not game.ended:
        game.step()
    summed_player_points += numpy.array(game.results())

print(summed_player_points)