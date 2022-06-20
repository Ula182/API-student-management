from fastapi import APIRouter
from services import sample as sample_service
from models.schemas import sample as sample_schema

router = APIRouter(
    prefix="/sample",
    tags=["Sample"]
)


@router.post("/create-sample/")
def create_sample(sample: sample_schema.SampleIn):
    return sample_service.create_sample(sample)

