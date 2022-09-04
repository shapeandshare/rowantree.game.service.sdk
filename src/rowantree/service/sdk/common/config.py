import configparser
import os
from typing import Optional

from pydantic import BaseModel


class Config(BaseModel):
    access_key: Optional[str]
    endpoint: Optional[str]

    def __init__(self, config_file_path: str = "rowantree.config", *args, **kwargs):
        super().__init__(*args, **kwargs)
        config = configparser.ConfigParser()
        config.read(config_file_path)

        # Server Options
        self.access_key = config.get("SERVER", "access_key")
        self.endpoint = config.get("SERVER", "endpoint")

        if "ACCESS_KEY" in os.environ:
            self.access_key = os.environ["ACCESS_KEY"]

        if "ROWANTREE_SERVICE_ENDPOINT" in os.environ:
            self.endpoint = os.environ["ROWANTREE_SERVICE_ENDPOINT"]
