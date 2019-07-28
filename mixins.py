from meta import DataFile, DataFormat
import yaml


class ReprMixin(object):
    pass


def load_fn(dtype: DataFormat):
    lds = {
        DataFormat.YML:
            lambda fname: 
                with open(fname, 'r+') as f:
                    yaml.load(f, Loader=yaml.SafeLoader)
    }
    return lds.get(dtype, None)


class DataFileMixin(metaclass=DataFile):
   
    @staticmethod
    def _file_dump(fname: str, data_format: DataFormat, key=None: str) -> dict:
        load_fn = load_fn(data_format)
        dumps = load_fn(fname)
        if key:
            return dumps.get(key, None)
        return dumps

    
