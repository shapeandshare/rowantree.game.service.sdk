import requests
from requests import Response

from ..contracts.responses.user_stores_get_response import UserStoresGetResponse
from .abstract_command import AbstractCommand


class UserStoresGetCommand(AbstractCommand):
    def execute(self, user_guid: str) -> UserStoresGetResponse:
        response: Response = requests.get(
            url=f"{self.config.endpoint}/v1/user/{user_guid}/stores", headers=self.headers
        )
        return UserStoresGetResponse.parse_obj(response.json())
