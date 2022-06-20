from db.entity.branch import ReqSample
from boto3.dynamodb.conditions import Key
from utils import core


def get_req_student(request):
    gsi1pk = ReqSample.get_gsi1pk(request.student_id)
    gsi1sk = ReqSample.get_gsi1sk(request.branch_name, request.sample_name)
    response = core.table.query(
        IndexName='GSI1',
        KeyConditionExpression=Key('GSI1PK').eq(gsi1pk)
        & Key('GSI1SK').eq(gsi1sk)
    ).get('Items', '')
    return response[0]