""" User State Get Command Definition """

import requests
from requests import Response

from rowantree.contracts import UserState

from ..abstract_command import AbstractCommand


class UserStateGetCommand(AbstractCommand):
    """
    User State Get Command
    Gets the user game state.

    Methods
    -------
    execute(self, user_guid: str) -> UserState
        Executes the command.
    """

    def execute(self, user_guid: str) -> UserState:
        """
        Executes the command.

        Parameters
        ----------
        user_guid: str
            The target user guid.

        Returns
        -------
        user_state: UserState
            The user state object.
        """

        response: Response = requests.get(
            url=f"{self.config.endpoint}/v1/user/{user_guid}/state", headers=self.headers, timeout=self.config.timeout
        )
        return UserState.parse_obj(response.json())
