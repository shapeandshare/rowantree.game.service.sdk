""" Merchant Transforms Perform Command Definition """

from starlette import status

from ..contracts.dto.request_status_codes import RequestStatusCodes
from ..contracts.dto.wrapped_request import WrappedRequest
from ..contracts.request_verb import RequestVerb
from ..contracts.requests.merchant_transform import MerchantTransformRequest
from .abstract_command import AbstractCommand


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
        user_guid
        request: MerchantTransformRequest
            The merchant transform request.
        """

        request: WrappedRequest = WrappedRequest(
            verb=RequestVerb.POST,
            url=f"https://api.{self.options.tld}/game/v1/user/{user_guid}/merchant",
            statuses=RequestStatusCodes(allow=[status.HTTP_200_OK], reauth=[status.HTTP_401_UNAUTHORIZED], retry=[]),
            data=request.json(by_alias=True),
        )
        self.wrapped_request(request=request)
