class CollideResponseError(Exception):
    __module__ = Exception.__module__

    # raised when the engine tries to call a collide response function with
    # other then 2 arguments (collider1, collider2)
    def __init__(self, func_name):
        """
        func func_name - the function that doesnt fit for collision response
        """
        self.func_name = func_name
        return

    def __str__(self):
        return f"function '{self.func_name}' does not take exactly 2 arguments and cannot be used as a collide response"
