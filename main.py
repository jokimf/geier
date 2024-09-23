import numpy
from game import Game

total_scores = numpy.array([0,0,0])
for _ in range(1000):
    game = Game()
    while not game.ended:
        game.step()
    total_scores += numpy.array(game.results())

print(total_scores)