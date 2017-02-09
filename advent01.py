if __name__ == '__main__':
    case = 'L1, R3, R1, L5, L2, L5, R4, L2, R2, R2, L2, R1, L5, R3, L4, L1, L2, R3, R5, L2, R5, L1, R2, L5, R4, R2, R2, L1, L1, R1, L3, L1, R1, L3, R5, R3, R3, L4, R4, L2, L4, R1, R1, L193, R2, L1, R54, R1, L1, R71, L4, R3, R191, R3, R2, L4, R3, R2, L2, L4, L5, R4, R1, L2, L2, L3, L2, L1, R4, R1, R5, R3, L5, R3, R4, L2, R3, L1, L3, L3, L5, L1, L3, L3, L1, R3, L3, L2, R1, L3, L1, R5, R4, R3, R2, R3, L1, L2, R4, L3, R1, L1, L1, R5, R2, R4, R5, L1, L1, R1, L2, L4, R3, L1, L3, R5, R4, R3, R3, L2, R2, L1, R4, R2, L3, L4, L2, R2, R2, L4, R3, R5, L2, R2, R4, R5, L2, L3, L2, R5, L4, L2, R3, L5, R2, L1, R1, R3, R3, L5, L2, L2, R5'
    path = [(1 if x[0] == 'R' else -1, int(x[1:])) for x in case.split(', ')]

    headings = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    current_heading = 0
    current_position = [0, 0]
    history = [tuple(current_position)]
    first_time = True

    for step in path:
        current_heading = (current_heading + step[0]) % len(headings)
        for i in range(step[1]):
            current_position[0] += headings[current_heading][0]
            current_position[1] += headings[current_heading][1]
            if tuple(current_position) in history and first_time:
                print('After %d steps, visited location twice: %d, %d or %d blocks away' % (len(history), current_position[0], current_position[1], abs(current_position[0]) + abs(current_position[1])))
                first_time = False
            else:
                history.append(tuple(current_position))

    print('Last position: %d, %d or %d blocks away' % (current_position[0], current_position[1], abs(current_position[0]) + abs(current_position[1])))
