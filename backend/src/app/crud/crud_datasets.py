from app.crud.base import CRUDBase
from app.models.datasets import Datasets
from app.schemas.datasets import DatasetCreate, DatasetUpdate


class CRUDDatasets(CRUDBase[Datasets, DatasetCreate, DatasetUpdate]):
    pass


datasets = CRUDDatasets(Datasets)
