import gym
from gym import spaces
import numpy as np
from scoring import init_scoreboard, fill_scoreboard, possible_categories_with_scores, calculate_end_score

class YahtzeeEnv(gym.Env):
    def __init__(self):
        super(YahtzeeEnv, self).__init__()
        
        # Define the action space (keep/re-roll dice + choose category)
        self.action_space = spaces.MultiDiscrete([2] * 5 + [13])
        
        # Define the observation space
        self.observation_space = spaces.Dict({
            "dices": spaces.MultiDiscrete([6] * 5),  # Values of 5 dice (1 to 6)
            "rolls_left": spaces.Discrete(4),        # Rolls left: 0 to 3
            "scoreboard": spaces.Box(low=-1, high=50, shape=(13,), dtype=np.int32),  # Scoreboard (-1 for unfilled)
            "turn": spaces.Discrete(14)             # Turn number: 1 to 13
        })

        self.reset()

    def reset(self):
        # Initialize the game state
        self.dices = [0] * 5
        self.rolls_left = 3
        self.scoreboard = [-1] * 13  # -1 indicates unfilled categories
        self.turn = 1
        self.total_score = 0
        
        # Return the initial state
        return self._get_state()

    def step(self, action):
        # Unpack the action
        keep_mask = action[:5]
        chosen_category = action[5]

        # Apply the dice roll based on the keep_mask
        self.dices = [
            self.dices[i] if keep_mask[i] == 1 else np.random.randint(1, 7)
            for i in range(5)
        ]
        self.rolls_left -= 1

        # Check if the turn is done (no rolls left or action to end)
        done = (self.rolls_left == 0 or chosen_category != -1)

        reward = 0
        if done:
            # Assign score to the chosen category
            if self.scoreboard[chosen_category] == -1:  # Only fill unfilled categories
                scores = possible_categories_with_scores(self.dices, self.scoreboard)
                self.scoreboard[chosen_category] = scores[chosen_category]
                reward = scores[chosen_category]
            else:
                reward = -10  # Penalize for invalid category choice

            self.total_score = calculate_end_score(self.scoreboard)
            self.turn += 1
            self.rolls_left = 3

        # End game after 13 turns
        game_over = self.turn > 13

        # Return the new state, reward, and done flag
        return self._get_state(), reward, done or game_over, {}

    def _get_state(self):
        # Encapsulate the current state as a dictionary
        return {
            "dices": np.array(self.dices, dtype=np.int32),
            "rolls_left": self.rolls_left,
            "scoreboard": np.array(self.scoreboard, dtype=np.int32),
            "turn": self.turn
        }

    def render(self, mode="human"):
        # Optional: Visualize the game state
        print(f"Turn {self.turn}, Rolls Left: {self.rolls_left}")
        print(f"Dices: {self.dices}")
        print(f"Scoreboard: {self.scoreboard}")