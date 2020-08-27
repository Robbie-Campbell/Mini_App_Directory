import tkinter as tk
from tkinter.font import Font
from Games.Classes.View import image_sorter
from Games.Classes.Home import return_home_button


class TheView(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master, bg="#000")
        self.master = master
        self.master.resizable(False, False)
        self.grid()
        self.current = 0

        # Create an instance of the image sorter class
        self.views = image_sorter.Images()

        # Allows the user to return back to the home directory
        self.back = return_home_button.ReturnHome(self, self.master)
        self.back.return_button.grid(row=0, columnspan=2, sticky="news")

        # Set the header text
        self.arial16 = Font(family="arial", size=16, weight="bold")
        self.header = tk.Label(self, font=self.arial16, bg="#000", fg="#FFF")
        self.header["text"] = self.views.descriptors[self.views.index]
        self.header.grid(row=1, columnspan=2)

        # Create a default image for application startup
        self.canvas = tk.Canvas(self, width=600, height=400, bd=0, highlightthickness=0, bg="#000")
        self.img = tk.PhotoImage(file="C:/Users/robbi/Python/DeckOfCards/Games/Classes/View/PNG/1.png")
        self.canvas.create_image(0, 0, anchor="nw", image=self.img)
        self.canvas.grid(row=2, columnspan=2)

        # Next image options
        self.next_image = tk.Button(self, font=self.arial16, bg="#FFF", fg="#222",
                                    command=lambda: self.show_image("next"))

        self.next_image["text"] = "NEXT IMAGE"
        self.next_image.grid(row=3, column=1, columnspan=1, ipady=5, sticky="news")

        # Previous image options
        self.prev_image = tk.Button(self, font=self.arial16, bg="#FFF", fg="#222",
                                    command=lambda: self.show_image("prev"))

        self.prev_image["text"] = "PREV IMAGE"
        self.prev_image.grid(row=3, column=0, columnspan=1, ipady=5, sticky="news")

    # Function passes in whether the user is hitting next or previous for the image and then updates the current image
    # and the title
    def show_image(self, direction):
        if direction == "next":
            self.img = tk.PhotoImage(file=self.views.next_image())
        elif direction == "prev":
            self.img = tk.PhotoImage(file=self.views.prev_image())
        self.canvas.create_image(0, 0, anchor="nw", image=self.img)
        self.header["text"] = self.views.descriptors[self.views.index]

