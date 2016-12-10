from sys import stdin
import re

def changeDirection(current_direction, turn):

    if turn == 'R':
        return (current_direction + 90) % 360
    elif turn == 'L':
        return (current_direction - 90) % 360

def changeCoords(location, current_direction, distance):

    x = location[0]
    y = location[1]

    # Facing North
    if current_direction == 0:
        return x, y + distance
    # Facing East
    elif current_direction == 90:
        return x + distance, y
    # Facing South
    elif current_direction == 180:
        return x, y - distance
    # Facing West
    elif current_direction == 270:
        return x - distance, y

def main():

    # Start facing North at origin
    current_direction = 0
    current_location = (0, 0)

    # Store location visited
    previous_locations = set(current_location)


    # Read all directions from input
    s = stdin.readline()

    # Split string
    directions_arr = s.split(', ')

    # Regex to find numbers
    digits = re.compile('\d+')
    findall = re.findall

    for step in directions_arr:

        # Get turn and distance for each step
        turn = step[0]
        distance = int(findall(digits, step)[0])

        # Convert locations

        # Update direction and distance
        current_direction = changeDirection(current_direction, turn)

        # Collect each location (eg. R4 -> collect distances at R1, R2, R3, R4)
        for i in range(0, distance):

            current_location = changeCoords(current_location, current_direction, 1)

            if current_location in previous_locations:
                print 'Easter Bunny HQ is %d blocks away.' % sum(map(abs, current_location))
                return
            else:
                previous_locations.add(current_location)

if __name__ == '__main__':
    main()
