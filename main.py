"""
Description:
A random card generator as made exclusively by me, it removes the card from the deck when it has been chosen and displays
it into a tkinter GUI
Author: Robbie Campbell
Date: 26/08/2020
"""

from Cards import gui
import tkinter as tk

# Execute the application
if __name__ == "__main__":
    root = tk.Tk()
    app = gui.Application(master=root)
    root.title("Random card generator")
    app.mainloop()