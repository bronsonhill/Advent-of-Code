
def return_max(filename):
    '''finds the three elves with the highest caloric intake from a txt 
    file where meals are seperated by new lines and each elves meals are
    seperated by two new lines'''

    # stores the highest elves intake
    total_calories = []

    # used to count each elves caloric intake
    calorie_counter = 0

    # counts each elves caloric intake and if its the highest recorded stores 
    # it in max_calories
    with open(filename) as fp:
        for line in fp.readlines():
            # when its a new elf, checks if maximum then resets counter
            if line == '\n':
                total_calories.append(calorie_counter)
                calorie_counter = 0
            
            else: 
                calorie_counter += int(line)
            
    total_calories.sort(reverse=True)
    print(total_calories)
    return sum(total_calories[0:3])

print(return_max('day1/input.txt'))