from db.data.branch import (
    get_branch_info, get_branch_student,
    get_branch_sample, request_student_sample
)
from db.entity.add_sample import AddSample
from db.entity.branch import Branch, ReqSample
from utils import helpers


def create_branch(branch_info):
    branch = Branch(**branch_info.dict(by_alias=True))
    return helpers.add_data_sk(branch.dict(by_alias=True))


def get_branch(school_name):
    return get_branch_info.get_branch(school_name)


def get_student_branch(branch_name):
    return get_branch_student.get_student_branch(branch_name)


def add_sample_branch(add_sample):
    item = AddSample(**add_sample.dict(by_alias=True))
    return helpers.add_data(item.dict(by_alias=True))


def get_sample_branch(branch_name):
    return get_branch_sample.get_sample_branch(branch_name)


def request_sample_student(branch_request):
    item = ReqSample(**branch_request.dict(by_alias=True))
    return request_student_sample.request_sample_student(item)
