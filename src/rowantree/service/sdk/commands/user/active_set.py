""" UserActiveSet Command Definition """
import requests
from requests import Response

from rowantree.contracts import UserActive

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

        response: Response = requests.post(
            url=f"{self.config.endpoint}/v1/user/{user_guid}/active",
            # TODO: In the future when this is the user object we will need to white list (or black list properties).
            data=request.json(by_alias=True, exclude={"state"}),
            headers=self.headers,
            timeout=self.config.timeout,
        )
        return UserActive.parse_obj(response.json())
