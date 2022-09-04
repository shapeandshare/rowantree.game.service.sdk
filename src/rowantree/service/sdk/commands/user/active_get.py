import requests
from requests import Response
from rowantree.contracts.dto.user.active import UserActive

from ..abstract_command import AbstractCommand


class UserActiveGetCommand(AbstractCommand):
    def execute(self, user_guid: str) -> UserActive:
        response: Response = requests.get(
            url=f"{self.config.endpoint}/v1/user/{user_guid}/active", headers=self.headers
        )
        return UserActive.parse_obj(response.json())
