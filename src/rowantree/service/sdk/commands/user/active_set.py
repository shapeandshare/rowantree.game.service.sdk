import requests
from requests import Response
from rowantree.contracts.dto.user.user import User

from ..abstract_command import AbstractCommand


class UserActiveSetCommand(AbstractCommand):
    def execute(self, user_guid: str, request: User) -> User:
        response: Response = requests.post(
            url=f"{self.config.endpoint}/v1/user/{user_guid}/active",
            data=request.json(by_alias=True, exclude={"state"}),
            headers=self.headers,
        )
        return User.parse_obj(response.json())
