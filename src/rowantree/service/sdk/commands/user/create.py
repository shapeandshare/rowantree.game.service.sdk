""" User Create Command Definition """

from starlette import status

from rowantree.common.sdk import demand_env_var
from rowantree.contracts import User

from ..abstract_command import AbstractCommand, RequestStatusCodes, RequestVerb, WrappedRequest


class UserCreateCommand(AbstractCommand):
    """
    User Create Command
    Creates a user.

    Methods
    -------
    execute(self) -> User
        Executes the command.
    """

    def execute(self, user_guid: str) -> User:
        """
        Executes the command.

        Parameters
        ----------
        user_guid: str

        Returns
        -------
        user: User
            The newly created user.
        """
        request: WrappedRequest = WrappedRequest(
            verb=RequestVerb.POST,
            url=f"{demand_env_var(name='ROWANTREE_SERVICE_ENDPOINT')}/v1/user/{user_guid}",
            statuses=RequestStatusCodes(
                allow=[status.HTTP_201_CREATED], reauth=[status.HTTP_401_UNAUTHORIZED], retry=[]
            ),
        )
        response: dict = self.wrapped_request(request=request)
        return User.parse_obj(response)
