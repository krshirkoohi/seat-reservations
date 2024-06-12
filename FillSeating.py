# 1. parse and read the file
path = 'EmptySeating.txt'

def readFile(path):
    with open(path, 'r') as file:
        return [list(line.strip()) for line in file]  # standard file reading approach

# IMPORTANT NOTE:
# - could be obvious but a SEAT is defined by [row][col]
# - we treat the txt file as a 2D position matrix
# - with the markers 'L' = empty, '#' = filled, '.' = immutable obstacle

# 2. helper functions
def checkOcc(seating, row, col):
    return seating[row][col] == '#'

def countAdjOcc(seating, row, col):
    directions = [(-1, 1), (0, 1), (1, 1), (-1, 0), (1, 0), (-1, -1), (0, -1), (1, -1)]
    occCount = 0
    for dr, dc in directions:
        r, c = row + dr, col + dc
        if 0 <= r < len(seating) and 0 <= c < len(seating[0]) and checkOcc(seating, r, c):
            occCount += 1
    return occCount

def countOccSeats(seating):
    return sum(row.count('#') for row in seating)

# 3. impose conditions
def applyRules(seating):
    newSeating = [row.copy() for row in seating]
    for row in range(len(seating)):
        for col in range(len(seating[0])):
            # If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
            if seating[row][col] == 'L' and countAdjOcc(seating, row, col) == 0:
                newSeating[row][col] = '#'
            # If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
            elif seating[row][col] == '#' and countAdjOcc(seating, row, col) >= 4:
                newSeating[row][col] = 'L'
    return newSeating

# 4. fill all possible seats
def fillAllSeats(seating):
    while True:
        newSeating = applyRules(seating)
        if newSeating == seating:
            break
        seating = newSeating
    return seating

# 5. test code if there is time
seating = readFile(path)
# print(seating)

filled_seating = fillAllSeats(seating)
occSeats = countOccSeats(filled_seating)

for row in filled_seating:
    print("".join(row))

print(f"Number of occupied seats: {occSeats}")