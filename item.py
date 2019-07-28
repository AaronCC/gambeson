from enum import Enum
from mixins import DataFileMixin, DataFormat
import random as rand


class ItmSlot(Enum):
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
    def __init__(
            self, 
            itm_type: str,
            itm_level: int,
            itm_base=None
            ) -> None:
        self.itm_type = itm_type
        self.itm_base = itm_base
        self.itm_level = itm_level
        self.data = self._file_dump(
                'data/itm_bases.yml',
                DataFormat.YML,
                key=self.itm_type)
        if not self.data:
            raise NotImplementedError(
                   'failed to load {itm}\
                    from data/itm_bases.yml'.format(itm=str(self))
                    )
        self._make() 


    def _make(self) -> None:
        self.properties = self.data['defaults']
        if not self.itm_base:
            self.itm_base = self._rand_base()
        self.properties.update(self.itm_base)
        self.quality = self._rand_quality()


    def _rand_base(self) -> str:
        possible_bases = self.data['bases']
        self.base_name = rand.choice(list(possible_bases.keys()))
        return possible_bases[self.base_name]

    
    def _rand_quality(self) -> int:
        deviation = self.itm_level // 4
        qual_min = self.itm_level - deviation
        qual_max = self.itm_level + deviation
        return rand.randint(qual_min, qual_max)


    def __str__(self): 
        return 'type: {type} | base: {base}'.format(
                type=self.itm_type, base=self.base_name)
