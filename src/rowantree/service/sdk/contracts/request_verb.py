from enum import Enum


class RequestVerb(str, Enum):
    GET = "GET"
    POST = "POST"
    DELETE = "DELETE"
