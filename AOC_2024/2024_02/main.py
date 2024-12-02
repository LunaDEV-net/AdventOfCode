# https://adventofcode.com/2024/day/2/input
def load_input_file(path="input.txt"):
    with open(path) as f:
        return f.read()

def row_fully_asc_desc(row):
    asc = None
    for y,x in enumerate(row[:-1]):
        value = x-row[y+1]
        #print(x,value)
        if asc is None:
            if value < 0:
                asc = True
            else:
                asc = False
        if value <= 0 and asc == False:
            return False
        elif value >= 0 and asc == True:
            return False
    return True

def row_differ(row):
    for y,x in enumerate(row[:-1]):
        value = abs(x-row[y+1])
        if not value < 1 and value > 3:
            return False
    return True


def check_safe_with_dampener(row):
    # ignore if safe in the first place
    if row_fully_asc_desc(row) and row_differ(row):
        return True

    # now with dampener
    for i in range(len(row)):
        modified_row = row[:i] + row[i + 1:]
        if row_fully_asc_desc(modified_row) and row_differ(modified_row):
            return True
    return False

def main(input):
    safe_without_dampener = 0
    safe_dampener = 0
    data = []
    for line in input.splitlines():
        temp = []
        for hi in line.split(" "):
            temp.append(int(hi))
        data.append(temp)

    for row in data:
        if row_fully_asc_desc(row):
            print(f"{data.index(row)} 1")
            if row_differ(row):
                print(f"{data.index(row)} 2")
                safe_without_dampener += 1
        if check_safe_with_dampener(row):
            safe_dampener += 1

    print("safe1",safe_without_dampener)
    print("safe2",safe_dampener)

if __name__ == '__main__':
    inp = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""
    main(load_input_file())