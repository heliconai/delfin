from app.crud.base import CRUDBase
from app.models.data import Data
from app.schemas.data import DataCreate, DataUpdate


class CRUDData(CRUDBase[Data, DataCreate, DataUpdate]):
    pass


data = CRUDData(Data)
