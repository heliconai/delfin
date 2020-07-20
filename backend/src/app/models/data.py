from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, String, text
from sqlalchemy.dialects.postgresql import JSONB, UUID
from sqlalchemy.orm import relationship

from app.database.base_class import Base

from .util import CastingArray

if TYPE_CHECKING:
    pass


class Data(Base):
    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        index=True,
        server_default=text("uuid_generate_v4()"),
    )
    dataset_id = Column(UUID(as_uuid=True), ForeignKey("datasets.id"), index=True)
    dataset = relationship("Datasets", back_populates="data")
    name = Column(String, index=True)
    properties = Column(JSONB, index=False)
    scopes = Column(CastingArray(JSONB), index=False)
