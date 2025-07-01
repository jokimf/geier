import numpy

from game import Game, VerboseGame
from player import Player
from players.random_player import RandomPlayer
from players.static_player import StaticPlayer
from players.cheater_player import CheaterPlayer

def simulate(games: int, game_class: Game, players: tuple[Player]) -> numpy.array:
    summed_player_points = numpy.zeros(len(players), dtype=int)

    for _ in range(games):
        game = game_class(players)
        game.cards = [-5,-4,-3,-2,-1,1,2,3,4,5,6,7,8,9,10]
        game.cards.reverse()
        while not game.ended:
            game.step()
        summed_player_points += numpy.array(game.results())
        for p in players:
            p.reset()
    return summed_player_points

print(simulate(10000, Game, (StaticPlayer(), CheaterPlayer())))