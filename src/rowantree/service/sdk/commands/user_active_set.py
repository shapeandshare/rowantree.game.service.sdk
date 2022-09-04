import requests
from requests import Response

from ..contracts.requests.user_active_set_request import UserActiveSetRequest
from .abstract_command import AbstractCommand


class UserActiveSetCommand(AbstractCommand):
    def execute(self, user_guid: str, request: UserActiveSetRequest) -> UserActiveSetRequest:
        response: Response = requests.post(
            url=f"{self.config.endpoint}/v1/user/{user_guid}/active",
            data=request.json(by_alias=True),
            headers=self.headers,
        )
        return UserActiveSetRequest.parse_obj(response.json())
