""" User Income Get Command Definition """
from typing import Optional

from starlette import status

from rowantree.contracts import IncomeSourceType, UserIncome

from ...contracts.dto.request_status_codes import RequestStatusCodes
from ...contracts.dto.wrapped_request import WrappedRequest
from ...contracts.request_verb import RequestVerb
from ...contracts.responses.income_get import UserIncomeGetResponse
from ..abstract_command import AbstractCommand


class UserIncomeGetCommand(AbstractCommand):
    """
    User Income Get Command
    Gets (unique) list of user incomes.

    Methods
    -------
    execute(self, user_guid: str) -> dict[IncomeSourceType, UserIncome]
        Executes the command.
    """

    def execute(self, user_guid: Optional[str] = None) -> dict[IncomeSourceType, UserIncome]:
        """
        Executes the command.

        Parameters
        ----------
        user_guid: str
            The target user guid.

        Returns
        -------
        user_incomes: dict[IncomeSourceType, UserIncome]
        """

        target_guid: str = self.demand_user_guid(user_guid=user_guid)

        request: WrappedRequest = WrappedRequest(
            verb=RequestVerb.GET,
            url=f"https://api.{self.options.tld}/game/v1/user/{target_guid}/income",
            statuses=RequestStatusCodes(allow=[status.HTTP_200_OK], reauth=[status.HTTP_401_UNAUTHORIZED], retry=[]),
        )
        response: dict = self.wrapped_request(request=request)
        user_income_get_response: UserIncomeGetResponse = UserIncomeGetResponse.parse_obj(response)
        return user_income_get_response.incomes
