from utils import core
from boto3.dynamodb.conditions import Key
from db.entity.add_sample import AddSample
from db.entity.sample import Sample
from fastapi import HTTPException
from typing import List


def get_sample_of_branch(branch_name) -> List:
    pk = AddSample.get_pk(branch_name)
    response = core.table.query(
        KeyConditionExpression=Key('PK').eq(pk)
    )
    items = response.get('Items', [])
    resp_items = []
    for item in items:
        pk = Sample.get_pk(item.get('SampleName'))
        response = core.table.query(
            KeyConditionExpression=Key('PK').eq(pk)
        ).get('Items', [])
        if response:
            resp_items.append(response[0])
    if not resp_items:
        raise HTTPException(status_code=404, detail='Not Found')
    return resp_items