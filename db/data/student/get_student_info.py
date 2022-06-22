from utils import core
from fastapi import HTTPException
from boto3.dynamodb.conditions import Key
from db.entity.student import Student


def get_student_info(student_id: str) -> dict:
    pk, sk = Student.get_pk_sk(student_id)
    response = core.table.query(
        KeyConditionExpression=Key('PK').eq(pk) & Key('SK').eq(sk)
    )
    items = response.get('Items', [])
    if not items:
        raise HTTPException(status_code=404, detail='Not Found')
    return items[0]