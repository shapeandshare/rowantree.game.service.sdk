import requests
from requests import Response
from rowantree.contracts.dto.user.stores import UserStores

from ..abstract_command import AbstractCommand


class UserStoresGetCommand(AbstractCommand):
    def execute(self, user_guid: str) -> UserStores:
        response: Response = requests.get(
            url=f"{self.config.endpoint}/v1/user/{user_guid}/stores", headers=self.headers
        )
        return UserStores.parse_obj(response.json())
