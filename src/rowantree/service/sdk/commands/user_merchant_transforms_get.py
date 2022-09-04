import requests
from requests import Response

from ..contracts.responses.user_merchant_transforms_get import UserMerchantTransformsGetResponse
from .abstract_command import AbstractCommand


class UserMerchantTransformsGetCommand(AbstractCommand):
    def execute(self, user_guid: str) -> UserMerchantTransformsGetResponse:
        response: Response = requests.get(
            url=f"{self.config.endpoint}/v1/user/{user_guid}/merchant", headers=self.headers
        )
        return UserMerchantTransformsGetResponse.parse_obj(response.json())
