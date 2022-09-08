""" User Features Get Command Definition """

import requests
from requests import Response

from rowantree.contracts import UserFeatures

from ..abstract_command import AbstractCommand


class UserFeaturesGetCommand(AbstractCommand):
    """
    User Features Get Command
    Gets the unique list of user features.

    Methods
    -------
    execute(self, user_guid: str) -> UserFeatures
        Executes the command.
    """

    def execute(self, user_guid: str, headers: dict[str, str]) -> UserFeatures:
        """
        Executes the command.

        Parameters
        ----------
        user_guid: str
            The target user guid.

        Returns
        -------
        user_features: UserFeatures
            A unique list of user features.
        """

        response: Response = requests.get(
            url=f"{self.config.endpoint}/v1/user/{user_guid}/features",
            headers=headers,
            timeout=self.config.timeout,
        )
        return UserFeatures.parse_obj(response.json())
