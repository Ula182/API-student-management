from datetime import datetime
from ksuid import Ksuid
from typing import Optional
from utils import core
from fastapi import HTTPException


def add_data(item):
    try:
        core.table.put_item(
            Item=item,
            ConditionExpression='attribute_not_exists(PK)'
        )
    except Exception:
        raise HTTPException(status_code=400, detail='Not Create')


def add_data_sk(item):
    try:
        core.table.put_item(
            Item=item,
            ConditionExpression='attribute_not_exists(SK)'
        )
        raise HTTPException(status_code=400, detail='Create')
    except Exception:
        raise HTTPException(status_code=400, detail='Not Create')


def get_date_time():
    now_iso = datetime.now().isoformat()
    return now_iso
    
    
def generate_request_id(date: Optional[datetime] = None) -> str:
    if date is None:
        date = datetime.now()
    kid = str(Ksuid(date))
    return kid

