from inspect import signature

from INDIGO.exceptions import CollideResponseError, CollideTypeError


def check_valid_resp(resp):
    """
    func resp - the response to check
    """
    # if the respond has other then 2 parameters it will break the code
    if len(signature(resp).parameters) != 2:
        raise CollideResponseError(resp.__name__)
    return


def check_valid_group(group):
    # if the group is not a group, it is not iteratable and not fun
    if hasattr(group, "object_type"):
        if group.object_type == "Group":
            return
    raise CollideTypeError(type(group).__name__)
