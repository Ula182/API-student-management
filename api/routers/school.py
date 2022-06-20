from fastapi import APIRouter
from services import school as school_service
from models.schemas import school as _school_schema

router = APIRouter(
    prefix="/school",
    tags=["School"]
)


@router.post("/create-school/")
def create_school(school_info: _school_schema.SchoolIn):
    return school_service.create_school(school_info)


@router.get(
    "/get-school",
    response_model=_school_schema.SchoolResp,
    status_code=200
)
def get_school(school_name: str):
    return school_service.get_school(school_name)
