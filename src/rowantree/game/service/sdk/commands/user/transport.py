""" User Transport Command Definition """
from typing import Optional

from starlette import status

from rowantree.contracts import UserFeatureState

from ...contracts.dto.request_status_codes import RequestStatusCodes
from ...contracts.dto.wrapped_request import WrappedRequest
from ...contracts.request_verb import RequestVerb
from ...contracts.requests.user.transport import UserTransportRequest
from ..abstract_command import AbstractCommand


class UserTransportCommand(AbstractCommand):
    """
    User Transport Command
    Performs a user transport. (feature to feature change)

    Methods
    -------
    execute(self, user_guid: str, request: UserTransportRequest) -> UserFeatureState
        Executes the command.
    """

    def execute(self, request: UserTransportRequest, user_guid: Optional[str] = None) -> UserFeatureState:
        """
        Executes the command.

        Parameters
        ----------
        user_guid
        request: UserTransportRequest
            The UserTransportRequest to perform.

        Returns
        -------
        feature_state: UserFeatureState
            The user's new active feature state.
        """

        target_guid: str = self.demand_user_guid(user_guid=user_guid)

        request: WrappedRequest = WrappedRequest(
            verb=RequestVerb.POST,
            url=f"https://api.{self.options.tld}/game/v1/user/{target_guid}/transport",
            statuses=RequestStatusCodes(allow=[status.HTTP_200_OK], reauth=[status.HTTP_401_UNAUTHORIZED], retry=[]),
            data=request.dict(by_alias=True),
        )
        response: dict = self.wrapped_request(request=request)
        return UserFeatureState.parse_obj(response)
