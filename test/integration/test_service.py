import unittest

from src.rowantree.game.service.sdk import RowanTreeService


class TestService(unittest.TestCase):
    def test_(self):

        client = RowanTreeService()
        client.user_active_get()


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(TestService())
