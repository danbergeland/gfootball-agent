import unittest
from src.agent import RandomAgent

_action_space = 14

class TestAgent(unittest.TestCase):    
    def test_exists(self):
        test_agent = RandomAgent(_action_space)
        self.assertIsNotNone(test_agent)

    def test_get_action_is_in_action_space(self):
        TestAgent = RandomAgent(_action_space)
        next_move = TestAgent.get_action()
        self.assertLessEqual(next_move, _action_space)
        self.assertGreaterEqual(next_move, 0)

if __name__ == '__main__':
    unittest.main()
