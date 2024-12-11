import math

NUM_PROC = 4

def len_of_int(num: int) -> int:
    return int(math.log10(num)+1)

def even(num: int) -> bool:
    return num % 2 == 0

def handle_num(num: int) -> list:
    if num == 0:
        return [1]
    elif even(len_of_int(num)):
        first_h = int(str(num)[:int(len_of_int(num)/2)])
        sec_h = int(str(num)[int(len_of_int(num)/2):])
        return [first_h, sec_h]
    elif not even(len_of_int(num)):
        return [num*2024]
    else:
        print("Here")
    pass

def main(inp: list, blinks: int) -> int:
    data: list = inp
    new_data: list = []

    for blink in range(blinks):
        print(len(data),"at blink:", blink)
        for stein in data:
            out = handle_num(stein)
            for num in out:
                new_data.append(num)
        data = new_data
        new_data = []

    return len(data)

inp = [3279, 998884, 1832781, 517, 8, 18864,28,0]

if __name__ == '__main__':
    print(f"Len Stones: {main(inp, 75)}")