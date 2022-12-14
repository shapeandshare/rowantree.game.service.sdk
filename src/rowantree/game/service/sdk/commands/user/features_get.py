""" User Features Get Command Definition """
from typing import Optional

from starlette import status

from rowantree.contracts import FeatureType

from ...contracts.dto.request_status_codes import RequestStatusCodes
from ...contracts.dto.wrapped_request import WrappedRequest
from ...contracts.request_verb import RequestVerb
from ...contracts.responses.features_get import FeaturesGetResponse
from ..abstract_command import AbstractCommand


class UserFeaturesGetCommand(AbstractCommand):
    """
    User Features Get Command
    Gets the unique set of user features.

    Methods
    -------
    execute(self, user_guid: str) -> set[FeatureType]
        Executes the command.
    """

    def execute(self, user_guid: Optional[str] = None) -> set[FeatureType]:
        """
        Executes the command.

        Parameters
        ----------
        user_guid: str
            The target user guid.

        Returns
        -------
        user_features: set[FeatureType]
            A unique set of user features.
        """

        target_guid: str = self.demand_user_guid(user_guid=user_guid)

        request: WrappedRequest = WrappedRequest(
            verb=RequestVerb.GET,
            url=f"https://api/{self.options.tld}/game/v1/user/{target_guid}/features",
            statuses=RequestStatusCodes(allow=[status.HTTP_200_OK], reauth=[status.HTTP_401_UNAUTHORIZED], retry=[]),
        )
        response: dict = self.wrapped_request(request=request)
        features_get_response: FeaturesGetResponse = FeaturesGetResponse.parse_obj(response)
        return features_get_response.features
