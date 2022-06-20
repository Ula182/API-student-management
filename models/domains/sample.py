from pydantic import BaseModel, Field


class SampleName(BaseModel):
    sample_name: str = Field(..., alias="SampleName")
    
    
class SampleOwner(BaseModel):
    owner_sample: str = Field(..., alias="OwnerSample")


class SampleFile(BaseModel):
    file: str = Field(..., alias="File")


class SampleDescription(BaseModel):
    description: str = Field(..., alias="Description")
    
