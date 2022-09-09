""" Merchant Transforms Perform Command Definition """

import requests
from starlette import status

from rowantree.common.sdk import demand_env_var, demand_env_var_as_float

from ..contracts.requests.merchant_transform import MerchantTransformRequest
from .abstract_command import AbstractCommand, RequestStatusCodes, RequestVerb, WrappedRequest


class MerchantTransformPerformCommand(AbstractCommand):
    """
    Merchant Transform Perform Command
    Performs a merchant transform.

    Methods
    -------
    execute(self, user_guid: str, request: MerchantTransformRequest) -> None
        Executes the command.
    """

    def execute(self, user_guid: str, request: MerchantTransformRequest) -> None:
        """
        Executes the command.

        Parameters
        ----------
        user_guid: str
            The target user guid.
        request: MerchantTransformRequest
            The merchant transform request.
        """

        request: WrappedRequest = WrappedRequest(
            verb=RequestVerb.POST,
            url=f"{demand_env_var(name='ROWANTREE_SERVICE_ENDPOINT')}/v1/user/{user_guid}/merchant",
            statuses=RequestStatusCodes(allow=[status.HTTP_200_OK], reauth=[status.HTTP_401_UNAUTHORIZED], retry=[]),
            data=request.json(by_alias=True),
        )
        self.wrapped_request(request=request)
