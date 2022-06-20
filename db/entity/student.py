from models.schemas import student as _schemas_student
from db.entity.base import BaseEntity
from pydantic import Field


class Student(BaseEntity, _schemas_student.StudentIn):
    gsi1pk: str = Field(None, min_length=2, alias='GSI1PK')
    gsi1sk: str = Field(None, min_length=2, alias='GSI1SK')

    def __init__(self, *args, **kwargs):
        super(Student, self).__init__(*args, **kwargs)
        self.pk = Student.get_pk(self.student_id)
        self.sk = Student.get_sk(self.student_id)
        self.pk, self.sk = Student.get_pk_sk(self.student_id)
        self.gsi1pk = Student.get_gsi1pk(self.branch_name)
        self.gsi1sk = Student.get_gsi1sk(self.branch_name)
        self.gsi1pk, self.gsi1sk = Student.get_gsi1pk_gsi1sk(self.branch_name)

    @staticmethod
    def get_pk(student_id: str):
        pk = f'STUDENT#{student_id}'
        return pk

    @staticmethod
    def get_sk(student_id: str):
        sk = f'STUDENT#{student_id}'
        return sk

    @staticmethod
    def get_pk_sk(student_id: str):
        pk = Student.get_pk(student_id)
        sk = Student.get_sk(student_id)
        return pk, sk

    @staticmethod
    def get_gsi1pk(branch_name: str):
        gsi1pk = f'BRANCH#{branch_name}'
        return gsi1pk

    @staticmethod
    def get_gsi1sk(branch_name: str):
        gsi1sk = f'BRANCH#{branch_name}'
        return gsi1sk

    @staticmethod
    def get_gsi1pk_gsi1sk(branch_name: str):
        gsi1pk = Student.get_gsi1pk(branch_name)
        gsi1sk = Student.get_gsi1sk(branch_name)
        return gsi1pk, gsi1sk

