from utils import helpers, core
from fastapi import HTTPException


def resp_request_of_student(request):
    response_at = helpers.get_date_time()
    request.update({
        'File': 'upload_file.jpg',
        'ReSampleStatus': 'accept',
        'ResponseAt': response_at
    })
    core.table.put_item(
        Item=request
    )
    raise HTTPException(status_code=200, detail='OK')
