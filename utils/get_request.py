from db.entity.branch import ReqSample
from boto3.dynamodb.conditions import Key
from utils import core
from models.schemas import student as _student_schema


def get_req_student(request: _student_schema.StudentRespReqIn) -> dict:
    gsi1pk, gsi1sk = ReqSample.get_gsi1pk_gsi1sk(
        request.student_id,
        request.branch_name,
        request.sample_name
    )
    response = core.table.query(
        IndexName='GSI1',
        KeyConditionExpression=Key('GSI1PK').eq(gsi1pk)
        & Key('GSI1SK').eq(gsi1sk)
    ).get('Items', '')
    return response[0]
