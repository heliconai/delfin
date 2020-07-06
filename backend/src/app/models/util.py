from sqlalchemy import cast
from sqlalchemy.dialects.postgresql import ARRAY


class CastingArray(ARRAY):
    def bind_expression(self, bindvalue):
        return cast(bindvalue, self)
