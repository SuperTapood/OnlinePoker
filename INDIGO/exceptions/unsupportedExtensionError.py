class UnsupportedExtensionError(Exception):
    # raised when an non supportable extension is tried to being loaded
    # this will not be raised for desktop.ini because i don't think that
    # ini files can be deleted or seen for that matter
    __module__ = Exception.__module__

    def __init__(self, file, loc, typ):
        self.file = file
        self.loc = loc[:-len(file) - 1]
        self.type = typ
        return

    def __str__(self):
        return f"File '{self.file}' at location '{self.loc}' of type '{self.type}' cannot be loaded"
