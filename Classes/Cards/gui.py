import tkinter as tk
from tkinter.font import Font
from Games.Classes.Cards import cards


# Initialise standard variables and display assets onto the frame of the application class
class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master, bg="#111")
        self.master = master
        self.pack()

        # Create a better looking font object
        self.arial16 = Font(family="arial", size=16, weight="bold")
        self.arial14 = Font(family="arial", size=14, weight="bold")
        self.arial10 = Font(family="arial", size=10, weight="bold")

        # Show the labels and the button object on the frame
        self.card = cards.CardDeck()
        self.card_name_label = tk.Label(self, font=self.arial14, fg="#DDD", bg="#111", pady=5)
        self.card_name_label["text"] = "DRAW A RANDOM CARD"
        self.cards_left_label = tk.Label(self, font=self.arial10, fg="#DDD", bg="#111", pady=5)
        self.cards_left_label["text"] = "YOU HAVE {} CARDS LEFT IN THE PACK!".format(self.card.total_cards)
        self.cards_left_label.pack()
        self.card_name_label.pack()
        self.canvas = tk.Canvas(self, width=400, height=600, bd=0, highlightthickness=0, bg="#111")
        self.canvas.pack(pady=10)

        # Create a default image for application startup
        self.img = tk.PhotoImage(self.card.PNG_value)
        self.canvas.create_image(0, 0, anchor="nw", image=self.img)

        # Button options
        self.draw_card = tk.Button(self, font=self.arial16, bg="#225", fg="#DDD")
        self.draw_card["text"] = "DRAW A RANDOM CARD"
        self.draw_card["command"] = self.reveal_card
        self.draw_card.pack(ipadx=80, ipady=20)

    # Update the gui with the card information and new card image
    def reveal_card(self):
        self.card.draw_a_card()
        cond = self.card.card_drawn.split(" ")
        an_or_a = "a"
        if cond[0] == "8" or cond[0] == "ACE":
            an_or_a = "an"
        self.card_name_label["text"] = "You drew {} {}.".format(an_or_a, self.card.card_drawn)
        self.cards_left_label["text"] = "YOU HAVE {} CARDS LEFT IN THE PACK!".format(self.card.total_cards)
        self.img = tk.PhotoImage(file=self.card.get_card_value())
        self.canvas.create_image(0, 0, anchor="nw", image=self.img)