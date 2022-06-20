from fastapi import APIRouter
from services import branch as branch_service
from models.schemas import branch as branch_schema
from models.schemas import student as student_schema
from typing import List

router = APIRouter(
    prefix="/branch",
    tags=["Branch"]
)


@router.post("/create-branch/")
def create_branch(branch: branch_schema.BranchIn):
    return branch_service.create_branch(branch)


@router.get(
    "/get-branch",
    response_model=List[branch_schema.BranchResp],
    status_code=200
)
def get_branch(school_name: str):
    return branch_service.get_branch(school_name)


@router.get(
    "/get-branch-students",
    response_model=List[student_schema.StudentResp],
    status_code=200
)
def get_student_branch(branch_name: str):
    return branch_service.get_student_branch(branch_name)


@router.post("/add-branch-sample")
def add_sample_branch(add_sample: branch_schema.AddSample):
    return branch_service.add_sample_branch(add_sample)


@router.get(
    "/get-branch-sample",
    response_model=List[branch_schema.SampleOfBranch],
    status_code=200
)
def get_sample_branch(branch_name: str):
    return branch_service.get_sample_branch(branch_name)


@router.post("/request-sample-student")
def request_sample_student(
    branch_request: branch_schema.ReqSampleIn
):
    return branch_service.request_sample_student(branch_request)
