from utils import core
from boto3.dynamodb.conditions import Key
from db.entity.branch import Branch
from fastapi import HTTPException


def get_branch(school_name: str):
    pk = Branch.get_pk(school_name)
    sk_prefix = 'BRANCH#'
    response = core.table.query(
        KeyConditionExpression=Key('PK').eq(pk)
        & Key('SK').begins_with(sk_prefix)
    )
    items = response.get('Items', [])
    if not items:
        raise HTTPException(status_code=404, detail='Not Found')
    return items