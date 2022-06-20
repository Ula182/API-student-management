from fastapi import APIRouter
from services import student as student_service
from models.schemas import student as student_schema
from typing import List


router = APIRouter(
    prefix="/student",
    tags=["Student"]
)


@router.post("/create-student")
def create_student(student: student_schema.StudentIn):
    return student_service.create_student(student)


@router.get(
    "/get-student",
    response_model=List[student_schema.StudentResp],
    status_code=200
)
def get_student(student_id: str):
    return student_service.get_student(student_id)


@router.get(
    "/get-student-request",
    response_model=List[student_schema.RequestStudent],
    status_code=200
)
def get_request_student(student_id: str):
    return student_service.get_request_student(student_id)


@router.post(
    "/response-student-request",
    response_model=List[student_schema.StudentRespSample],
    status_code=200
)
def resp_request_student(
    request: student_schema.StudentRespReqIn
):
    return student_service.resp_request_student(request)
# def resp_request_student(
#     request: student_schema.StudentRespReqIn,
#     file: UploadFile = File(...)
# ):
#     return student_service.resp_request_student(request, file)
