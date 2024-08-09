from api.base_api import BaseAPI


class RepositoriesAPI(BaseAPI):
    def __init__(self, base_url):
        super().__init__(base_url)

    def get_repositories(self, user):
        return self.get(f"/users/{user}/repos")
