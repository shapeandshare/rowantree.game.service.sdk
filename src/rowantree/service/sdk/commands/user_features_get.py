import requests
from requests import Response

from ..contracts.responses.user.features_get import UserFeaturesGetResponse
from .abstract_command import AbstractCommand


class UserFeaturesGetCommand(AbstractCommand):
    def execute(self, user_guid: str) -> UserFeaturesGetResponse:
        response: Response = requests.get(
            url=f"{self.config.endpoint}/v1/user/{user_guid}/features", headers=self.headers
        )
        return UserFeaturesGetResponse.parse_obj(response.json())
