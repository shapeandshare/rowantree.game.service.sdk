""" Health Get Command Definition """

import requests
from requests import Response

from .abstract_command import AbstractCommand


class HealthGetCommand(AbstractCommand):
    """
    Health Get Command
    Gets the server health.

    Methods
    -------
    execute(self) -> bool
        Executes the command.
    """

    def execute(self) -> bool:
        """
        Executes the command.

        Returns
        -------
        health: bool
            The server health (true or false).
        """

        response: Response = requests.get(url=f"{self.config.endpoint}/health/plain", timeout=self.config.timeout)
        return bool(response.text)
