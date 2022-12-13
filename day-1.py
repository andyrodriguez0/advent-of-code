
# Part One and Part Two

elves = []
elf = 0

with open('input.txt', 'r') as f:
    for line in f:
        line = line.strip()
        if line:
            elf += int(line)
        else:
            elves.append(elf)
            elf = 0

elves.sort()

print(f'Top: {elves[-1]}')
print(f'Top Three: {elves[-1] + elves[-2] + elves[-3]}')