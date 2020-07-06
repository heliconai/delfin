from app.crud.base import CRUDBase
from app.models.label_options import LabelOptions
from app.schemas.label_options import LabelOptionCreate, LabelOptionUpdate


class CRUDLabelOptions(CRUDBase[LabelOptions, LabelOptionCreate, LabelOptionUpdate]):
    pass


label_options = CRUDLabelOptions(LabelOptions)
