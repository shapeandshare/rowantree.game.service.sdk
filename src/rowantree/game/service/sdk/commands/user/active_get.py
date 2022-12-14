""" UserActiveGet Command Definition """
from typing import Optional

from starlette import status

from ...contracts.dto.request_status_codes import RequestStatusCodes
from ...contracts.dto.wrapped_request import WrappedRequest
from ...contracts.request_verb import RequestVerb
from ...contracts.user_active_status import UserActiveGetStatus
from ..abstract_command import AbstractCommand


class UserActiveGetCommand(AbstractCommand):
    """
    User Active Get Command
    Gets the user active state.

    Methods
    -------
    execute(self, user_guid: str) -> UserActiveGetStatus
        Executes the command.
    """

    def execute(self, user_guid: Optional[str] = None) -> UserActiveGetStatus:
        """
        Executes the command.

        Parameters
        ----------
        user_guid: str
            The user guid to look up.

        Returns
        -------
        user_active: UserActiveGetStatus
            The user active state object.
        """

        target_guid: str = self.demand_user_guid(user_guid=user_guid)

        request: WrappedRequest = WrappedRequest(
            verb=RequestVerb.GET,
            url=f"https://api.{self.options.tld}/game/v1/user/{target_guid}/active",
            statuses=RequestStatusCodes(allow=[status.HTTP_200_OK], reauth=[status.HTTP_401_UNAUTHORIZED], retry=[]),
        )
        response: dict = self.wrapped_request(request=request)
        return UserActiveGetStatus.parse_obj(response)
