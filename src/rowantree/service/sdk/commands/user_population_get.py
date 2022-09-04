import requests
from requests import Response

from ..contracts.responses.user.population_get import UserPopulationGetResponse
from .abstract_command import AbstractCommand


class UserPopulationGetCommand(AbstractCommand):
    def execute(self, user_guid: str) -> UserPopulationGetResponse:
        response: Response = requests.post(
            url=f"{self.config.endpoint}/v1/user/{user_guid}/population", headers=self.headers
        )
        return UserPopulationGetResponse.parse_obj(response.json())
