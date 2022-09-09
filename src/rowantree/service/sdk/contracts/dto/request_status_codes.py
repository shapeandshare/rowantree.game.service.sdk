from pydantic import BaseModel


class RequestStatusCodes(BaseModel):
    allow: list[int]
    retry: list[int]
    reauth: list[int]
