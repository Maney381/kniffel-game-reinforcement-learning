from game import Game
from helper_functions import get_yes_or_no

if __name__ == "__main__":
    # Initilaize the game
    game = Game()
    print(game.show_scoreborad())

    start_game = get_yes_or_no('Do you want to start the game? (y/n):\n')

    if start_game in ['y', 'yes']:
        while game.turn <= game.max_turns:
            start_turn = input(f'To start your {game.turn}. turn press Enter.\n')
            game.dice_roll()
            
            while game.roll_count < 3:
                print(f'{game.turn}. round, {game.roll_count}. throw. You have the following dice:\n')
                game.print_dices()
                print('With this throw, you have the following scores:')
                print(game.show_possible_scores())

                response = get_yes_or_no("Do you want to throw again? (y/n): ")
                if response in ['y', 'yes']:
                    indices_to_keep = game.get_dice_to_keep()
                    game.dice_roll(indices_to_keep)
                else:
                    break

            print(f'No more throws. You finished your {game.turn}. turn. These are your dice: {game.dices}.')
            print('You can enter them in one of the following categories:\n')
            print(game.show_possible_scores())

            chosen_category = game.choose_category()
            game.update_scoreboard(chosen_category)
            print(game.show_scoreborad())

            game.turn += 1
            game.roll_count = 0
            
        print("Game over! You've completed all turns.")
        print(f"Your final score is: {game.get_score()}")
        
    else:
        print('Goodbye!')