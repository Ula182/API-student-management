from db.data.student.get_student_info import get_student_info
from db.data.student.get_student_request import get_request_of_student
from db.data.student.response_student_resquest import resp_request_of_student
from db.entity.student import Student
from models.schemas import student as _student_schema
from utils import get_request, helpers


def create_student(student_info: _student_schema.StudentIn):
    item = Student(**student_info.dict(by_alias=True))
    return helpers.add_data([item])


def get_student(student_id: str):
    return get_student_info(student_id)


def get_request_student(student_id: str):
    return get_request_of_student(student_id)


def resp_request_student(
    request: _student_schema.StudentRespReqIn
):
    request_student = get_request.get_req_student(request)
    return resp_request_of_student(
        request_student
    )
