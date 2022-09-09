""" User Merchant Transforms Get Command Definition """

from starlette import status

from rowantree.common.sdk import demand_env_var
from rowantree.contracts import UserMerchants

from ..abstract_command import AbstractCommand, RequestStatusCodes, RequestVerb, WrappedRequest


class UserMerchantTransformsGetCommand(AbstractCommand):
    """
    User Merchant Transforms Get Command
    Gets a (unique) list of user merchant transforms.

    Methods
    -------
    execute(self, user_guid: str) -> UserMerchants
        Executes the command.
    """

    def execute(self, user_guid: str) -> UserMerchants:
        """
        Executes the command.

        Parameters
        ----------
        user_guid: str
            Target user guid.

        Returns
        -------
        user_merchants: UserMerchants
            A (unique) list of user merchant transforms.
        """

        request: WrappedRequest = WrappedRequest(
            verb=RequestVerb.GET,
            url=f"{demand_env_var(name='ROWANTREE_SERVICE_ENDPOINT')}/v1/user/{user_guid}/merchant",
            statuses=RequestStatusCodes(allow=[status.HTTP_200_OK], reauth=[status.HTTP_401_UNAUTHORIZED], retry=[]),
        )
        response: dict = self.wrapped_request(request=request)
        return UserMerchants.parse_obj(response)
