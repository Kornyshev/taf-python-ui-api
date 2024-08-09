from api.base_api import BaseAPI


class UsersAPI(BaseAPI):
    def __init__(self, base_url):
        super().__init__(base_url)

    def get_user(self, username):
        return self.get(f"/users/{username}")
