from db.data.school.get_school_info import get_school_info
from db.entity.school import School, SchoolEmail
from fastapi import HTTPException
from utils import helpers, check_email_exist
from models.schemas import school as _school_schema


def create_school(school_info: _school_schema.SchoolIn):
    school_email = school_info.school_email
    if check_email_exist.check_email_exist(school_email):
        raise HTTPException(status_code=404, detail='Email already exists')
    
    school_dict = (school_info.dict(by_alias=True))
    school_email_db = SchoolEmail(**school_dict)
    school_info_db = School(**school_dict)

    list = [school_email_db, school_info_db]
    return helpers.add_data(list)
    

def get_school(school_name):
    return get_school_info(school_name)
