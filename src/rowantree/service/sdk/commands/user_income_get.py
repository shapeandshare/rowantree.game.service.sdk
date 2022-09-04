import requests
from requests import Response

from ..contracts.responses.user.income_get import UserIncomeGetResponse
from .abstract_command import AbstractCommand


class UserIncomeGetCommand(AbstractCommand):
    def execute(self, user_guid: str) -> UserIncomeGetResponse:
        response: Response = requests.get(
            url=f"{self.config.endpoint}/v1/user/{user_guid}/income", headers=self.headers
        )
        return UserIncomeGetResponse.parse_obj(response.json())
