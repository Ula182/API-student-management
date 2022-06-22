from db.data.branch.get_branch_info import get_branch_info
from db.data.branch.get_branch_student import get_student_info_branch
from db.data.branch.get_branch_sample import get_sample_of_branch
from db.data.branch.request_student_sample import request_sample_of_student
from db.entity.add_sample import AddSample
from db.entity.branch import Branch, ReqSample
from utils import helpers
from models.schemas import (
    branch as _branch_schema,
    student as _student_schema
)


def create_branch(branch_info: _branch_schema.BranchIn):
    branch = Branch(**branch_info.dict(by_alias=True))
    return helpers.add_data_sk(branch)


def get_branch(school_name: str):
    return get_branch_info(school_name)


def get_student_branch(branch_name: str):
    return get_student_info_branch(branch_name)


def add_sample_branch(add_sample: _branch_schema.AddSample):
    item = AddSample(**add_sample.dict(by_alias=True))
    return helpers.add_data([item])


def get_sample_branch(branch_name: str):
    return get_sample_of_branch(branch_name)


def request_sample_student(branch_request: _student_schema.StudentRespReqIn):
    item = ReqSample(**branch_request.dict(by_alias=True))
    return request_sample_of_student(item)
