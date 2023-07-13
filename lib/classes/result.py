from classes.player import Player
from classes.game import Game


class Result:
    all = []

    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score
        player.results(self)
        player.games_played(game)
        game.results(self)
        game.players(player)
        Result.all.append(self)

    @property
    def player(self):
        return self._player

    @player.setter
    def player(self, player):
        if not isinstance(player, Player):
            raise ValueError("player must be Player class")
        else:
            self._player = player

    @property
    def game(self):
        return self._game

    @game.setter
    def game(self, game):
        if not isinstance(game, Game):
            raise ValueError("player must be Player class")
        else:
            self._game = game

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, score):
        if not isinstance(score, int) or not 1 <= score <= 5000:
            raise ValueError("Score must be integer, between 1-5000")
        else:
            self._score = score
