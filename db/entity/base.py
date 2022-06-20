# from fastapi import UploadFile, File
from pydantic import BaseModel
from pydantic.fields import Field
from datetime import datetime
from utils import helpers


class BaseEntityCreatedAt(BaseModel):
    created_at: datetime = Field(
        default_factory=helpers.get_date_time, alias='CreateAt')
    
    
class BaseEntityFile(BaseModel):
    file: str = Field(default='file.jpg', alias='File')


class BaseEntityRequestId(BaseModel):
    request_id: str = Field(
        default_factory=helpers.generate_request_id, alias='RequestId')


class BaseEntity(BaseModel):
    pk: str = Field(None, min_length=2, alias='PK')
    sk: str = Field(None, min_length=2, alias='SK')

    def get_exclude(self):
        attributes = set()
        for attribute, value in self.__dict__.items():
            if isinstance(value, bool) or isinstance(value, int):
                continue
            if not value:
                attributes.add(attribute)
        return attributes
