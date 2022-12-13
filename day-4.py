
# Part One

pairs = 0

with open('day-4-input.txt', 'r') as f:
    for line in f:
        line = line.strip().replace('-',',').split(',')
        if int(line[0]) >= int(line[2]) and int(line[1]) <= int(line[3]):
            pairs += 1
        elif int(line[2]) >= int(line[0]) and int(line[3]) <= int(line[1]):
            pairs += 1

print(f'Part One Pairs: {pairs}')

# Part Two

pairs = 0

with open('day-4-input.txt', 'r') as f:
    for line in f:
        line = line.strip().replace('-',',').split(',')
        if int(line[0]) >= int(line[2]) and int(line[0]) <= int(line[3]):
            pairs += 1
        elif int(line[1]) >= int(line[2]) and int(line[1]) <= int(line[3]):
            pairs += 1
        elif int(line[2]) >= int(line[0]) and int(line[2]) <= int(line[1]):
            pairs += 1
        elif int(line[3]) >= int(line[0]) and int(line[3]) <= int(line[1]):
            pairs += 1

print(f'Part Two Pairs: {pairs}')