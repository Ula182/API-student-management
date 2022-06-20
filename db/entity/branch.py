from models.schemas import branch as _schemas_branch
from db.entity.base import (
    BaseEntity, BaseEntityCreatedAt,
    BaseEntityRequestId, BaseEntityFile
)
from pydantic import Field


class Branch(BaseEntity, _schemas_branch.BranchIn):

    def __init__(self, *args, **kwargs):
        super(Branch, self).__init__(*args, **kwargs)
        self.pk = Branch.get_pk(self.school_name)
        self.sk = Branch.get_sk(self.branch_name)
        self.pk, self.sk = Branch.get_pk_sk(self.branch_name)

    @staticmethod
    def get_pk(school_name: str):
        pk = f'SCHOOL#{school_name}'
        return pk

    @staticmethod
    def get_sk(branch_name: str):
        sk = f'BRANCH#{branch_name}'
        return sk

    @staticmethod
    def get_pk_sk(branch_name: str):
        pk = Branch.get_pk(branch_name)
        sk = Branch.get_sk(branch_name)
        return pk, sk


class ReqSample(
    BaseEntityCreatedAt, BaseEntityRequestId,
    BaseEntityFile,
    BaseEntity, _schemas_branch.ReqSampleIn
):
    gsi1pk: str = Field(None, min_length=2, alias='GSI1PK')
    gsi1sk: str = Field(None, min_length=2, alias='GSI1SK')

    def __init__(self, *args, **kwargs):
        super(ReqSample, self).__init__(*args, **kwargs)
        self.pk = ReqSample.get_pk(self.branch_name, self.sample_name)
        self.sk = ReqSample.get_sk(self.request_to, self.request_id)
        self.pk, self.sk = ReqSample.get_pk_sk(
            self.branch_name, self.sample_name,
            self.request_to, self.request_id
        )
        self.gsi1pk = ReqSample.get_gsi1pk(self.request_to)
        self.gsi1sk = ReqSample.get_gsi1sk(self.branch_name, self.sample_name)
        self.gsi1pk, self.gsi1sk = ReqSample.get_gsi1pk_gsi1sk(
            self.request_to,
            self.branch_name,
            self.sample_name
        )

    @staticmethod
    def get_pk(branch_name: str, sample_name: str):
        pk = f'BRANCH#{branch_name}#SAMPLE#{sample_name}'
        return pk

    @staticmethod
    def get_sk(request_to: str, request_id: str):
        sk = f'STUDENT#{request_to}#REQUEST#{request_id}'
        return sk

    @staticmethod
    def get_pk_sk(
        branch_name: str, sample_name: str,
        request_to: str, request_id: str
    ):
        pk = ReqSample.get_pk(branch_name, sample_name)
        sk = ReqSample.get_sk(request_to, request_id)
        return pk, sk

    @staticmethod
    def get_gsi1pk(request_to: str):
        gsi1pk = f'STUDENT#{request_to}'
        return gsi1pk

    @staticmethod
    def get_gsi1sk(branch_name: str, sample_name: str):
        gsi1sk = f'BRANCH#{branch_name}#SAMPLE#{sample_name}'
        return gsi1sk

    @staticmethod
    def get_gsi1pk_gsi1sk(request_to: str, branch_name: str, sample_name: str):
        gsi1pk = ReqSample.get_gsi1pk(request_to)
        gsi1sk = ReqSample.get_gsi1sk(branch_name, sample_name)
        return gsi1pk, gsi1sk
