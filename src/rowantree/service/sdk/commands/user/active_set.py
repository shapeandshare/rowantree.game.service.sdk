""" UserActiveSet Command Definition """

from starlette import status

from rowantree.common.sdk import demand_env_var
from rowantree.contracts import UserActive

from ...contracts.dto.request_status_codes import RequestStatusCodes
from ...contracts.dto.wrapped_request import WrappedRequest
from ...contracts.request_verb import RequestVerb
from ..abstract_command import AbstractCommand


class UserActiveSetCommand(AbstractCommand):
    """
    User Active Set Command
    Sets the user active state.

    Methods
    -------
    execute(self, user_guid: str, request: UserActive) -> UserActive
        Executes the command.
    """

    def execute(self, user_guid: str, request: UserActive) -> UserActive:
        """
        Executes the command.

        Parameters
        ----------
        user_guid: str
            The user guid to target.
        request: UserActive
            The active state to set the user to.

        Returns
        -------
        user_active: UserActive
            The state of the user.
        """

        request: WrappedRequest = WrappedRequest(
            verb=RequestVerb.POST,
            url=f"{demand_env_var(name='ROWANTREE_SERVICE_ENDPOINT')}/v1/user/{user_guid}/active",
            data=request.json(by_alias=True, exclude={"state"}),
            statuses=RequestStatusCodes(allow=[status.HTTP_200_OK], reauth=[status.HTTP_401_UNAUTHORIZED], retry=[]),
        )
        response: dict = self.wrapped_request(request=request)
        return UserActive.parse_obj(response)
