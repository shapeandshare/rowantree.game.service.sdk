""" User Feature Active Get Command """

import requests
from requests import Response

from rowantree.contracts import UserFeature

from ..abstract_command import AbstractCommand


class UserFeatureActiveGetCommand(AbstractCommand):
    """
    User Feature Active Get Command
    Gets the active user feature.

    Methods
    -------
    execute(self, user_guid: str, details: bool) -> UserFeature
        Executes the command.
    """

    def execute(self, user_guid: str, details: bool) -> UserFeature:
        """
        Executes the command.

        Parameters
        ----------
        user_guid: str
            The target user guid.
        details: bool
            Whether to include details of the feature.

        Returns
        -------
        user_feature: UserFeature
            The active UserFeature.
        """

        response: Response = requests.get(
            url=f"{self.config.endpoint}/v1/user/{user_guid}/features/active",
            params={"details": details},
            headers=self.headers,
            timeout=self.config.timeout,
        )
        return UserFeature.parse_obj(response.json())
