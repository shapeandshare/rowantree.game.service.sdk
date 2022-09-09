from typing import Any, Optional

from pydantic import BaseModel

from ...contracts.request_verb import RequestVerb
from .request_status_codes import RequestStatusCodes


class WrappedRequest(BaseModel):
    verb: RequestVerb
    statuses: RequestStatusCodes
    url: str
    data: Optional[Any]  # str or dict ? - needs confirmation
    params: Optional[dict[str, str]]
