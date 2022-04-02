class NonKillableObjectError(Exception):
    __module__ = Exception.__module__

    # raised when the engine tries to kill a non killable object
    def __init__(self, obj):
        """
        object obj - the object that cannot be killed
        """
        self.obj = obj
        return

    def __str__(self):
        return f"object {self.obj} has no attribute 'kill' and can't be marked to be killed during collision"
