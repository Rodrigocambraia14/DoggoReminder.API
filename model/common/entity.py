from abc import ABCMeta, abstractmethod

#obriga as classes que herdarem de Entity, a implementarem um construtor

class EntityMeta(ABCMeta):
    def __init__(cls, name, bases, dct):
        if not hasattr(cls, '_abstract') or not cls._abstract:
            if '__init__' not in dct or not callable(getattr(cls, '__init__')):
                raise TypeError(f"Class '{cls.__name__}' must provide a constructor '__init__'")
        super(EntityMeta, cls).__init__(name, bases, dct)

class Entity(metaclass=EntityMeta):
    _abstract = True

    @abstractmethod
    def __init__(self, *args, **kwargs):
        pass