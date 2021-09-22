class Joueur:
    def __init__(self):
        self.paquet_carte = []
        self.paquet_carte_gagnee = []
        self.nombre_de_carte = 26

    def paquet_vide(self):
        return len(self.paquet_carte) == 0

    def switch_paquet(self):
        self.paquet_carte = self.paquet_carte_gagnee
        self.paquet_carte_gagnee = []

    def acutaliser_nbre_carte(self):
        self.nombre_de_carte = len(self.paquet_carte) + len(self.paquet_carte_gagnee)

    def retourner_sa_carte(self):
        return self.paquet_carte[0]

    def victoire_manche(self, c1, c2):
        self.paquet_carte_gagnee.append(c1)
        self.paquet_carte_gagnee.append(c2)

    def retirer_carte_manche(self):
        self.paquet_carte.pop(0)
