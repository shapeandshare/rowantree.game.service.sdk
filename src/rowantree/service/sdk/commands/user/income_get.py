import requests
from requests import Response
from rowantree.contracts.dto.user.incomes import UserIncomes

from ..abstract_command import AbstractCommand


class UserIncomeGetCommand(AbstractCommand):
    def execute(self, user_guid: str) -> UserIncomes:
        response: Response = requests.get(
            url=f"{self.config.endpoint}/v1/user/{user_guid}/income", headers=self.headers
        )
        return UserIncomes.parse_obj(response.json())
