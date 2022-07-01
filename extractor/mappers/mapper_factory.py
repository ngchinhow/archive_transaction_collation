import collections

from extractor.mappers.dbs_mapper import DBSAccountMapper, DBSCardMapper
from extractor.mappers.ocbc_mapper import OCBCAccountMapper, OCBCCardMapper
from extractor.mappers.posb_mapper import POSBCardMapper, POSBAccountMapper
from extractor.mappers.uob_mapper import UOBAccountMapper, UOBCardMapper


class MapperFactory:
    def __init__(self):
        self._mappers = collections.defaultdict(dict)

    def register_mapper(self, key1, key2, mapper):
        self._mappers[key1][key2] = mapper

    def get(self, key1, key2):
        builder = self._mappers[key1][key2]
        return builder


mapper_factory = MapperFactory()

# UOB
mapper_factory.register_mapper('UOB', 'account', UOBAccountMapper)
mapper_factory.register_mapper('UOB', 'card', UOBCardMapper)

# OCBC
mapper_factory.register_mapper('OCBC', 'account', OCBCAccountMapper)
mapper_factory.register_mapper('OCBC', 'card', OCBCCardMapper)

# DBS
mapper_factory.register_mapper('DBS', 'account', DBSAccountMapper)
mapper_factory.register_mapper('DBS', 'card', DBSCardMapper)

# POSB
mapper_factory.register_mapper('POSB', 'account', POSBAccountMapper)
mapper_factory.register_mapper('POSB', 'card', POSBCardMapper)
