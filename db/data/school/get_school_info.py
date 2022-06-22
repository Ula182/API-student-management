from utils import core
from boto3.dynamodb.conditions import Key
from fastapi import HTTPException
from db.entity.school import School


def get_school_info(school_name: str) -> dict:
    pk, sk = School.get_pk_sk(school_name)
    response = core.table.query(
        KeyConditionExpression=Key("PK").eq(pk) & Key("SK").eq(sk)
    )
    items = response.get("Items", [])
    if not items:
        raise HTTPException(status_code=404, detail='Not Found')
    return items[0]
