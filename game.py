import random
from scoring import (
    init_scoreboard,
    calculate_end_score,
    fill_scoreboard,
    possible_categories_with_scores,
    allign_for_printing,
    print_scoreboard,
    dice_to_art,
)

class Game:
    def __init__(self):
        self.scoreboard = init_scoreboard() # initalize empty scoreboard
        self.dices = [0] * 5 # initalize empty dices
        self.roll_count = 0  # keeps track of the current throws
        self.turn = 1 # keeps track of the current turn
        self.max_turns = 13

    def sort_dices(self):
        self.dices.sort()

    def dice_roll(self, keep_indices = None):
        self.roll_count += 1
        if keep_indices is None:
            self.dices = [random.randint(1, 6) for _ in range(5)]
            self.sort_dices()
        else:
            self.dices = [self.dices[i] if i in keep_indices else random.randint(1, 6) for i in range(5)]
        self.sort_dices()
    

    def get_score(self):
        return calculate_end_score(self.scoreboard)
    
    def update_scoreboard(self, category):
        self.scoreboard = fill_scoreboard(self.dices, category, self.scoreboard)

    def show_possible_scores(self):
        return allign_for_printing(possible_categories_with_scores(self.dices, self.scoreboard))
    
    def show_scoreborad(self):
        return print_scoreboard(self.scoreboard)
    
    def print_dices(self):
        print("\n\n".join(dice_to_art(d) for d in self.dices))

    def get_dice_to_keep(self) -> list[int]:
            """
            Prompts the player to select dice to keep and validates the input.
            """
            while True:
                try:
                    user_input = input('Enter the indices (0-5) of the dice to keep, separated by spaces: ').split()
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
                if category in [key for key, value in self.scoreboard.items() if not value]:
                    return category
                else:
                    raise ValueError("Category has already been filled. Choose an empty category.")
            except ValueError as e:
                print(f"Invalid input: {e}")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")

