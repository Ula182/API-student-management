from models.domains import sample as _domains_sample


class SampleIn(
    _domains_sample.SampleOwner, _domains_sample.SampleName,
    _domains_sample.SampleFile, _domains_sample.SampleDescription
):
    pass


class SampleResp(SampleIn):
    pass
