from Classes.Guesser.play import recognise_speech
import speech_recognition as sr
import random
import time


# This class contains all information for the guessing game
class Guess:
    def __init__(self):

        # Potential AI word choice
        self.words = ["Apple", "Banana", "Grape", "Orange", "Mango", "Lemon"]

        # Define variables for keeping track of the game
        self.num_guesses = 3
        self.prop_limit = 5
        self.current_guess = 0
        self.guess = ""

        # These variables pass in the users voice
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()

        # The word the user needs to guess
        self.word = random.choice(self.words)

        self.plural = "guesses"

        # Description always resets to this core message after each game
        self.instructions = (
            "I'm thinking of one of these words!:\n\n"
            "{}\n\n"
            "You have {} tries to guess which one.\n"
        ).format('\n'.join(self.words), self.num_guesses)

        # Stores current description information
        self.output = 'Guess {}. Speak!'.format(self.current_guess)
        self.guess_is_correct = ""

    def guess_attempt(self):

        # Passes in information to be translated to a string value
        self.guess = recognise_speech(self.recognizer, self.microphone)

        # Sets the text of the output for the user and checks conditions to see if they are correct
        # Also error handling is carried out here
        if self.guess["transcription"]:
            self.output = "You said: {}".format(self.guess["transcription"])
            self.guess_is_correct = self.guess["transcription"].lower() == self.word.lower()
        if not self.guess["Success"]:
            self.output = "ERROR: {}".format(self.guess["Error"])
            return
        if self.guess["Error"]:
            self.output = "I didn't catch that.\nWhat did you say?"
            return

        # Handles whether there is more than one guess
        if self.current_guess == 1:
            self.plural = "guess"

        # Win condition
        if self.guess_is_correct:
            self.output = "Correct! You win! \nThe word was:\n{}!".format(self.word)
        elif self.current_guess < 2:
            self.output = "{} {} left\n\n{} was incorrect.\nHave another try"\
                .format(2 - self.current_guess, self.plural, self.guess["transcription"].capitalize())
            self.current_guess += 1

        # Lose condition
        else:
            self.current_guess += 1
            self.output = "Sorry, you lose!\nI was thinking of:\n{}.".format(self.word)
