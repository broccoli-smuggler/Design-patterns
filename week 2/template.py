class Camera(object):
    def __init__(self, key):
        self.key = key
        self.current_frame = None

    def grab_frame(self):
        raise NotImplementedError()

    def assign_settings(self):
        raise NotImplementedError()

    def get_frame(self):
        self.grab_frame()
        return self.current_frame

    def get_key(self):
        return self.key


class ACam(Camera):
    def __init__(self):
        super(ACam, self).__init__(self.__class__.__name__)

    def assign_settings(self):
        print("assigned " + self.key)

    def grab_frame(self):
        self.current_frame = "A FRAME"


class BCam(Camera):
    def __init__(self):
        super(BCam, self).__init__(self.__class__.__name__)

    def assign_settings(self):
        print("assigned " + self.key)

    def grab_frame(self):
        self.current_frame = "B FRAME"


a = ACam()
a.assign_settings()
print(a.get_frame())
b = BCam()
b.assign_settings()
print(b.get_frame())
