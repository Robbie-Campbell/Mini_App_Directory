from Classes.Guesser import game
from Classes.Home import return_home_button
from tkinter.font import Font
import time
import tkinter as tk


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master.resizable(False, False)
        self.master = master

        # Define variables to make the text panel a consistent size
        self.rowconfigure(2, minsize=300)
        self.columnconfigure(1, minsize=500)
        self.grid()

        # Create a better looking font object
        self.arial16 = Font(family="arial", size=16, weight="bold")
        self.arial20 = Font(family="arial", size=20, weight="bold", underline = True)
        self.arial30 = Font(family="arial", size=30, weight="bold")

        # Allows the user to return back to the home directory
        self.back = return_home_button.ReturnHome(self, self.master)
        self.back.return_button.grid(row=0, column=1, sticky="news")

        # Create an instance of the Guess class
        self.guess = game.Guess()

        # The title of the current game is set here
        self.guessing_game_title = tk.Label(self, font=self.arial20, fg="#FFF", bg="#151", pady=5)
        self.guessing_game_title["text"] = "Audio Guessing game"
        self.guessing_game_title.grid(row=1, column=1, sticky="news", ipady=5)

        # Tells the user what to do and is updated later with each guess
        self.description = tk.Label(self, font=self.arial16, fg="#222", bg="#CCF", pady=5)
        self.description["text"] = "Speak into the microphone to guess a word\n {}"\
                                   .format(self.guess.instructions).upper()
        self.description.grid(row=2, column=1, sticky="news")

        # Define the buttons look and position
        self.arial16 = Font(family="arial", size=16, weight="bold")
        self.take_guess_button = tk.Button(self, bg="#151", font=self.arial16, fg="#DDD")
        self.take_guess_button["text"] = "TAKE A GUESS"
        self.take_guess_button["command"] = self.new_guess
        self.take_guess_button.grid(row=3, column=1, sticky="news", ipady=5)

        # Create a fruit image
        self.canvas = tk.Canvas(self, width=500, height=449, bd=0, highlightthickness=0, bg="#FFF")
        self.img = tk.PhotoImage(file="Classes/Guesser/fruits.png")
        self.canvas.create_image(0, 0, anchor="nw", image=self.img)
        self.canvas.grid(row=0, column=0, rowspan=4)

    # Function is called when the user wants to make a guess at the word
    def new_guess(self):
        self.guess.guess_attempt()
        self.description["font"] = self.arial30
        self.description["text"] = self.guess.output.upper()
        if self.guess.current_guess == 3 or self.guess.guess_is_correct:
            self.take_guess_button["text"] = "TRY AGAIN?"
            self.take_guess_button["command"] = self.reset_game

    # Gives the user the option to start the game again
    def reset_game(self):
        self.guess = game.Guess()
        self.take_guess_button["text"] = "TAKE A GUESS"
        self.description["font"] = self.arial16
        self.description["text"] = "Speak into the microphone to guess a word\n {}"\
                                   .format(self.guess.instructions).upper()
        self.take_guess_button["command"] = self.new_guess
