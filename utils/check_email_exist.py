from boto3.dynamodb.conditions import Key
from utils import core
from db.entity.school import SchoolEmail


def check_email_exist(school_email: str):
    email_pk, email_sk = SchoolEmail.get_pk_and_sk(school_email)
    email_res = core.table.query(
        KeyConditionExpression=Key('PK').eq(email_pk)
        & Key('SK').eq(email_sk)
    ).get('Items', [])
    return email_res