""" User Population Get Command Definition """

from starlette import status

from rowantree.common.sdk import demand_env_var
from rowantree.contracts import UserPopulation

from ..abstract_command import AbstractCommand, RequestStatusCodes, RequestVerb, WrappedRequest


class UserPopulationGetCommand(AbstractCommand):
    """
    User Population Get Command
    Gets the user population.

    Methods
    -------
    execute(self, user_guid: str) -> UserPopulation
        Executes the command.
    """

    def execute(self, user_guid: str) -> UserPopulation:
        """
        Executes the command.

        Parameters
        ----------
        user_guid: str
            The target user guid.

        Returns
        -------
        user_population: UserPopulation
            User population object.
        """

        request: WrappedRequest = WrappedRequest(
            verb=RequestVerb.GET,
            url=f"{demand_env_var(name='ROWANTREE_SERVICE_ENDPOINT')}/v1/user/{user_guid}/population",
            statuses=RequestStatusCodes(allow=[status.HTTP_200_OK], reauth=[status.HTTP_401_UNAUTHORIZED], retry=[]),
        )
        response: dict = self.wrapped_request(request=request)
        return UserPopulation.parse_obj(response)
