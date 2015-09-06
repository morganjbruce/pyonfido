import defaults
from resources import ApiResource


class Checks(ApiResource):
    def create(self, applicant_id, check_details):
        return self.post("applicants/{0}/checks".format(applicant_id),
                         check_details)

    def find(self, applicant_id, check_id):
        return self.get("applicants/{0}/checks/{1}".format(applicant_id,
                        check_id))

    def all(self, applicant_id, page=defaults.page,
            per_page=defaults.per_page):

        params = {
            "page": page,
            "per_page": per_page
        }

        return self.get("applicants/{0}/checks".format(applicant_id), params)
