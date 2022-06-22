from utils import core
from boto3.dynamodb.conditions import Key
from db.entity.student import Student
from fastapi import HTTPException
from typing import List


def get_student_info_branch(branch_name: str) -> List:
    gsi1pk, gsi1sk = Student.get_gsi1pk_gsi1sk(branch_name)
    response = core.table.query(
        IndexName='GSI1',
        KeyConditionExpression=Key('GSI1PK').eq(gsi1pk)
        & Key('GSI1SK').eq(gsi1sk)
    )
    items = response.get('Items', [])
    if not items:
        raise HTTPException(status_code=404, detail='Not Found')
    return items