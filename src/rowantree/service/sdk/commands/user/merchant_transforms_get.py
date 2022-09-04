import requests
from requests import Response
from rowantree.contracts.dto.user.merchants import UserMerchants

from ..abstract_command import AbstractCommand


class UserMerchantTransformsGetCommand(AbstractCommand):
    def execute(self, user_guid: str) -> UserMerchants:
        response: Response = requests.get(
            url=f"{self.config.endpoint}/v1/user/{user_guid}/merchant", headers=self.headers
        )
        return UserMerchants.parse_obj(response.json())
