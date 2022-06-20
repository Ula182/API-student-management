from models.schemas import branch as _schemas_branch
from db.entity.base import BaseEntity


class AddSample(BaseEntity, _schemas_branch.AddSample):

    def __init__(self, *args, **kwargs):
        super(AddSample, self).__init__(*args, **kwargs)
        self.pk = AddSample.get_pk(self.branch_name)
        self.sk = AddSample.get_sk(self.sample_name)
        self.pk, self.sk = AddSample.get_pk_and_sk(
            self.branch_name, self.sample_name)

    @ staticmethod
    def get_pk(branch_name: str):
        pk = f'BRANCH#{branch_name}'
        return pk

    @ staticmethod
    def get_sk(sample_name: str):
        sk = f'SAMPLE#{sample_name}'
        return sk

    @ staticmethod
    def get_pk_and_sk(branch_name: str, sample_name: str):
        pk = AddSample.get_pk(branch_name)
        sk = AddSample.get_sk(sample_name)
        return pk, sk
