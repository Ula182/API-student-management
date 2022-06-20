from db.entity.sample import Sample
from utils import helpers


def create_sample(simple_info):
    item = Sample(**simple_info.dict(by_alias=True))
    return helpers.add_data(item.dict(by_alias=True))
