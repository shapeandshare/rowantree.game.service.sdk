import requests
from requests import Response
from rowantree.contracts.dto.user.population import UserPopulation

from ..abstract_command import AbstractCommand


class UserPopulationGetCommand(AbstractCommand):
    def execute(self, user_guid: str) -> UserPopulation:
        response: Response = requests.post(
            url=f"{self.config.endpoint}/v1/user/{user_guid}/population", headers=self.headers
        )
        return UserPopulation.parse_obj(response.json())
