from random import randint
from faker import Faker

from player import Player
from propety import Propety

fake = Faker('pt_BR')


class Board:

    def __init__(self):
        self.champion = None
        self.rotation = 0
        self.players = []
        self.propeties = [
            Propety(index, name=fake.address(), )
            for index in range(int(20))
        ]

    def __str__(self):
        return f'''        
        Champion:{self.champion.profile}
        Rotation:{self.rotation if self.rotation < 1000 else 1000} 
        Money of champion: R$ {self.champion.money}
        '''

    def run(self, player: Player):
        if player.money < 0:
            self.remove_player(player)
            return

        propety = self.propeties[self.walk_player(player)]

        if propety.owner and propety.owner != player.id:
            return player.pay_rent(propety, self)

        if propety.owner is None:
            return player.buy_property(propety, board=self)

    def walk_player(self, player: Player) -> int:
        walk = player.position + randint(1, 6)
        if walk >= 20:
            player.money += float(100)
            walk -= 20
        player.position = walk
        return walk

    def remove_player(self, player: Player):
        for propety in self.propeties:
            if propety.owner == player.id:
                propety.owner = None
        self.players.remove(player)

    def player_max_money(self) -> Player:
        max = 0
        champion = None
        for player in self.players:
            if player.money > max:
                max = player.money
                champion = player

        return champion
