from db.data.student import (
    get_student_info, get_student_request,
    response_student_resquest
)
from db.entity.student import Student
from models.schemas import student as _student_schema
from utils import get_request, helpers


def create_student(student_info):
    item = Student(**student_info.dict(by_alias=True))
    return helpers.add_data(item.dict(by_alias=True))


def get_student(student_id):
    return get_student_info.get_student(student_id)


def get_request_student(student_id):
    return get_student_request.get_request_student(student_id)


def resp_request_student(
    request: _student_schema.StudentRespReqIn
):
    request_student = get_request.get_req_student(request)
    return response_student_resquest.resp_request_student(
        request_student
    )

# def resp_request_student(
#     request: _student_schema.StudentRespReqIn,
#     file: UploadFile
# ):
#     request_student = get_req_student(request)
#     return response_student_resquest.resp_request_student(
#         request_student,
#         file
#     )
