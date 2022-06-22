from pydantic import BaseModel, Field
from typing import Optional


class BranchName(BaseModel):
    branch_name: str = Field(..., alias="BranchName")


class BranchEmail(BaseModel):
    branch_email: Optional[str] = Field(alias="BranchEmail")


class ReqSampleTo(BaseModel):
    request_to: str = Field(..., alias="ReqSampleTo")


class ReqSampleName(BaseModel):
    sample_name: str = Field(alias="ReqSampleName")


class ReqSampleStatus(BaseModel):
    status: str = Field(alias="ReSampleStatus")


class ReqSampleDeadLine(BaseModel):
    dead_line: str = Field(alias="ReqSampleDeadLine")
    
    
class ReqSampleCreateAt(BaseModel):
    created_at: str = Field(alias="CreatedAt")
