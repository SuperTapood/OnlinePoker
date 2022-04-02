class GroupAddError(Exception):
    ## raised when the group object gets a non-addable object (non group or engine object) ##
    __module__ = Exception.__module__

    def __init__(self, inst, class_type):
        """
        instance inst - the instance of class class type that is being tried to be added to the group
        class type class_type - the pythonic expression of the class type of instance inst (which needs to beautification)
        """
        self.type = str(class_type)[7:]
        self.type = self.type[:-1]
        self.inst = inst
        return

    def __str__(self):
        return f"instance '{self.inst}' of class type {self.type} cannot be added to a Group"
