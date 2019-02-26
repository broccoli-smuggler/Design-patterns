class SingletonType(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        # Check to see if we've already made a class of this type
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonType, cls).__call__(*args, *kwargs)
        return cls._instances[cls]


class Singleton(metaclass=SingletonType):
    def __init__(self):
        print("blob")


# Should only print "blob" once as it's only created once
s = Singleton()
s2 = Singleton()
s4 = Singleton()
