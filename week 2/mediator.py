class IMediator(object):
    def addCollegue(self, collegue):
        raise NotImplementedError()

    def ask_for_help(self, another_collegue):
        raise NotImplementedError()


class ICollegue(object):
    def update(self, is_moving, is_asking):
        raise NotImplementedError()


class John(ICollegue):
    def __init__(self):
        self.is_moving = False
        self.is_helping = False

    def update(self, is_moving, is_helping):
        self.is_moving = is_moving
        self.is_helping = is_helping
        print(self.__class__.__name__ + str(self.is_helping))


class John2(ICollegue):
    def __init__(self):
        self.is_moving = False
        self.is_helping = False

    def update(self, is_moving, is_helping):
        self.is_moving = is_moving
        self.is_helping = not is_helping
        print(self.__class__.__name__ + str(self.is_helping))


class Mediator(IMediator):
    def __init__(self, name):
        self.name = name
        self.collegues = {}

    def addCollegue(self, other):
        self.collegues[other.__class__.__name__] = other

    def ask_for_help(self, another):
        if another.__class__.__name__ in self.collegues:
            another.update(False, True)


m = Mediator("me")

j1 = John()
j2 = John2()
j3 = John()

m.addCollegue(j1)
m.addCollegue(j3)
m.addCollegue(j2)

m.ask_for_help(j2)
