class CollideTypeError(Exception):
    __module__ = Exception.__module__

    # raised when a non-group object is referd to as a group
    def __init__(self, non_group_type):
        self.non_group_type = non_group_type
        return

    def __str__(self):
        return f"class type '{self.non_group_type}' is not of class type Group"
