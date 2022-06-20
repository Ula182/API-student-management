from models.domains import (
    branch as _domains_branch,
    school as _domains_school,
    sample as _domains_sample
)


class BranchIn(
    _domains_school.SchoolName, _domains_branch.BranchName,
    _domains_branch.BranchEmail
):
    pass


class BranchResp(BranchIn):
    pass


class AddSample(
    _domains_branch.BranchName,
    _domains_sample.SampleName
):
    pass


class SampleOfBranch(
    _domains_sample.SampleName, _domains_sample.SampleFile,
    _domains_sample.SampleDescription, _domains_sample.SampleOwner
):
    pass


class ReqSampleIn(
    _domains_branch.BranchName, _domains_branch.ReqSampleTo,
    _domains_branch.ReqSampleName, _domains_branch.ReqSampleStatus,
    _domains_branch.ReqSampleDeadLine
):
    pass
