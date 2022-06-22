from utils import core
from fastapi import HTTPException


def request_sample_of_student(branch_request):
    try:
        core.table.put_item(
            Item=branch_request.dict(by_alias=True),
            ConditionExpression='attribute_not_exists(PK)'
        )
    except Exception:
        raise HTTPException(status_code=400, detail='Request failed')
    return branch_request
