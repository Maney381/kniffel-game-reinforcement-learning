import random
from dices import Dices
from scoring import Scoreboard

class Game:
    def __init__(self):
        self.scoreboard = Scoreboard() # initalize empty scoreboard
        self.dices = Dices() # initalize empty dices
        self.roll_count = 0  # keeps track of the current throws
        self.turn = 1 # keeps track of the current turn
        self.max_turns = 13


    def dice_roll(self, keep_indices = None):
        self.roll_count += 1
        if keep_indices is None:
            self.dices.dices = [random.randint(1, 6) for _ in range(5)]
        else:
            self.dices.dices = [self.dices.dices[i] if i in keep_indices else random.randint(1, 6) for i in range(5)]
        self.dices.dices.sort()

    def get_end_score(self):
        return self.scoreboard.calculate_end_score()
    
    def update_scoreboard(self, category):
        self.scoreboard.fill_scoreboard(self.dices, category)

    def show_possible_scores(self):
        categories = self.scoreboard.possible_categories_with_scores(self.dices)
        string = 'Possible scores:\n'
        string += '{:<13}:  {:>0}\n'.format('Category', 'Score')
        string += '-'*21 + '\n'
        for category, score in categories.items():
            string += '{:<13}:  {:>5}'.format(category, score)
            string += '\n'
        return string

    def get_dice_to_keep(self) -> list[int]:
            """
            Prompts the player to select dice to keep and validates the input.
            """
            while True:
                try:
                    user_input = input('\nEnter the indices (0-5) of the dice to keep, separated by spaces: ').split()
                    indices_to_keep = [int(index) for index in user_input]
                    
                    if not all(0 <= index <= 5 for index in indices_to_keep):
                        raise ValueError("Indices must be between 0 and 5.")
                    if len(indices_to_keep) != len(set(indices_to_keep)):
                        raise ValueError("Indices cannot be duplicated.")
                    
                    return indices_to_keep
                except ValueError as e:
                    print(f"Invalid input: {e}")
                except Exception as e:
                    print(f"An unexpected error occurred: {e}")

    def choose_category(self):
        """
        Prompts the player to select a category and validates the choice.
        """
        while True:
            try:
                category = input('Enter a category to assign your dice score: ')
                if category in [key for key, value in self.scoreboard.scoreboard.items() if not value]:
                    return category
                else:
                    raise ValueError("Category has already been filled. Choose an empty category.")
            except ValueError as e:
                print(f"Invalid input: {e}")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")

