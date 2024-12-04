def load_input_file(path="input.txt"):
    with open(path) as f:
        return f.read()

def count_wort(grid, word="XMAS"):
    rows, cols = len(grid), len(grid[0])
    word_len = len(word)
    directions = [
        (0, 1),  # right
        (0, -1),  # left
        (1, 0),  # down
        (-1, 0),  # up
        (1, 1),  # down-right
        (1, -1),  # down-left
        (-1, 1),  # up-right
        (-1, -1)  # up-left
    ]

    def is_valid(x, y):
        # gegen Index Error
        return 0 <= x < rows and 0 <= y < cols

    def find_word(x, y, dx, dy):
        # Für jeden Buchstaben im Wort
        for i in range(word_len):
            # Position des nächsten Buchstaben
            nx = x + i * dx
            ny = y + i * dy
            if not is_valid(nx, ny) or grid[nx][ny] != word[i]:
                return False
        return True

    count = 0
    for x in range(rows):
        for y in range(cols):
            # Für jede Zelle
            for dx, dy in directions:
                if find_word(x, y, dx, dy):
                    count += 1

    return count

def count_wort2(grid):
    rows, cols = len(grid), len(grid[0])
    counter = 0

    for y in range(1, rows - 1):
        for x in range(1, cols - 1):
            try:
                cell = grid[y][x]
                cell_lo = grid[y - 1][x - 1]
                cell_ru = grid[y + 1][x + 1]
                cell_ro = grid[y - 1][x + 1]
                cell_lu = grid[y + 1][x - 1]

                p1, p2 = False, False

                if cell == "A":
                    if (cell_lo in ["M", "S"] and
                            cell_ru in ["M", "S"] and
                            cell_lo != cell_ru):
                        p1 = True

                    if (cell_ro in ["M", "S"] and
                            cell_lu in ["M", "S"] and
                            cell_ro != cell_lu):
                        p2 = True

                    if p1 and p2:
                        counter += 1
            except IndexError:
                continue

    return counter


# Example word search grid
grid = [
    "MMMSXXMASM",
    "MSAMXMSMSA",
    "AMXSXMAAMM",
    "MSAMASMSMX",
    "XMASAMXAMM",
    "XXAMMXXAMA",
    "SMSMSASXSS",
    "SAXAMASAAA",
    "MAMMMXMMMM",
    "MXMXAXMASX"
]

inp_2 = [
    "MMMSMMMMMM",
    "MMAMMMSMSM",
    "MMMSMMAAMM",
    "MMAMASMSMM",
    "MMMSMMMMMM",
    "MMMMMMMMMM",
    "SMSMSMSMSM",
    "MAMAMAMAMM",
    "MMMMMMMMMM",
    "MMMMMMMMMM",
]

result = count_wort(load_input_file().splitlines())
print(f"The word 'XMAS' appears {result} times.")

#print(f"The pattern appear {count_wort2(load_input_file().splitlines())} times.")
#print(f"The pattern appear {count_wort2(inp_2)} times.")