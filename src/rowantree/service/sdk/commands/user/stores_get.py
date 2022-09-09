""" User Stores Get Command Definition """

import requests
from requests import Response
from starlette import status

from rowantree.common.sdk import demand_env_var, demand_env_var_as_float
from rowantree.contracts import UserStores

from ..abstract_command import AbstractCommand, RequestStatusCodes, RequestVerb, WrappedRequest


class UserStoresGetCommand(AbstractCommand):
    """
    User Stores Get Command
    Gets the (unique) list of user stores.

    Methods
    -------
    execute(self, user_guid: str) -> UserStores
        Executes the command.
    """

    def execute(self, user_guid: str) -> UserStores:
        """
        Gets the (unique) list of user stores.

        Parameters
        ----------
        user_guid: str
            The target user guid.

        Returns
        -------
        user_stores: UserStores
            A (unique) list of user stores.
        """

        request: WrappedRequest = WrappedRequest(
            verb=RequestVerb.GET,
            url=f"{demand_env_var(name='ROWANTREE_SERVICE_ENDPOINT')}/v1/user/{user_guid}/stores",
            statuses=RequestStatusCodes(allow=[status.HTTP_200_OK], reauth=[status.HTTP_401_UNAUTHORIZED], retry=[]),
        )
        response: dict = self.wrapped_request(request=request)
        return UserStores.parse_obj(response)
