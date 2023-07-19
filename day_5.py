
# Part One

import re

matches = []
search = r'.(.)...(.)...(.)...(.)...(.)...(.)...(.)...(.)...(.).'
stacks = {0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: []}

with open('day-5-input.txt', 'r') as f:
    for i in range(8):
        line = f.readline()
        matches.append(re.match(search, line))
    for match in matches:
        hits = match.groups()
        for i in range(len(hits)):
            if hits[i] != ' ':
                stacks[i].append(hits[i])
    for i in range(len(stacks)):
        stacks[i].reverse()
    f.readline()
    f.readline()
    for i in range(502):
        line = f.readline().split()
        for i in range(int(line[1])):
            stacks[int(line[5]) - 1].append(stacks[int(line[3]) - 1][-1])
            stacks[int(line[3]) - 1].pop()

print(f'Part One Stacks: {stacks}')

# Part Two

stacks = {0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: []}

with open('day-5-input.txt', 'r') as f:
    for match in matches:
        hits = match.groups()
        for i in range(len(hits)):
            if hits[i] != ' ':
                stacks[i].append(hits[i])
    for i in range(len(stacks)):
        stacks[i].reverse()
    f.readline()
    f.readline()
    f.readline()
    f.readline()
    f.readline()
    f.readline()
    f.readline()
    f.readline()
    f.readline()
    f.readline()
    for i in range(502):
        line = f.readline().split()
        stacks[int(line[5]) - 1].extend(stacks[int(line[3]) - 1][-int(line[1]):])
        stacks[int(line[3]) - 1] = stacks[int(line[3]) - 1][:-int(line[1])]

print(f'Part Two Stacks: {stacks}')