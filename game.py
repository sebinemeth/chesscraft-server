class Game:
    def __init__(self):
        self.players = []
        self.status = False
        self.state = ""  # some default state
        self.round_of = 0

    def add_player(self, p):
        self.players.append(p)
        if len(self.players) == 2:
            self.start()

    def start(self):
        self.status = True

    def next_round(self):
        self.round_of = 1 - self.round_of
