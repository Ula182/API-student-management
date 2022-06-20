from pydantic import BaseModel, Field
from typing import Optional


class SchoolName(BaseModel):
    school_name: str = Field(..., alias="SchoolName")


class SchoolEmail(BaseModel):
    school_email: Optional[str] = Field(alias="SchoolEmail")


class SchoolAddresses(BaseModel):
    school_addresses: dict = Field(..., alias="SchoolAddresses")
