class InvalidDeployableError(Exception):
    __module__ = Exception.__module__

    # raised when a non-deployable object is being defined as deployable
    def __init__(self, class_name):
        """
        str class_name - the name of the class that cannot be deployed
        """
        self.class_name = class_name
        return

    def __str__(self):
        return f"{self.class_name} cannot be used a deployable"
