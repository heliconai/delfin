from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy import cast

class CastingArray(ARRAY):
    def bind_expression(self, bindvalue):
        return cast(bindvalue, self)
