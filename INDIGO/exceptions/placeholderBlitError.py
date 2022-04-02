class PlaceholderBlitError(Exception):
    ## raise this when the group object gets a non-addable object (non group or engine object) ##
    __module__ = Exception.__module__

    def __init__(self, x, y):
        """
        int x, y - the loc of the blitting
        """
        self.x = x
        self.y = y
        return

    def __str__(self):
        return f"cannot blit placeholder to pos ({self.x}, {self.y})"
