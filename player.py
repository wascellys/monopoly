from random import randint

PERFIS = {
    1: 'impulsivo',
    2: 'exigente',
    3: 'cauteloso',
    4: 'aleatorio'
}


class Player():

    def __init__(
            self, profile: int, position=0,
    ):
        self.id = profile
        self.position = position
        self.money = 300
        self.profile = PERFIS[profile]

    def __str__(self):
        return f' id:{self.id}  - profile:{self.profile} - money: {self.money} - position: {self.position}'

    def __repr__(self):
        return f' id:{self.id}  - profile:{self.profile} - money: {self.money} - position: {self.position}'

    def pay_rent(self, propety, board):
        owner = None
        if propety.owner:
            self.money -= propety.rent
            for player in board.players:
                if player.id == propety.owner:
                    owner = player
            owner.money += propety.rent
        if self.money < 0:
            board.remove_player(self)

    def buy_property(self, propety, board, injected_value=None):
        buy = False
        if self.profile == PERFIS[1]:
            buy = True
        if self.profile == PERFIS[2]:
            if propety.rent > 50:
                buy = True
        if self.profile == PERFIS[3]:
            if self.money - propety.price >= 80:
                buy = True
        if self.profile == PERFIS[4]:
            if injected_value or randint(0, 1) == 1:
                buy = True

        if buy:
            self.money -= propety.price
            propety.owner = self.id

        if self.money < 0:
            board.remove_player(self)
