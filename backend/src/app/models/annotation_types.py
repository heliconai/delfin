from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, String, text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.database.base_class import Base

if TYPE_CHECKING:
    pass


class AnnotationTypes(Base):
    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        index=True,
        server_default=text("uuid_generate_v4()"),
    )
    data_modality_id = Column(
        UUID(as_uuid=True), ForeignKey("datamodality.id"), index=True
    )
    data_modality = relationship("DataModality", back_populates="annotation_types")
    annotation_type = Column(String, index=False)
    description = Column(String, index=False)
    label_options = relationship("LabelOptions", back_populates="annotation_type")
