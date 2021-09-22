from View.View import View
from Model.Carte import Carte
from Model.Colors import BLUE_BACKGROUND
from Model.Joueur import Joueur


class Controller:
    def __init__(self):
        self.fen = View()
        self.deck = Carte()

        self.J1 = Joueur()
        self.J1.paquet_carte = self.deck.paquet_1

        self.J2 = Joueur()
        self.J2.paquet_carte = self.deck.paquet_2

        # self.home_page()
        #
        # self.fen.fen.mainloop()

    # def home_page(self):
    #     self.fen.home(BLUE_BACKGROUND)

    def game(self):
        while self.J1.nombre_de_carte != 0 and self.J2.nombre_de_carte != 0:
            print(f"Carte du J1 : {self.J1.retourner_sa_carte()}")
            print(f"Carte du J2 : {self.J2.retourner_sa_carte()}")

            if self.deck.comparaison_carte(self.J1.paquet_carte[0], self.J2.paquet_carte[0]):
                # J1 gagne
                self.J1.victoire_manche(self.J1.paquet_carte[0], self.J2.paquet_carte[0])
                print("Victoire J1")

            else:
                # J2 gagne
                self.J2.victoire_manche(self.J2.paquet_carte[0], self.J1.paquet_carte[0])
                print("Victoire J2")

            self.J1.retirer_carte_manche()
            self.J2.retirer_carte_manche()

            if self.J1.paquet_vide():
                self.J1.switch_paquet()

            if self.J2.paquet_vide():
                self.J2.switch_paquet()

            # Verifier le gagnant ^^
            self.J1.acutaliser_nbre_carte()
            self.J2.acutaliser_nbre_carte()

        if self.J1.nombre_de_carte == 0:
            print("J1 lose")

        else:
            print("J2 lose")


