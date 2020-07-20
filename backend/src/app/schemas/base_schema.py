from typing import Any

from pydantic import BaseModel
import datetime

class BaseSchema(BaseModel):
    created_on: datetime.datetime
    updated_on: datetime.datetime