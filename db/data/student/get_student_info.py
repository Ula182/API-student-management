from utils import core
from fastapi import HTTPException
from boto3.dynamodb.conditions import Key
from db.entity.student import Student


def get_student(student_id: str):
    pk, sk = Student.get_pk_sk(student_id)
    response = core.table.query(
        KeyConditionExpression=Key('PK').eq(pk) & Key('SK').eq(sk)
    )
    items = response.get('Items', [])
    if not items:
        raise HTTPException(status_code=404, detail='Not Found')
    else:
        return items