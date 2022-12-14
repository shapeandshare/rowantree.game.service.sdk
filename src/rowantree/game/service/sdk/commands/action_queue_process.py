""" Action Queue Process Command Definition """

from starlette import status

from rowantree.contracts import ActionQueue

from ..contracts.dto.request_status_codes import RequestStatusCodes
from ..contracts.dto.wrapped_request import WrappedRequest
from ..contracts.request_verb import RequestVerb
from .abstract_command import AbstractCommand


class ActionQueueProcessCommand(AbstractCommand):
    """
    Action Queue Process Command
    Processes an action queue.

    Methods
    -------
    execute(self, request: ActionQueue) -> None
        Executes the command.
    """

    def execute(self, request: ActionQueue) -> None:
        """
        Executes the command.

        Parameters
        ----------
        request: ActionQueue
            The action queue to process.
        """

        request: WrappedRequest = WrappedRequest(
            verb=RequestVerb.POST,
            url=f"https://api.{self.options.tld}/game/v1/world/queue",
            statuses=RequestStatusCodes(allow=[status.HTTP_200_OK], reauth=[status.HTTP_401_UNAUTHORIZED], retry=[]),
            data=request.dict(by_alias=True),
        )
        self.wrapped_request(request=request)
