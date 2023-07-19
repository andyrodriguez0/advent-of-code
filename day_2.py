
# Part One

score = 0

with open('day-2-input.txt', 'r') as f:
    for line in f:
        moves = line.split()
        if moves[1] == 'X':
            score += 1
            if moves[0] == 'C':
                score += 6
            elif moves[0] == 'A':
                score += 3
        elif moves[1] == 'Y':
            score += 2
            if moves[0] == 'A':
                score += 6
            elif moves[0] == 'B':
                score += 3
        else:
            score += 3
            if moves[0] == 'B':
                score += 6
            elif moves[0] == 'C':
                score += 3

print(f'Strategy One Score: {score}')

# Part Two

score = 0

with open('day-2-input.txt', 'r') as f:
    for line in f:
        moves = line.split()
        if moves[1] == 'X':
            if moves[0] == 'A':
                score += 3
            elif moves[0] == 'B':
                score += 1
            else:
                score += 2
        elif moves[1] == 'Y':
            score += 3
            if moves[0] == 'A':
                score += 1
            elif moves[0] == 'B':
                score += 2
            else:
                score += 3
        else:
            score += 6
            if moves[0] == 'A':
                score += 2
            elif moves[0] == 'B':
                score += 3
            else:
                score += 1

print(f'Strategy Two Score: {score}')