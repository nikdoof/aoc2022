# Day 1 - Calorie Counting
# https://adventofcode.com/2022/day/1

elves = []

with open('input.txt', 'r') as fobj:
    total_calories = 0

    # Iterate the file, and build the totals
    for line in fobj.readlines():
        if line.strip() == '':
            elves.append(total_calories)
            total_calories = 0
        else:
            total_calories += int(line)
    
    # Add the last elf of the file
    elves.append(total_calories)

# Sort the elves
elves = sorted(elves, reverse=True)

print('Total Calories: {0}'.format(sum(elves)))
print('Total Elves: {0}'.format(len(elves)))

# Part 1 - Top elf
print('Highest Calories Elf: {0}'.format(max(elves)))

# Part 2 - Top 3 elves
print('Top 3 Elves Total: {0}'.format(sum(elves[:3])))
