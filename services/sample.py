from db.entity.sample import Sample
from utils import helpers
from models.schemas import sample as _sample_schema


def create_sample(simple_info: _sample_schema.SampleIn):
    item = Sample(**simple_info.dict(by_alias=True))
    return helpers.add_data([item])
