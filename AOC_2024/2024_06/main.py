import sys
import os

def change_row(row,inp,x):
    output = []
    for index, char in enumerate(row):
        if index == x:
            output.append(inp)
        else:
            output.append(char)

def move_gard(map, alt_pos, curr_pos, char_rep, char_new):
    #map[alt_pos[0]][alt_pos[1]] = char_rep
    map[alt_pos[0]] = change_row(map[alt_pos[0]], char_rep, alt_pos[1])
    #map[curr_pos[0]][curr_pos[1]] = char_new
    map[curr_pos[0]] = change_row(map[curr_pos[0]], char_new, curr_pos[1])
    return map

def clear_last_n_lines(n):
    """
    Clear the last n lines in the console.

    Args:
    n (int): Number of lines to clear.
    """
    # Get the current cursor position
    cursor_up = '\033[A'
    erase_line = '\033[K'

    # Move cursor up n lines and erase each line
    for _ in range(n):
        sys.stdout.write(cursor_up)
        sys.stdout.write(erase_line)

    # Flush the output to ensure immediate display
    sys.stdout.flush()

def is_next_step_end(map,pos):
    if 0 > pos[0]-1 or pos[0]+1 > len(map):
        print("ended")
        return True
    if 0 > pos[1]-1 or pos[1]+1 > len(map[0]):
        print("ended")
        return True
    return False

orientation = {
    0: "^",
    90: ">",
    180: "v",
    270: "<",
}

def main(in_map,interactive=False):
    print("Find Starting Location of Guard")
    pos_start = (0, 0)
    for y_index, row in enumerate(in_map):
        for x_index, value in enumerate(row):
            if value == "^":
                pos_start = (y_index, x_index)
    print("Starts at", pos_start)
    print("\n---")
    curr_pos = pos_start
    map = in_map
    while True:
        if is_next_step_end(map, curr_pos):
            print("stop")
            break
        hi = map[curr_pos[0]][curr_pos[1]]
        if hi == "^":
            next_hi = map[curr_pos[0] - 1][curr_pos[1]]

            if next_hi == "#":
                alt_pos = curr_pos
                curr_pos = (curr_pos[0], curr_pos[1]+1)
                move_gard(map, alt_pos, curr_pos, "X", orientation[90])
            alt_pos = curr_pos
            curr_pos = (curr_pos[0] - 1, curr_pos[1])
            char = "^"
            move_gard(map, alt_pos, curr_pos, "X", char)
            print(curr_pos)
        print(hi)


test_input = [
    "....#.....",
    ".........#",
    ".........."
    "..#.......",
    ".......#..",
    "..........",
    ".#..^.....",
    "........#.",
    "#.........",
    "......#..."
]

if __name__ == '__main__':
    #print("\033[2J")
    clear_last_n_lines(20)
    main(test_input, interactive=True)