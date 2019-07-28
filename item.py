""" 
LETS MAKE SOME ITEMS
"""
from enum import Enum

class ItmType(Enum):
    HEAD = 'head'
    BODY = 'body' 
    LEGS = 'legs' 
    TRK1 = 'trk1' 
    TRK2 = 'trk2'
    ARM1 = 'arm1' 
    ARM2 = 'arm2' 


class DmgType(Enum):
    SLSH = 'slsh' 
    STAB = 'stab' 
    CRSH = 'crsh' 


class Item(DataFileMixin):
    def __init__(self) -> None:


# what is an item?
# * constitution cost (is it heavy)
# * item type
# * stats
# * quality

# enemies drop what they're carrying!


