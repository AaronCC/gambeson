from meta import DataFile, DataFormat
import yaml


# mapping of DataFormat -> loader fn
LOADERS = {
    DataFormat.YML: lambda fname:
            yaml.load(open(fname, 'r+'), Loader=yaml.SafeLoader)
}


class DataFileMixin(metaclass=DataFile):

    @staticmethod
    def _file_dump(fname: str, data_format: DataFormat, key=None) -> dict:
        loader = LOADERS.get(data_format, None)
        if not loader:
            raise NotImplementedError(
                    'no loader implemented for dataformat: '+data_format)
        dumps = loader(fname)
        if key:
            return dumps.get(key, None)
        return dumps
