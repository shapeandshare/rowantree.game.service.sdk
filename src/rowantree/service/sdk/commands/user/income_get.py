""" User Income Get Command Definition """

from starlette import status

from rowantree.common.sdk import demand_env_var

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
    execute(self, user_guid: str) -> UserIncomeGetResponse
        Executes the command.
    """

    def execute(self, user_guid: str) -> UserIncomeGetResponse:
        """
        Executes the command.

        Parameters
        ----------
        user_guid: str
            The target user guid.

        Returns
        -------
        user_incomes: UserIncomeGetResponse
            A (unique) list of user incomes.
        """

        request: WrappedRequest = WrappedRequest(
            verb=RequestVerb.GET,
            url=f"{demand_env_var(name='ROWANTREE_SERVICE_ENDPOINT')}/v1/user/{user_guid}/income",
            statuses=RequestStatusCodes(allow=[status.HTTP_200_OK], reauth=[status.HTTP_401_UNAUTHORIZED], retry=[]),
        )
        response: dict = self.wrapped_request(request=request)
        return UserIncomeGetResponse.parse_obj(response)
