class IGameObject(object):
    properties = {}

    def show_properties(self):
        raise NotImplementedError()


class IDecorate(IGameObject):
    def __init__(self, game_base):
        self.game_base = game_base

    def show_properties(self):
        self.game_base.show_properties()


class Weight(IDecorate):
    def __init__(self, game_obj, weight):
        self.weight = weight
        super(Weight, self).__init__(game_obj)

    def show_properties(self):
        super().properties[self.__class__.__name__] = self.weight
        super().show_properties()


class Grow(IDecorate):
    def __init__(self, game_obj, length):
        self.length = length
        super(Grow, self).__init__(game_obj)
        super().properties["Length"] = self.length

    def show_properties(self):
        super().show_properties()
        self.length += 1
        super().properties["Length"] = self.length


class WeightySword(IGameObject):
    def __init__(self, sword_name):
        super().properties[self.__class__.__name__] = sword_name

    def show_properties(self):
        print(self.properties)


sword = WeightySword('black')
sword.show_properties()

weightedSword = Weight(sword, 10.0)
weightedSword.show_properties()

weightBiggerSword = Grow(weightedSword, 1)
weightBiggerSword.show_properties()
weightBiggerSword.show_properties()
