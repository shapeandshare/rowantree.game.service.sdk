import unittest

from rowantree.contracts import UserState

from src.rowantree.game.service.sdk import RowanTreeService


class TestService(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.client = RowanTreeService()

    def test_(self):
        # self.client.user_create()
        # self.client.user_active_set(active=True)
        # self.client.user_active_get()
        state: UserState = self.client.user_state_get()
        print(state)

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(TestService())
