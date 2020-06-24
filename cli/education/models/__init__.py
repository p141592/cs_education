import itertools
from enum import Enum

from .handbook import *
from .materials import *

METATABLES = BaseDBHandbook, BaseDBModel
convert_subclass_to_name = lambda x: x.__tablename__ if x not in METATABLES else None

# Хочу получить список имен всех таблиц
TABLES = set(
    (filter(bool,
            map(convert_subclass_to_name,
                itertools.chain(*[i.__subclasses__() for i in METATABLES])
                )
            )
     )
)

TABLES_ENUM = Enum('TableEnum', " ".join(TABLES))
