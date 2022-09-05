""" User Transport Command Definition """

import requests
from requests import Response

from rowantree.contracts import UserFeature

from ...contracts.requests.user.transport import UserTransportRequest
from ..abstract_command import AbstractCommand


class UserTransportCommand(AbstractCommand):
    """
    User Transport Command
    Performs a user transport. (feature to feature change)

    Methods
    -------
    execute(self, user_guid: str, request: UserTransportRequest) -> UserFeature
        Executes the command.
    """

    def execute(self, user_guid: str, request: UserTransportRequest) -> UserFeature:
        """
        Executes the command.

        Parameters
        ----------
        user_guid: str
            The target user guid.
        request: UserTransportRequest
            The UserTransportRequest to perform.

        Returns
        -------
        user_feature: UserFeature
            The user's new active feature.
        """

        response: Response = requests.post(
            url=f"{self.config.endpoint}/v1/user/{user_guid}/transport",
            data=request.json(by_alias=True),
            headers=self.headers,
            timeout=self.config.timeout,
        )
        return UserFeature.parse_obj(response.json())
