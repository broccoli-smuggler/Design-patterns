
class IThingsIDontWantToGoDivingWith(object):
    def is_wet(self):
        raise NotImplementedError()

    def chuck(self):
        raise NotImplementedError()

    def is_on_me(self):
        raise NotImplementedError()


class Phone(IThingsIDontWantToGoDivingWith):
    def __init__(self, on_me=True):
        self.on_me = on_me

    def chuck(self):
        self.on_me = False
        print("Chucked phone")

    def is_wet(self):
        return self.on_me


class Watch(IThingsIDontWantToGoDivingWith):
    def __init__(self, on_me=True):
        self.on_me = on_me
        self.wet = False

    def chuck(self):
        self.wet = True

    def is_wet(self):
        return self.wet


class WhenIGoToDive(object):
    def __init__(self):
        self.things = {}

    def add_item(self, item_name):
        if item_name is 'phone':
            self.things[item_name] = Phone()
        if item_name is 'watch':
            self.things[item_name] = Watch()

    def remove_item(self, item_name):
        if item_name in self.things:
            self.things.pop(item_name)

    def dive(self):
        for thing in self.things.keys():
            self.things[thing].chuck()

        for thing in self.things:
            print(str(thing) + " is wet?:" + str(self.things[thing].is_wet()))


class Person(object):
    def __init__(self, name):
        self.name = name
        self.diving_interface = WhenIGoToDive()
        self.diving_interface.add_item('watch')
        self.diving_interface.add_item('phone')

    def dive(self):
        self.diving_interface.dive()


p = Person('boib')
p.dive()
