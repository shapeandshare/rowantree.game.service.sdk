import requests
from requests import Response
from rowantree.contracts.dto.user.user import User

from ..abstract_command import AbstractCommand


class UserCreateCommand(AbstractCommand):
    def execute(self) -> User:
        response: Response = requests.post(url=f"{self.config.endpoint}/v1/user", headers=self.headers)
        return User.parse_obj(response.json())
