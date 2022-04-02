from INDIGO.objects.engineobject import EngineObject

from INDIGO.collision import sprite_sprite_collision, sprite_group_collision
from INDIGO.exceptions import CollideTypeError


class Player(EngineObject):
    def __init__(self, scr, img, x, y):
        self.screen = scr
        self.x = x
        self.y = y
        self.img_name = img
        self.img = img
        self.remain_smooth_x = 0
        self.remain_smooth_y = 0
        self.smooth_x = False
        self.smooth_y = False
        self.x_move_factor = 0
        self.y_move_factor = 0
        self.rect = self.get_rekt()
        return

    def blit(self):
        self.smooth()
        self.screen.blit(self.img, self.x, self.y)
        return

    def smooth(self):
        if self.smooth_x:
            self.x += self.smoother_x
            self.remain_smooth_x -= 1
        if self.smooth_y:
            self.y += self.smoother_y
            self.remain_smooth_y -= 1
        if self.remain_smooth_x == 0:
            self.smooth_x = False
        if self.remain_smooth_y == 0:
            self.smooth_y = False
        return

    def move_smoothly(self, direction, factor, frames):
        if direction == "x":
            self.smooth_x = True
            self.remain_smooth_x = frames
            self.smoother_x = factor / self.remain_smooth_x
        elif direction == "y":
            self.smooth_y = True
            self.remain_smooth_y = frames
            self.smoother_y = factor / self.remain_smooth_y
        return

    def check_collide(self, other, resp):
        if hasattr(other, "object_type"):
            if other.object_type == "Group":
                sprite_group_collision(self, other, resp)
            elif other.object_type == "EngineObject":
                sprite_sprite_collision(self, other, resp)
            else:
                raise CollideTypeError(type(other).__name__)
        else:
            raise CollideTypeError(type(other).__name__)
        return

    def __repr__(self):
        module = self.__class__.__module__
        class_name = self.__class__.__name__
        memory_location = hex(id(self))
        return f"<{module}.{class_name} object at {memory_location}>"

    def __str__(self):
        return f"Player {repr(self)} of img {self.img_name} at location ({self.x}, {self.y})"
