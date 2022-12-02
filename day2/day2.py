# Day 2
# https://adventofcode.com/2022/day/2

with open('input.txt', 'r') as fobj:
    strategy = [line.strip().split(' ') for line in fobj.readlines()]

scoring = {
    'A': 1,
    'B': 2,
    'C': 3,
    'X': 1,
    'Y': 2,
    'Z': 3
}

# Part 1
total_points = 0
for play in strategy:
    their, our = play

    if their == chr(ord(our) - 23):
        total_points += (scoring[our] + 3)
    elif (their == 'A' and our == 'Y') or (their == 'B' and our == 'Z') or (their == 'C' and our == 'X'):
        total_points += (scoring[our] + 6)
    else:
        total_points += (scoring[our]) 

print('Part 1: {0}'.format(total_points))


# Part 2
total_points = 0
for play in strategy:
    their, our = play

    # Lose
    if our == 'X':
        total_points += ([3, 1, 2][ord(their)-65])  
    # Draw
    elif our == 'Y':
        total_points += (scoring[their] + 3)
    # Win
    else:
        total_points += ([2, 3, 1][ord(their)-65] + 6) 

print('Part 2: {0}'.format(total_points))