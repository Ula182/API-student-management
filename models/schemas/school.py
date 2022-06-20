from models.domains import school as _domains_school


class SchoolIn(
    _domains_school.SchoolName, _domains_school.SchoolEmail,
    _domains_school.SchoolAddresses
):
    pass


class SchoolResp(SchoolIn):
    pass
