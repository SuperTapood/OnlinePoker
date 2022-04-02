import inspect

from INDIGO.image import Image


# this is seemingly useless, but this will handle collision later on ##
# the engine object meta classes will talk to each other ##
# to decide if a collision was made ##

class EngineObject:
    object_type = "EngineObject"

    # we also got this sick useless function
    def get_attributes(self, output=False):
        att_dict = {}
        memebers = inspect.getmembers(self, lambda a: not (inspect.isroutine(a)))
        for memeber in memebers:
            attribute = memeber[0]
            value = memeber[1]
            # exclude builtin attributes
            if not attribute[:2] == attribute[-2:] == "__":
                att_dict[attribute] = value
        if output:
            print(att_dict)
        return att_dict

    def process_event(self, event):
        ## placeholder method ##
        pass

    def get_rekt(self):
        try:
            return self.rect
        except AttributeError:
            self.__set_rect()
            return self.get_rekt()
        return

    def __set_rect(self):
        if type(self.img) == str:
            self.img = Image(self.img).get_img()
        self.rect = self.img.get_rect()
        x = self.rect.x
        y = self.rect.y
        w = self.rect.width
        h = self.rect.height
        self.rect = self.x, self.y, w, h
        return
