import inspect
from pprint import pprint


class Example:
    def __init__(self):
        self.atr = 1
        pass
    def method(self):
        pass
object_1 = Example()

def introspection(obj):
    print(type(obj))
    print('\n')
    print(dir(obj))
    print('\n')
    pprint(inspect.getmembers(obj))
    print('\n')
    print(inspect.getmodule(obj))

introspection(object_1)