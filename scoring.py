from dices import Dices

class Scoreboard():
    def __init__(self):
        self.scoreboard = self.init_scoreboard() 

    def __str__(self):
        string = 'Current scoreboard:\n'
        string += '{:<13}:  {:>0}\n'.format('Category', 'Score')
        string += '-'*21 + '\n'
        for category, entry in self.scoreboard.items():
            string += '{:<13}:  {:>5}'.format(category, entry)
            string += '\n'
        return string
    
    def init_scoreboard(self):
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
    
    def calculate_end_score(self):
        sum_upper_categories = 0 
        sum_lower_categories = 0
        for category, item in self.scoreboard.items():
            if category in ['ones', 'twos', 'threes', 'fours', 'fives', 'sixes']:
                sum_upper_categories += item
            else:
                sum_lower_categories += item

            if sum_upper_categories >= 63:
                sum_upper_categories += 35

        return sum_upper_categories + sum_lower_categories


    def fill_scoreboard(self, dices: Dices, category: str):
        dices.dices.sort()
        if self.scoreboard[category] != '':
            print('Error: category has already been filled out. Pick another category!')
            return

        if category == 'ones':
            self.scoreboard['ones'] = dices.dices.count(1) * 1
        if category == 'twos':
            self.scoreboard['twos'] = dices.dices.count(2) * 2
        if category == 'threes':
            self.scoreboard['threes'] = dices.dices.count(3) * 3
        if category == 'fours':
            self.scoreboard['fours'] = dices.dices.count(4) * 4
        if category == 'fives':
            self.scoreboard['fives'] = dices.dices.count(5) * 5
        if category == 'sixes':
            self.scoreboard['sixes'] = dices.dices.count(6) * 6

        if category == '3_of_a_kind':
            if dices.max_count >= 3:
                self.scoreboard['3_of_a_kind'] = sum(dices.dices)
            else: 
                print(f'{category} not possible -> {category} will be crossed out')
                self.scoreboard['3_of_a_kind'] = 0

        if category == '4_of_a_kind':
            if dices.max_count >= 4:
                self.scoreboard['4_of_a_kind'] = sum(dices.dices)
            else:
                print(f'{category} not possible -> {category} will be crossed out')
                self.scoreboard['4_of_a_kind'] = 0

        if category == 'full_house':
            if dices.possible_full_house():
                self.scoreboard['full_house'] = 25
            else:
                print(f'{category} not possible -> {category} will be crossed out')
                self.scoreboard['full_house'] = 0

        small_street_possible, large_street_possible = dices.possible_small_large_street()
        if category == 'small_street':
            if small_street_possible:
                self.scoreboard['small_street'] = 30
            else:
                print(f'{category} not possible -> {category} will be crossed out')
                self.scoreboard['small_street'] = 0

        if category == 'large_street':
            if large_street_possible:
                self.scoreboard['large_street'] = 40
            else:
                print(f'{category} not possible -> {category} will be crossed out')
                self.scoreboard['large_street'] = 0

        if category == 'yahtzee':
            if dices.possible_yahtzee():
                self.scoreboard['yahtzee'] = 50
            else: 
                print(f'{category} not possible -> {category} will be crossed out')
                self.scoreboard['yahtzee'] = 0

        if category == 'chance':
            self.scoreboard['chance'] = sum(dices.dices)
        ###end of function
    
    def possible_categories_with_scores(self, dices: Dices):
        categories = {}
        if self.scoreboard['ones'] == '':
            categories['ones'] = dices.dices.count(1) * 1
        if self.scoreboard['twos'] == '':
            categories['twos'] = dices.dices.count(2) * 2
        if self.scoreboard['threes'] == '':
            categories['threes'] = dices.dices.count(3) * 3
        if self.scoreboard['fours'] == '':
            categories['fours'] = dices.dices.count(4) * 4
        if self.scoreboard['fives'] == '':
            categories['fives'] = dices.dices.count(5) * 5
        if self.scoreboard['sixes'] == '':
            categories['sixes'] = dices.dices.count(6) * 6

        if self.scoreboard['3_of_a_kind'] == '':
            if dices.max_count >= 3:
                categories['3_of_a_kind'] = sum(dices.dices)
            else: 
                categories['3_of_a_kind'] = 0

        if self.scoreboard['4_of_a_kind'] == '':
            if dices.max_count >= 4:
                categories['4_of_a_kind'] = sum(dices.dices)
            else:
                categories['4_of_a_kind'] = 0

        if self.scoreboard['full_house'] == '':
            if dices.possible_full_house():
                categories['full_house'] = 25
            else:
                categories['full_house'] = 0

        small_street_possible, large_street_possible = dices.possible_small_large_street()
        if self.scoreboard['small_street'] == '':
            if small_street_possible:
                categories['small_street'] = 30
            else:
                categories['small_street'] = 0

        if self.scoreboard['large_street'] == '':
            if large_street_possible:
                categories['large_street'] = 40
            else:
                categories['large_street'] = 0

        if self.scoreboard['yahtzee'] == '':
            if dices.possible_yahtzee():
                categories['yahtzee'] = 50
            else: 
                categories['yahtzee'] = 0

        if self.scoreboard['chance'] == '':
            categories['chance'] = sum(dices.dices)
        
        return categories