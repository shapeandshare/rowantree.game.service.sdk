import requests
from requests import Response

from rowantree.contracts.dto.user.state import UserState

from ..abstract_command import AbstractCommand


class UserStateGetCommand(AbstractCommand):
    def execute(self, user_guid: str) -> UserState:
        response: Response = requests.get(url=f"{self.config.endpoint}/v1/user/{user_guid}/state", headers=self.headers)
        return UserState.parse_obj(response.json())
