from meta import DataFile, DataFormat
import yaml


class ReprMixin(object):
    pass


def load_fn(dtype: DataFormat):
    lds = {
        DataFormat.YML: lambda fname:
                yaml.load(open(fname, 'r+'), Loader=yaml.SafeLoader)
    }
    return lds.get(dtype, None)


class DataFileMixin(metaclass=DataFile):
   
    @staticmethod
    def _file_dump(fname: str, data_format: DataFormat, key=None) -> dict:
        dumps = load_fn(data_format)(fname)
        if key:
            return dumps.get(key, None)
        return dumps
