from tkinter import *
from Model.Colors import BLUE_BACKGROUND


class View:
    def __init__(self):
        self.fen = Tk()
        self.fen.config(bg="White")
        self.fen.minsize(width=1000, height=700)
        self.fen.title("Bataille")
        self.fen.resizable(False, False)

    @staticmethod
    def update_card():
        print("Carte")

    def home(self, bg_color):
        self.fen.config(bg=bg_color)

        grid = Frame(self.fen)
        grid.grid(sticky="news", column=0, row=2, columnspan=2)
        self.fen.rowconfigure(5, weight=1)
        self.fen.columnconfigure(0, weight=1)

        title = Label(self.fen, bg=bg_color, fg="White", bd=0, text="Bataille", font=("Arial", 24, "bold")).grid(column=0, row=0)
        choice = Label(self.fen, bg=bg_color, fg="#dfdfdf", bd=0, text="Que souhaitez-vous faire ?", font=("Arial", 14, "normal")).grid(column=0, row=1)
