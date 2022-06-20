from pydantic import BaseModel, Field
from typing import Optional


class StudentId(BaseModel):
    student_id: str = Field(..., alias="StudentId")


class StudentEmail(BaseModel):
    student_email: Optional[str] = Field(alias="StudentEmail")


class StudentFirstName(BaseModel):
    student_firstname: str = Field(..., alias="StudentFirstName")


class StudentLastName(BaseModel):
    student_lastname: str = Field(..., alias="StudentLastName")
    
    