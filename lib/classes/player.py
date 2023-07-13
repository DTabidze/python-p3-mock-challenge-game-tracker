class Player:
    all = []

    def __init__(self, username):
        self.username = username
        self._results = []
        self._games_played = []

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        if isinstance(username, str) and 2 <= len(username) <= 16:
            self._username = username
        else:
            raise ValueError("Username must be 2-16 len and String!")

    def results(self, new_result=None):
        from classes.result import Result

        if isinstance(new_result, Result):
            self._results.append(new_result)
        return self._results

    def games_played(self, new_game=None):
        from classes.game import Game

        if isinstance(new_game, Game):
            self._games_played.append(new_game)
        return self._games_played

    def played_game(self, game):
        if game in self._games_played:
            return True
        else:
            return False

    def num_times_played(self, game):
        return self._games_played.count(game)

    @classmethod
    def highest_scored(cls, game):
        max_result = 0
        max_player = None
        for player in game.players():
            if player.average_score(game) >= max_result:
                max_player = player
                max_result = player.average_score(game)
        return max_player
