import pygame


# the purpose of this class is to ease the image manipulation in pygame

class Image:
    def __init__(self, path):
        """
        r path - the path to the image
        """
        # load the image
        self.image = self.load_image(path)
        return

    def load_image(self, path):
        """
        r path - the path to the image
        """
        return pygame.image.load(path)

    def get_img(self):
        # get img just sounds way better
        # trust me
        # im a cs
        return self.image

    def get_dims(self):
        # return the dimensions of the image
        # idk might be useful
        rect = self.image.get_rect()
        x = rect.x
        y = rect.y
        w = rect.w
        h = rect.h
        return f"x: {x}, y: {y}, w: {w}, h: {h}"

    def rescale(self, new_scale):
        """
        int/float new_scale - the new scale of the image to be resized
        """
        # provide a way to scale images rather then define x and y
        new_x = self.image.get_rect().w * new_scale
        new_y = self.image.get_rect().h * new_scale
        self.resize(new_x, new_y)
        return

    def resize(self, x, y):
        """
        resize the image to (x, y)
        """
        self.image = pygame.transform.scale(self.image, (int(x), int(y)))
        return

    def match_size(self, image):
        ## ! will fill this space later ! ##
        pass

    def __repr__(self):
        module = self.__class__.__module__
        class_name = self.__class__.__name__
        memory_location = hex(id(self))
        return f"<{module}.{class_name} object at {memory_location}>"

    def __str__(self):
        obj = repr(self)
        dims = self.get_dims()
        out = f"{obj} with dimensions {dims}\n"
        return out

    def rotate(self, ang):
        self.image = pygame.transform.rotate(self.image, ang)
        return

    def get_rect(self):
        return self.get_img().get_rect()
