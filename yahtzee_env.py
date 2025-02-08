import gym
import numpy as np
from gym import spaces
from game import Game

class YahtzeeEnv(gym.Env):
    """s
    Custom OpenAI Gym environment for Yahtzee.
    """
    def __init__(self):
        super(YahtzeeEnv, self).__init__()
        
        # Initialize the game
        self.game = Game()
        
        # Observation space: (5 dice values, roll count, turn number, scoreboard state)
        self.observation_space = spaces.Box(low=0, high=6, shape=(5 + 1 + 1 + 13,), dtype=np.int32)
        
        # Action space: (5 binary choices for rerolling dice + 13 category choices)
        self.action_space = spaces.Discrete(45)
        
    def reset(self):
        """Reset the environment and return the initial state."""
        self.game = Game()
        self.game.dice_roll()  # Initial roll   
        return self.get_observation()
    
    def get_observation(self):
        """Return the current game state as an observation."""
        dice_values = self.game.dices.dices
        roll_count = [self.game.roll_count]
        turn_number = [self.game.turn]
        scoreboard_state = [1 if v != '' else 0 for v in self.game.scoreboard.scoreboard.values()]
        
        return np.array(dice_values + roll_count + turn_number + scoreboard_state, dtype=np.int32)
    
    def step(self, action):
        """Take an action and return the next state, reward, done flag, and extra info."""
        reward = 0
        done = False

        if action < 32:  # Reroll action (action is a 5-bit binary number)
            reroll_mask = [(action >> i) & 1 for i in range(5)]  # Convert number to bitmask
            indices_to_keep = [i for i in range(5) if not reroll_mask[i]]
            self.game.dice_roll(indices_to_keep)
            reward = 0  # No reward for rerolling
        else:  # Choosing a category (actions 32-44 map to categories)
            category_list = list(self.game.scoreboard.scoreboard.keys())
            category = category_list[action - 32]
            
            if self.game.scoreboard.scoreboard[category] == '':  # Valid category
                self.game.update_scoreboard(category)
                reward = self.game.get_end_score()
                self.game.turn += 1
                self.game.roll_count = 0
                if self.game.turn > self.game.max_turns:
                    done = True  # End of game
                else:
                    self.game.dice_roll()  # Start next turn
            else:
                reward = -10  # Penalize invalid category selection
        
        return self.get_observation(), reward, done, {}

    def render(self, mode='human'):
        """Render the current state of the game."""
        print("\n" + str(self.game.dices))
        print(self.game.scoreboard)
    
    def close(self):
        """Cleanup if necessary."""
        pass