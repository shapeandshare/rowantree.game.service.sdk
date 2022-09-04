import requests
from requests import Response

from ...contracts.responses.user.active_get import UserActiveGetResponse
from ..abstract_command import AbstractCommand


class UserActiveGetCommand(AbstractCommand):
    def execute(self, user_guid: str) -> UserActiveGetResponse:
        response: Response = requests.get(
            url=f"{self.config.endpoint}/v1/user/{user_guid}/active", headers=self.headers
        )
        return UserActiveGetResponse.parse_obj(response.json())
