from models.schemas import school as _schemas_school
from db.entity.base import BaseEntity


class School(BaseEntity, _schemas_school.SchoolIn):

    def __init__(self, *args, **kwargs):
        super(School, self).__init__(*args, **kwargs)
        self.pk = School.get_pk(self.school_name)
        self.sk = School.get_sk(self.school_name)
        self.pk, self.sk = School.get_pk_sk(self.school_name)

    @staticmethod
    def get_pk(school_name: str):
        pk = f'SCHOOL#{school_name}'
        return pk

    @staticmethod
    def get_sk(school_name: str):
        sk = f'SCHOOL#{school_name}'
        return sk

    @staticmethod
    def get_pk_sk(school_name: str):
        pk = School.get_pk(school_name)
        sk = School.get_sk(school_name)
        return pk, sk


class SchoolEmail(BaseEntity, _schemas_school.SchoolIn):

    def __init__(self, *args, **kwargs):
        super(SchoolEmail, self).__init__(*args, **kwargs)
        self.pk = SchoolEmail.get_pk(self.school_email)
        self.sk = SchoolEmail.get_sk(self.school_email)
        self.pk, self.sk = SchoolEmail.get_pk_and_sk(self.school_email)

    @staticmethod
    def get_pk(school_email: str):
        pk = f'SCHOOLEMAIL#{school_email}'
        return pk

    @staticmethod
    def get_sk(school_email: str):
        sk = f'SCHOOLEMAIL#{school_email}'
        return sk

    @staticmethod
    def get_pk_and_sk(school_email: str):
        pk = SchoolEmail.get_pk(school_email)
        sk = SchoolEmail.get_sk(school_email)
        return pk, sk
