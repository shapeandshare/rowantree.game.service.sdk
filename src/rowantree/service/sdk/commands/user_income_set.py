import requests
from requests import Response

from ..contracts.requests.user_income_set import UserIncomeSetRequest
from .abstract_command import AbstractCommand


class UserIncomeSetCommand(AbstractCommand):
    def execute(self, user_guid: str, request: UserIncomeSetRequest) -> None:
        requests.post(
            url=f"{self.config.endpoint}/v1/user/{user_guid}/income",
            data=request.json(by_alias=True),
            headers=self.headers,
        )
