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
    location = (0, 0)

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

        # Update direction and distance
        current_direction = changeDirection(current_direction, turn)
        location = changeCoords(location, current_direction, distance)

    print 'Easter bunny HQ is %d blocks away.' % sum(map(abs, location))

if __name__ == '__main__':
    main()
