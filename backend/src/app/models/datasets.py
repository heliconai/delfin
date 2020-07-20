from typing import TYPE_CHECKING

from sqlalchemy import Column, String, text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.database.base_class import Base

if TYPE_CHECKING:
    pass


class Datasets(Base):
    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        index=True,
        server_default=text("uuid_generate_v4()"),
    )
    name = Column(String, index=True)
    instructions = Column(String, index=False)
    data_modality = Column(String, index=False)
    data = relationship("Data", back_populates="dataset")
    label_options = relationship("LabelOptions", back_populates="dataset")
