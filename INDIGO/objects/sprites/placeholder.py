from inspect import signature

from INDIGO.objects.engineobject import EngineObject

from INDIGO.collision import sprite_sprite_collision, sprite_group_collision
from INDIGO.exceptions import CollideTypeError
from INDIGO.exceptions import PlaceholderBlitError


class Placeholder(EngineObject):
    def __init__(self, scr, img, x=None, y=None, deployable=None):
        self.deployable = Placeholder
        if deployable is not None:
            self.deployable = deployable
        self.scr = scr
        self.img = img
        self.x = x
        self.y = y
        # if len(signature(self.delpoyable).__init__) != 2:
        #     raise InvalidDeployableError(self.delpoyable.__name__)
        return

    def deploy(self, x, y):
        return self.clone(x, y)

    def clone(self, x, y):
        return self.deployable(self.scr, self.img, x, y)

    def blit(self):
        if self.x is None or self.y is None:
            raise PlaceholderBlitError(self, self.x, self.y)
        self.rect = self.get_rekt()
        self.scr.blit(self.img, self.x, self.y)
        return

    def check_collide(self, other, resp):
        if hasattr(other, "object_type") and other.object_type == "Group":
            sprite_group_collision(self, other, resp)
        elif hasattr(other, "object_type") and other.object_type == "EngineObject":
            sprite_sprite_collision(self, other, resp)
        else:
            raise CollideTypeError(type(other).__name__)
        return

    def __repr__(self):
        module = self.__class__.__module__
        class_name = self.__class__.__name__
        memory_location = hex(id(self))
        return f"<{module}.{class_name} object at {memory_location}>"

    def __str__(self):
        return f"Placeholder {repr(self)} at location ({self.x}, {self.y}) which deploys {self.delpoyable}"
