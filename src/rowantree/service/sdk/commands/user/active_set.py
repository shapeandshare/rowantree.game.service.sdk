import requests
from requests import Response
from rowantree.contracts import User, UserActive

from ..abstract_command import AbstractCommand


class UserActiveSetCommand(AbstractCommand):
    def execute(self, user_guid: str, request: UserActive) -> UserActive:
        response: Response = requests.post(
            url=f"{self.config.endpoint}/v1/user/{user_guid}/active",
            data=request.json(by_alias=True, exclude={"state"}),
            headers=self.headers,
        )
        return UserActive.parse_obj(response.json())
