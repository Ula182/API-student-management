from models.schemas import sample as _schemas_sample
from db.entity.base import BaseEntity


class Sample(BaseEntity, _schemas_sample.SampleIn):
    
    def __init__(self, *args, **kwargs):
        super(Sample, self).__init__(*args, **kwargs)
        self.pk = Sample.get_pk(self.sample_name)
        self.sk = Sample.get_sk(self.sample_name)
        self.pk, self.sk = Sample.get_pk_sk(self.sample_name)

    @staticmethod
    def get_pk(sample_name: str):
        pk = f'SAMPLE#{sample_name}'
        return pk

    @staticmethod
    def get_sk(sample_name: str):
        sk = f'SAMPLE#{sample_name}'
        return sk
    
    @staticmethod
    def get_pk_sk(sample_name: str):
        pk = Sample.get_pk(sample_name)
        sk = Sample.get_sk(sample_name)
        return pk, sk
