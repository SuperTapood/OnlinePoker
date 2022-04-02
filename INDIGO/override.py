from INDIGO.exceptions import OverrideError


def override(interface_class):
    # assert im overriding an existing method
    def overrider(method):
        if method.__name__ in dir(interface_class):
            return method
        else:
            raise OverrideError(method.__name__, interface_class.__name__)

    return overrider
