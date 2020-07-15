from app.crud.base import CRUDBase
from app.models.data_modality import DataModality
from app.schemas.data_modality import DataModalityCreate, DataModalityUpdate


class CRUDDataModality(CRUDBase[DataModality, DataModalityCreate, DataModalityUpdate]):
    pass


data_modality = CRUDDataModality(DataModality)
