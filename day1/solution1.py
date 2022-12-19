
def return_max(filename):
    '''finds the elf with the highest caloric intake from a txt file
    where meals are seperated by new lines and each elves meals are
    seperated by two newlines'''

    # stores the highest elves intake
    max_calories = 0

    # used to count each elves caloric intake
    calorie_counter = 0

    # counts each elves caloric intake and if its the highest recorded stores 
    # it in max_calories
    with open(filename) as fp:
        for line in fp.readlines():

            # when its a new elf, checks if maximum then resets counter
            if line == '\n':
                if calorie_counter > max_calories:
                    max_calories = calorie_counter
                calorie_counter = 0
            
            else: 
                calorie_counter += int(line)
    

    return max_calories

return_max('day1/input.txt')