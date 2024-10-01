from typing import TypeVar, Generic

T = TypeVar('T')


class BaseFactory(Generic[T]):
    _instance = None

    @classmethod
    def get_instance(cls) -> T:
        if cls._instance is None:
            cls._instance = cls.create_instance()

        return cls._instance

    @classmethod
    def create_instance(cls) -> T:
        raise NotImplementedError("Die Methode create_instance() muss in der Unterklasse implementiert werden.")


class BaseService:

    def __init__(self):
        pass
