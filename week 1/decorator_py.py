
class IThing(object):
    def show_props(self):
        raise NotImplementedError()


def magic(cls):
    class Magic(IThing):
        def __init__(self, *args, **kwargs):
            self.instance = cls(*args, **kwargs)
            self.base_instance = self.instance
            while not hasattr(self.base_instance, 'props'):
                self.base_instance = self.base_instance.base_instance

        def show_props(self):
            for p in self.base_instance.props.keys():
                new_v = self.base_instance.props[p]
                if p is 'weight':
                    new_v = -1
                elif p is 'name':
                    new_v = 'magic ' + new_v
                self.base_instance.props[p] = new_v
            cls.show_props(self.instance)
    return Magic


def weight(cls):
    class Weight(IThing):
        def __init__(self, *args, **kwargs):
            self.instance = cls(*args, **kwargs)
            self.base_instance = self.instance
            if not kwargs['weight']:
                raise NotImplemented()
            while not hasattr(self.base_instance, 'props'):
                self.base_instance = self.base_instance.base_instance
            self.base_instance.props['weight'] = kwargs['weight']

        def show_props(self):
            cls.show_props(self.instance)
    return Weight


@weight
class WeightSword(IThing):
    def __init__(self, name, *args, **kwargs):
        self.props = {'name': name}

    def show_props(self):
        print(self.props)


@magic
@weight
class MagicWeightSword(IThing):
    def __init__(self, name, *args, **kwargs):
        self.props = {'name': name}

    def show_props(self):
        print(self.props)


w = MagicWeightSword("sword", {}, weight=1)
w.show_props()

r = WeightSword("ws", {}, weight=2)
r.show_props()
w.show_props()
