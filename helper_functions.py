def get_yes_or_no(prompt):
    while True:
        user_input = input(prompt).strip().lower()  # Normalize input
        if user_input in ['y', 'n', 'yes', 'no']:
            return user_input
        else:
            print("Invalid input. Please enter 'y', 'n', 'yes', or 'no'.")