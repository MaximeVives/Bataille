from random import shuffle


class Carte:
    def __init__(self):
        self.paquet = 4 * [i + 1 for i in range(13)]
        self.melange_carte()

        self.paquet_1 = []
        self.paquet_2 = []
        self.distrib_card()

    def melange_carte(self):
        shuffle(self.paquet)

    def distrib_card(self):
        self.paquet_1 = self.paquet[0:26]
        self.paquet_2 = self.paquet[26:]

    # Ma fonction retourne True si le Joueur 1 gagne Sinon retourne False
    def comparaison_carte(self, c1, c2):
        if c1 != c2:
            return self.action_normal(c1, c2)
        if c1 == c2:
            self.tie()

    def action_normal(self, c1, c2):
        if c1 == 1:
            return True
        elif c2 == 1:
            return False

        elif c1 > c2:
            return True
        else:
            return False

    def tie(self):
        pass