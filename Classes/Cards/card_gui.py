import tkinter as tk
from Classes.Cards import cards
from Classes.Home import return_home_button


# Initialise standard variables and display assets onto the frame of the application class
class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master, bg="#111")
        self.master.resizable(False, False)
        self.master = master
        self.grid()

        # Create a better looking font object
        self.arial16 = Font(family="arial", size=16, weight="bold")
        self.arial14 = Font(family="arial", size=14, weight="bold")
        self.arial10 = Font(family="arial", size=10, weight="bold")

        # Allows the user to return back to the home directory
        self.back = return_home_button.ReturnHome(self, self.master)
        self.back.return_button.grid(row=0, sticky="news")

        # Show the labels and the button object on the frame
        self.card = cards.CardDeck()
        self.card_name_label = tk.Label(self, font=self.arial14, fg="#DDD", bg="#111", pady=5)
        self.card_name_label["text"] = "DRAW A RANDOM CARD"
        self.cards_left_label = tk.Label(self, font=self.arial10, fg="#DDD", bg="#111", pady=5)
        self.cards_left_label["text"] = "YOU HAVE {} CARDS LEFT IN THE PACK!".format(self.card.total_cards)
        self.cards_left_label.grid(row=1, sticky="news")
        self.card_name_label.grid(row=2, sticky="news")
        self.img = tk.PhotoImage(file=self.card.PNG_value)
        self.canvas = tk.Canvas(self, width=400, height=600, bd=0, highlightthickness=0, bg="#111")
        self.draw_card = tk.Button(self, font=self.arial16, bg="#225", fg="#DDD")
        self.reshuffle = tk.Button(self, font=self.arial16, bg="#225", fg="#DDD")
        self.create_canvas()

    def create_canvas(self):
        # Create a default image for application startup
        self.canvas = tk.Canvas(self, width=400, height=600, bd=0, highlightthickness=0, bg="#111")
        self.canvas.create_image(0, 0, anchor="nw", image=self.img)
        self.canvas.grid(pady=10, row=3, sticky="news")

        # Button options
        self.draw_card = tk.Button(self, font=self.arial16, bg="#225", fg="#DDD")
        self.draw_card["text"] = "DRAW A RANDOM CARD"
        self.draw_card["command"] = self.reveal_card
        self.draw_card.grid(row=4, sticky="news", ipady=20)

    # Update the gui with the card information and new card image
    def reveal_card(self):
        if self.card.total_cards > 0:
            self.card.draw_a_card()
            cond = self.card.card_drawn.split(" ")
            an_or_a = "a"
            if cond[0] == "8" or cond[0] == "ACE":
                an_or_a = "an"
            self.card_name_label["text"] = "You drew {} {}.".format(an_or_a, self.card.card_drawn)
            self.cards_left_label["text"] = "YOU HAVE {} CARDS LEFT IN THE grid!".format(self.card.total_cards)
            self.img = tk.PhotoImage(file=self.card.get_card_value())
            self.canvas.create_image(0, 0, anchor="nw", image=self.img)
        else:
            self.canvas.destroy()
            self.draw_card.destroy()
            self.reshuffle["text"] = "RESHUFFLE DECK?"
            self.reshuffle["command"] = self.start_again
            self.reshuffle.grid(row=3, sticky="news", ipady=20)

    def start_again(self):
        self.card.restart()
        self.create_canvas()
        self.cards_left_label["text"] = "YOU HAVE {} CARDS LEFT IN THE grid!".format(self.card.total_cards)
        self.reshuffle.destroy()
