""" Action Queue Process Command Definition """

import requests
from starlette import status

from rowantree.common.sdk import demand_env_var, demand_env_var_as_float
from rowantree.contracts import ActionQueue

from .abstract_command import AbstractCommand, RequestStatusCodes, RequestVerb, WrappedRequest


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
            url=f"{demand_env_var(name='ROWANTREE_SERVICE_ENDPOINT')}/v1/world/queue",
            statuses=RequestStatusCodes(allow=[status.HTTP_200_OK], reauth=[status.HTTP_401_UNAUTHORIZED], retry=[]),
            data=request.json(by_alias=True),
        )
        self.wrapped_request(request=request)
