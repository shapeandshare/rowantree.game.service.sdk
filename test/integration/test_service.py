import unittest

from src.rowantree.game.service.sdk import RowanTreeService


class TestService(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.client = RowanTreeService()

    def test_(self):
        self.client.user_create()
        # self.client.user_active_get()


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(TestService())
