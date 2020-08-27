import os
import time


class Images:
    def __init__(self):
        self.index = 1
        self.root = os.getenv("RootPathPython")
        self.image_prefix = self.root + "/DeckOfCards/Games/Classes/View/PNG/"
        self.descriptors = {1: "Isnt That Nice?",
                            2: "Na ma ste",
                            3: "God of war was good",
                            4: "What a cool game",
                            5: "The real waifu",
                            6: "What a happy chap!"}

    def next_image(self):
        self.index += 1
        resulting_image = self.image_prefix + str(self.index) + ".png"
        if self.index >= len(self.descriptors) + 1:
            self.index = 1
            resulting_image = self.image_prefix + str(self.index) + ".png"
        return resulting_image

    def prev_image(self):
        self.index -= 1
        resulting_image = self.image_prefix + str(self.index) + ".png"
        if self.index == 0:
            self.index = len(self.descriptors)
            resulting_image = self.image_prefix + str(self.index) + ".png"
        return resulting_image
