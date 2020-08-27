import tkinter as tk
from tkinter.font import Font
from Games.Classes.Cards import card_gui
from Games.Classes.View import view_gui


# This is a class which extends to all of the children classes
class Options(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master, bg="#000")
        self.master = master
        self.master.resizable(False, False)
        self.master.size()
        self.grid()

        self.arial16 = Font(family="arial", size=16, weight="bold")
        self.title = tk.Label(self, font=self.arial16, bg="#FFF")
        self.title["text"] = "SELECT AN OPTION"
        self.title.grid(row=0, sticky="news", ipadx=100, ipady=20)

        # The list of buttons which create the new classes
        self.card_option = tk.Button(self, font=self.arial16, bg="#225", fg="#DDD")
        self.card_option["text"] = "RANDOM CARD GENERATOR"
        self.card_option["command"] = self.open_card_game
        self.card_option.grid(row=1, sticky="news", ipady=10)

        self.view_option = tk.Button(self, font=self.arial16, bg="#522", fg="#DDD")
        self.view_option["text"] = "IMAGE GALLERY"
        self.view_option["command"] = self.image_gallery
        self.view_option.grid(row=2, sticky="news", ipady=10)

    # Open the card guessing game
    def open_card_game(self):
        self.destroy()
        card_game = card_gui.Application(self.master)
        self.master.title("RANDOM CARD GENERATOR")

    def image_gallery(self):
        self.destroy()
        beautiful = view_gui.TheView(self.master)
        self.master.title("Image Gallery")




