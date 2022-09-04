import requests
from requests import Response

from ...contracts.responses.user.create import UserCreateResponse
from ..abstract_command import AbstractCommand


class UserCreateCommand(AbstractCommand):
    def execute(self) -> UserCreateResponse:
        response: Response = requests.post(url=f"{self.config.endpoint}/v1/user", headers=self.headers)
        return UserCreateResponse.parse_obj(response.json())
