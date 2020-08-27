"""
Description:
A random card generator as made exclusively by me, it removes the card from the deck when it has been chosen and displays
it into a tkinter GUI
Author: Robbie Campbell
Date: 26/08/2020
"""

from Games.Classes.choice import Options
import tkinter as tk

# Execute the application
if __name__ == "__main__":
    root = tk.Tk()
    app = Options(master=root)
    root.title("Choose an option")
    app.mainloop()
