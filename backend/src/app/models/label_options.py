from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, text
from sqlalchemy.dialects.postgresql import JSONB, UUID
from sqlalchemy.orm import relationship

from app.database.base_class import Base

from .util import CastingArray

if TYPE_CHECKING:
    pass


class LabelOptions(Base):
    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        index=True,
        server_default=text("uuid_generate_v4()"),
    )
    project_id = Column(UUID(as_uuid=True), ForeignKey("projects.id"), index=True)
    project = relationship("Projects", back_populates="label_options")
    annotation_type_id = Column(
        UUID(as_uuid=True), ForeignKey("annotationtypes.id"), index=False
    )
    annotation_type = relationship("AnnotationTypes", back_populates="label_options")
    labels = Column(CastingArray(JSONB), index=False)
