import tkinter as tk
from tkinter.font import Font
from Games.Classes.Cards import gui


# Borrowing a few assets from the Cards gui, i may optimise the class inheritance later on, but not now
class Options(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master, bg="#FFF")
        self.master = master
        self.pack(ipadx=100, ipady=80)

        self.arial16 = Font(family="arial", size=16, weight="bold")
        self.title = tk.Label(self, font=self.arial16, bg="#FFF")
        self.title["text"] = "SELECT AN OPTION"
        self.title.pack(ipady=10)

        self.card_option = tk.Button(self, font=self.arial16, bg="#225", fg="#DDD")
        self.card_option["text"] = "RANDOM CARD GENERATOR"
        self.card_option["command"] = self.open_game
        self.card_option.pack(ipadx=20, ipady=5)

    def open_game(self):
        self.destroy()
        card_game = gui.Application(self.master)



