from random import randint


# Initialise standard variables and create a card_deck class
class CardDeck:
    def __init__(self):
        self.royals = ["Jack", "Queen", "King", "Ace"]
        self.names = ["Hearts", "Diamonds", "Spades", "Clubs"]
        self.full_deck = self.create_deck()
        self.total_cards = 52
        self.card_drawn = ""
        self.card_PNG_value_default = "Cards/PNG/"
        self.PNG_value = ""
        self.array_row = []

    def create_deck(self):
        created_full_deck = []
        # Appends a card of each suit to the full_deck list
        for starter, name in enumerate(self.names):
            created_full_deck.append([str(x) + " of " + self.names[(x + starter) % 4] for x in range(2, 11)])
            starter += 1

        for starter, name in enumerate(self.royals):
            created_full_deck.append([name + " of " + self.names[(x + starter) % 4] for x in range(1, 5)])
            starter += 1

        return created_full_deck

    # Selects a random card from the deck and then removes it, also removes the tuples in the list
    def draw_a_card(self):
        if self.total_cards > 0:
            self.total_cards -= 1
            random_number = randint(0, len(self.full_deck) - 1)
            self.array_row = self.full_deck[random_number]
            if len(self.array_row) > 0:
                result = randint(0, len(self.array_row) - 1)
                self.card_drawn = self.array_row[result]
                self.array_row.remove(self.card_drawn)
                if len(self.array_row) == 0:
                    self.full_deck.remove(self.full_deck[random_number])

        else:
            self.restart()

    # Loops back to a full deck with a new random amount
    def restart(self):
        self.total_cards = 52
        self.full_deck = self.create_deck()

    # Converts the text information from the card drawn into a format which can be read into the png file, to display
    # an image in the gui.py file
    def get_card_value(self):
        first_letters = self.card_drawn.split(" ")
        card_value = [first_letter[0] for first_letter in first_letters]
        if card_value[0] == "1":
            card_value[0] = "10"
        self.PNG_value = self.card_PNG_value_default + (card_value[0] + card_value[len(card_value) - 1] + ".png")
        return self.PNG_value
