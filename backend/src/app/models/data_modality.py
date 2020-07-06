from typing import TYPE_CHECKING

from sqlalchemy import Column, String, text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.database.base_class import Base

if TYPE_CHECKING:
    pass


class DataModality(Base):
    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        index=True,
        server_default=text("uuid_generate_v4()"),
    )
    data_modality = Column(String, index=False)
    description = Column(String, index=False)
    annotation_types = relationship("AnnotationTypes", back_populates="data_modality")
