from random import randint


class Propety:

    def __init__(self, id, name=None):
        self.id = id
        self.name = name
        self.rent = randint(10, 60)
        self.price = randint(40, 100)
        self.owner = None

    def __str__(self):
        return f'owner:{self.owner} - name: {self.name} - rent:{self.rent} - price:{self.price}'

    def __repr__(self):
        return f'owner:{self.owner} - name: {self.name} - rent:{self.rent} - price:{self.price}'
