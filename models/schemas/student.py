from models.domains import (
    student as _domains_student,
    branch as _domains_branch,
    sample as _domains_sample
)


class StudentIn(
    _domains_student.StudentId, _domains_student.StudentEmail,
    _domains_student.StudentFirstName, _domains_student.StudentLastName,
    _domains_branch.BranchName
):
    pass


class StudentResp(StudentIn):
    pass


class StudentRespSample(
    _domains_branch.ReqSampleName, _domains_branch.BranchName, 
    _domains_branch.ReqSampleDeadLine, _domains_branch.ReqSampleStatus,
    _domains_sample.SampleFile
):
    pass


class RequestStudent(
   StudentRespSample, _domains_branch.ReqSampleCreateAt
):
    pass


class StudentRespReqIn(
    _domains_sample.SampleName, _domains_branch.BranchName,
    _domains_student.StudentId
):
    pass
