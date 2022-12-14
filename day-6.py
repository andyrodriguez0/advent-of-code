
# Part One

location = 4

with open('day-6-input.txt', 'r') as f:
    signal = f.read()
    marker = signal[:4]
    while len(set(marker)) != 4:
        location += 1
        marker = signal[location - 4: location]

print(location)

# Part Two

location = 4

with open('day-6-input.txt', 'r') as f:
    signal = f.read()
    marker = signal[:14]
    while len(set(marker)) != 14:
        location += 1
        marker = signal[location - 14: location]

print(location)