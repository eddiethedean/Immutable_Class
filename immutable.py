import inspect
class Immutable(object):
        def __setattr__(self, *args):
                if inspect.stack()[1][3] == '__init__':
                        object.__setattr__(self, *args)
                else:
                        raise TypeError('Cannot modify immutable instance')
        
        __delattr__ = __setattr__
