class Player(object):
    def __init__(self, num):
        super().__init__()
        self.num = num
        self.name = ""
        self.faction = None
        self.colour = ""
        self.score = 0
        self.strat_card = 0
        self.passed = False
        self.card_used = False
        self.is_turn = False
