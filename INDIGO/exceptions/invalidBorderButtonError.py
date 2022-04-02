class InvalidBorderButtonError(Exception):
    # raised when an invalid border button is being created
    __module__ = Exception.__module__

    def __init__(self, w1, h1, w2, h2):
        """
        int w1, h1, w2, h2 - widths and heights of the two buttons
        """
        self.rect1_dim = (w1, h1)
        self.rect2_dim = (w2, h2)
        return

    def __str__(self):
        return f"Cannot create a button with dims {self.rect2_dim} within rect with dims {self.rect1_dim}"

    pass
