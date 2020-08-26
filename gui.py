import tkinter as tk
from Cards import cards


# Initialise standard variables and display assets onto the frame of the application class
class Application(tk.Frame):
    def __init__(self, master = None):
        super().__init__(master)
        self.master = master
        self.pack()

        # Show the labels and the button object on the frame
        self.draw_a_card()
        self.card = cards.CardDeck()
        self.card_name_label = tk.Label(self)
        self.card_name_label["text"] = "Draw a random card!"
        self.cards_left_label = tk.Label(self)
        self.cards_left_label["text"] = "You have {} cards left!".format(self.card.total_cards)
        self.cards_left_label.pack()
        self.card_name_label.pack()
        self.canvas = tk.Canvas(self.master, width=400, height=600)
        self.canvas.pack()

        # Create a default image for application startup
        self.img = tk.PhotoImage(file="PNG/AS.png")
        self.canvas.create_image(0, 0, anchor="nw", image=self.img)

    # Create a button object for revealing cards
    def draw_a_card(self):
        self.draw_card = tk.Button(self)
        self.draw_card["text"] = "Draw a random card"
        self.draw_card["command"] = self.reveal_card
        self.draw_card.pack()

    # Update the gui with the card information and new card image
    def reveal_card(self):
        self.card.draw_a_card()
        self.card_name_label["text"] = self.card.card_drawn
        self.cards_left_label["text"] = "You have {} cards left!".format(self.card.total_cards)
        self.img = tk.PhotoImage(file=self.card.get_card_value())
        self.canvas.create_image(0, 0, anchor="nw", image=self.img)
