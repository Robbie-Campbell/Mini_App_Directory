import Games.Classes.Home.choice as choice
import tkinter as tk
from tkinter.font import Font


class ReturnHome:
    def __init__(self, window_to_destroy, window):
        self.arial16 = Font(family="arial", size=16, weight="bold")
        self.return_button = tk.Button(window_to_destroy, bg="#FFF", font=self.arial16, fg="#000")
        self.return_button["text"] = "HOME"
        self.return_button["command"] = self.return_home
        self.window_to_destroy = window_to_destroy
        self.window = window

    def return_home(self):
        home = choice.Options(self.window)
        self.window_to_destroy.destroy()
