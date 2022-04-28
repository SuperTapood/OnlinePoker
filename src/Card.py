import pygame

from Engine import Screen

conv_value = {
    1: "ace",
    11: "jack",
    12: "queen",
    13: "king"
}

conv_type = ["clubs", "diamonds", "hearts", "spades"]


class Card:
    def __init__(self, value: int, cls: int):
        """
        create a new card instance
        :param value: the value of the card (ranges from ace to king)
        :param cls: the class of the card (club, diamond, heart, spade)
        """
        self.real_img = self.get_image(value, cls)
        self.img = pygame.image.load(f"..\\assets\\Cards\\back.png")
        self.img = pygame.transform.scale(self.img, (self.real_img.get_width(), self.real_img.get_height()))
        if value in conv_value.keys():
            value = conv_value.get(value)[0].upper()
        if value == 10:
            value = "T"
        self.code = f"{value}{conv_type[cls][0]}"
        self.rect = [0, 0, 0, 0]
        return

    @staticmethod
    def get_image(value: int, cls: int):
        """
        get an image file from input parameters
        :param value: the value of the card (ranges from ace to king)
        :param cls: the class of the card (club, diamond, heart, spade)
        :return: the resulting image
        """
        if value in conv_value.keys():
            value = conv_value.get(value)
        cls = conv_type[cls]
        img = pygame.image.load(f"..\\assets\\Cards\\{value}_of_{cls}.png")
        return pygame.transform.scale(img, (img.get_width() / 3.5, img.get_height() / 3.5))

    def blit(self):
        """
        render the image on the screen
        """
        Screen.scr.blit(self.img, self.rect)
        return

    def set_index(self, card_index, hand_index):
        """
        manipulate the card to show it nicely
        do not even attempt to understand what is happening here

        :param card_index: the index of this card
        :param hand_index: the index of the hand this card is in
        :return this instance because I feel it adds personality to the function
        """
        # self.img = self.real_img
        if hand_index == 0:
            self.rect[0] = 350 + card_index * 50
            self.rect[1] = 750
            self.img = self.real_img
        elif hand_index == 1:
            self.img = pygame.transform.rotate(self.img, 90)
            self.rect[0] = 0
            self.rect[1] = 350 + card_index * 30
        elif hand_index == 2:
            self.img = pygame.transform.rotate(self.img, -14 * (1 - (card_index * 2)))
            self.rect[0] = 350 + card_index * 50
            self.rect[1] = 0
        elif hand_index == 3:
            self.img = pygame.transform.rotate(self.img, -14 * (1 - (card_index * 2)))
            self.img = pygame.transform.rotate(self.img, -90)
            self.rect[0] = 800
            self.rect[1] = 350 + card_index * 30
        rot = pygame.transform.rotate(self.img, 7 * (1 - (card_index * 2)))
        self.rect = rot.get_rect(center=self.img.get_rect(center=(self.rect[0], self.rect[1])).center)
        self.img = rot
        return self

    pass
