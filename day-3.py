
# Part One

letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
priorities = 0

with open('day-3-input.txt', 'r') as f:
    for line in f:
        line = line.strip()
        for letter in line[:int(len(line) / 2)]:
            if letter in line[int(len(line) / 2):]:
                priorities += letters.index(letter) + 1
                break

print(f'Part One Priorities: {priorities}')

# Part Two

priorities = 0

with open('day-3-input.txt', 'r') as f:
    lines = f.read().split()
    for i in range(int(len(lines) / 3)):
        for letter in lines[3 * i]:
            if letter in lines[3 * i + 1]:
                if letter in lines[3 * i + 2]:
                    priorities += letters.index(letter) + 1
                    break

print(f'Part Tw0 Priorities: {priorities}')