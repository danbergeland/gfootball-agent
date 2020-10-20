import random

class BasicAgent:
    def __init__(self, action_space_dim:int):
        self._action_space_dim = action_space_dim

    def get_action(self):
        return random.randint(0,self._action_space_dim)
