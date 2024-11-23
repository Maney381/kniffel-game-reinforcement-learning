def init_scoreboard():
        categories = [
            'ones',
            'twos',
            'threes',
            'fours',
            'fives',
            'sixes',
            '3_of_a_kind',
            '4_of_a_kind',
            'full_house',
            'small_street',
            'large_street',
            'yahtzee',
            'chance'
        ]
        return {category : '' for category in categories}

def maximum_occurence(dices):
    max_count = 0
    counts = {}
    for dice in dices:
        counts[dice] = counts.get(dice, 0) + 1
        # Keep track of the maximum count while iterating
        if counts[dice] > max_count:
            max_count = counts[dice]
    return counts, max_count

def possible_full_house(dices):
    dices_dic, max_count = maximum_occurence(dices)

    if (max_count == 3 and len(dices_dic) == 2) or max_count == 5:
        return True
    return False

def possible_small_large_street(dices):
    previous_dice = dices[0]
    street_length = 1
    small_street, large_street = False, False
    for dice in dices[1:]:
        if previous_dice == dice - 1:
            street_length +=1
        elif previous_dice == dice:
            continue
        else:
            street_length = 1
            
        previous_dice = dice
        
        if street_length == 4:
            small_street = True
    
    if street_length == 5:
        large_street = True
    return small_street, large_street   

def possible_yahtzee(dices):
    return maximum_occurence(dices)[1] == 5

def calculate_end_score(scorebaord):
    sum_upper_categories = 0 
    sum_lower_categories = 0
    for category, item in scorebaord.items():
        if category in ['ones', 'twos', 'threes', 'fours', 'fives', 'sixes']:
            sum_upper_categories += item
        else:
            sum_lower_categories += item

        if sum_upper_categories >= 63:
            sum_upper_categories += 35
        
    return sum_upper_categories + sum_lower_categories

def fill_scoreboard(dices, category, scoreboard):
    dices.sort()
    if scoreboard[category]:
        print('Error: category has already been filled out. Pick another category!')
        return scoreboard

    if category == 'ones':
        scoreboard['ones'] = dices.count(1) * 1
    if category == 'twos':
        scoreboard['twos'] = dices.count(2) * 2
    if category == 'threes':
        scoreboard['threes'] = dices.count(3) * 3
    if category == 'fours':
        scoreboard['fours'] = dices.count(4) * 4
    if category == 'fives':
        scoreboard['fives'] = dices.count(5) * 5
    if category == 'sixes':
        scoreboard['sixes'] = dices.count(6) * 6

    if category == '3_of_a_kind':
        if maximum_occurence(dices)[1] >= 3:
            scoreboard['3_of_a_kind'] = sum(dices)
        else: 
            print(f'{category} not possible -> {category} will be crossed out')
            scoreboard['3_of_a_kind'] = 0

    if category == '4_of_a_kind':
        if maximum_occurence(dices)[1] >= 4:
            scoreboard['4_of_a_kind'] = sum(dices)
        else:
            print(f'{category} not possible -> {category} will be crossed out')
            scoreboard['4_of_a_kind'] = 0

    if category == 'full_house':
        if possible_full_house(dices):
            scoreboard['full_house'] = 25
        else:
            print(f'{category} not possible -> {category} will be crossed out')
            scoreboard['full_house'] = 0

    small_street_possible, large_street_possible = possible_small_large_street(dices)
    if category == 'small_street':
        if small_street_possible:
            scoreboard['small_street'] = 30
        else:
            print(f'{category} not possible -> {category} will be crossed out')
            scoreboard['small_street'] = 0

    if category == 'large_street':
        if large_street_possible:
            scoreboard['large_street'] = 40
        else:
            print(f'{category} not possible -> {category} will be crossed out')
            scoreboard['large_street'] = 0

    if category == 'yahtzee':
        if possible_yahtzee(dices):
            scoreboard['yahtzee'] = 50
        else: 
            print(f'{category} not possible -> {category} will be crossed out')
            scoreboard['yahtzee'] = 0

    if category == 'chance':
        scoreboard['chance'] = sum(dices)
    
    return scoreboard

def possible_categories_with_scores(dices, scoreboard):
    categories = {}
    if not scoreboard['ones']:
        categories['ones'] = dices.count(1) * 1
    if not scoreboard['twos']:
        categories['twos'] = dices.count(2) * 2
    if not scoreboard['threes'] :
        categories['threes'] = dices.count(3) * 3
    if not scoreboard['fours'] :
        categories['fours'] = dices.count(4) * 4
    if not scoreboard['fives'] :
        categories['fives'] = dices.count(5) * 5
    if not scoreboard['sixes'] :
        categories['sixes'] = dices.count(6) * 6

    if not scoreboard['3_of_a_kind']:
        if maximum_occurence(dices)[1] >= 3:
            categories['3_of_a_kind'] = sum(dices)
        else: 
            categories['3_of_a_kind'] = 0

    if not scoreboard['4_of_a_kind']:
        if maximum_occurence(dices)[1] >= 4:
            categories['4_of_a_kind'] = sum(dices)
        else:
            categories['4_of_a_kind'] = 0

    if not scoreboard['full_house']:
        if possible_full_house(dices):
            categories['full_house'] = 25
        else:
            categories['full_house'] = 0

    small_street_possible, large_street_possible = possible_small_large_street(dices)
    if not scoreboard['small_street']:
        if small_street_possible:
            categories['small_street'] = 30
        else:
            categories['small_street'] = 0

    if not scoreboard['large_street']:
        if large_street_possible:
            categories['large_street'] = 40
        else:
            categories['large_street'] = 0

    if not scoreboard['yahtzee']:
        if possible_yahtzee(dices):
            categories['yahtzee'] = 50
        else: 
            categories['yahtzee'] = 0

    if not scoreboard['chance']:
        categories['chance'] = sum(dices)
    
    return categories

def allign_for_printing(scoreboard):
    string = '\n\n'
    string += '{:<13}:  {:>0}\n'.format('Category', 'Score')
    string += '-'*21 + '\n'
    for category, entry in scoreboard.items():
        string += '{:<13}:  {:>5}'.format(category, entry)
        string += '\n'
    return string

def print_scoreboard(scoreboard):
    string = 'Current scoreboard:\n'
    string += '{:<13}:  {:>0}\n'.format('Category', 'Score')
    string += '-'*21 + '\n'
    for category, entry in scoreboard.items():
        string += '{:<13}:  {:>5}'.format(category, entry)
        string += '\n'
    return string

def dice_to_art(dice_value):
    dice_art = {
        1: "     \n  *  \n     ",
        2: "*    \n     \n    *",
        3: "*    \n  *  \n    *",
        4: "*   *\n     \n*   *",
        5: "*   *\n  *  \n*   *",
        6: "*   *\n*   *\n*   *",
    }
    
    art =  dice_art.get(dice_value, "     \n     \n     ")  # Default for invalid values
    
    # Add a border
    bordered_art = []
    lines = art.split("\n")  # Split the art into lines
    bordered_art.append(" -----")  # Top border
    for line in lines:
        bordered_art.append(f"|{line}|")  # Add side borders
    bordered_art.append(" -----")  # Bottom border
    
    # Join the bordered lines into a single string
    return "\n".join(bordered_art)

