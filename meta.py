from enum import Enum


class DataFormat(Enum):
    YML = 'yml'
    JSON = 'json'


class DataFile(type):
    def __new__(cls, name, bases, dct):
        spr = super().__new__(cls, name, bases, dct)
        spr.default_format = DataFormat.YML
        return spr
