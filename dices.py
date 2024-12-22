class Dices:
    def __init__(self):
        self.dices = [0] * 5
        self.counts, self.max_count = self.calculate_counts_and_max_count
    
    def __str__(self):
        dice_art = {
            1: "     \n  *  \n     ",
            2: "*    \n     \n    *",
            3: "*    \n  *  \n    *",
            4: "*   *\n     \n*   *",
            5: "*   *\n  *  \n*   *",
            6: "*   *\n*   *\n*   *",
        }
        
        # Store the bordered art for each dice
        bordered_art_list = []
        for dice in self.dices:
            art = dice_art.get(dice, "     \n     \n     ")  # Default for invalid dice
            bordered_art = []
            lines = art.split("\n")
            bordered_art.append(" ----- ")  # Top border
            for line in lines:
                bordered_art.append(f"|{line}|")  # Add side borders
            bordered_art.append(" ----- ")  # Bottom border
            bordered_art_list.append(bordered_art)
        
        # Combine the lines of all dice horizontally
        result = []
        for i in range(len(bordered_art_list[0])):  # Iterate over the number of lines in a single dice
            result.append("  ".join(dice[i] for dice in bordered_art_list))  # Join each corresponding line
        
        return "\n".join(result)

    @property
    def calculate_counts_and_max_count(self):
        max_count = 0
        counts = {}
        for dice in self.dices:
            counts[dice] = counts.get(dice, 0) + 1
            # Keep track of the maximum count while iterating
            if counts[dice] > max_count:
                max_count = counts[dice]
        return counts, max_count

    def possible_full_house(self):
        self.counts, self.max_count = self.calculate_counts_and_max_count
        if (self.max_count == 3 and len(self.counts) == 2) or self.counts == 5:
            return True
        return False
    
    def possible_yahtzee(self):
        self.counts, self.max_count = self.calculate_counts_and_max_count
        return self.max_count== 5
    
    def possible_small_large_street(self):
        self.counts, self.max_count = self.calculate_counts_and_max_count
        self.dices.sort()
        previous_dice = self.dices[0]
        street_length = 1
        small_street, large_street = False, False
        for dice in self.dices[1:]:
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