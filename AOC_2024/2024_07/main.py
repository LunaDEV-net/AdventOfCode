import re, math, itertools
from itertools import repeat

def load_input_file(path="input.txt"):
    with open(path) as f:
        return f.read().splitlines()

def part_one(total,output,index,line,inp):
    ok = False
    erg = line.split(":")[0]
    erg = int(erg)
    arg = re.findall(r"\d+", line.split(":")[1])
    arg = [int(x) for x in arg]
    # check +
    ops = ["+", "*"]  # Mathematische Operatoren
    all_pos_op_comb = list(itertools.product(ops, repeat=len(arg) - 1))
    for op_comb in all_pos_op_comb:
        to_eval_list = []
        for i in range(len(arg) - 1):
            to_eval_list.append("(")
        for i in range(len(arg)):
            to_eval_list.append(str(arg[i]))
            if i > 0:
                to_eval_list.append(")")
            if i < len(op_comb):
                to_eval_list.append(op_comb[i])

        to_eval = ''.join(to_eval_list)
        result = eval(to_eval)

        if result == erg:
            ok = True
            print(f"Index: {index} right with {op_comb}")
            output += erg
            total += 1
            break
    if not ok:
        print(f"Index: {index} not right with {op_comb}")
        total += 1

    return total, output

def part_two(total,output,index,line,inp):
    ok = False
    erg = line.split(":")[0]
    erg = int(erg)
    arg = re.findall(r"\d+", line.split(":")[1])
    arg = [int(x) for x in arg]
    # check +
    ops = ["+", "*", "||"]
    all_pos_op_comb = list(itertools.product(ops, repeat=len(arg) - 1))
    for op_comb in all_pos_op_comb:
        to_eval_list = []
        for i in range(len(arg) - 1):
            to_eval_list.append("(")
        for i in range(len(arg)):
            to_eval_list.append(str(arg[i]))
            if i > 0:
                app=True
                if i < len(op_comb):
                    if op_comb[i] == "||":
                        app=False
                if app:
                    to_eval_list.append(")")
            if i < len(op_comb):
                to_eval_list.append(op_comb[i])

        for ghg_index, ghg in enumerate(to_eval_list):
            if ghg == "||":
                to_eval_list[ghg_index - 1] = str(to_eval_list[ghg_index - 1]) + str(to_eval_list[ghg_index + 1])
                del to_eval_list[ghg_index:ghg_index + 2]
        to_eval = ''.join(to_eval_list)
        result = eval(to_eval)

        if result == erg:
            ok = True
            print(f"Index: {index} right with {op_comb}")
            output += erg
            total += 1
            break
    if not ok:
        print(f"Index: {index} not right with {op_comb}")
        total += 1

    return total, output

def part_d(total, output, index, line, inp):
    ok = False
    erg = line.split(":")[0]
    erg = int(erg)
    arg = re.findall(r"\d+", line.split(":")[1])
    arg = [int(x) for x in arg]
    ops = ["+", "*", "||"]
    all_pos_op_comb = list(itertools.product(ops, repeat=len(arg) - 1))
    for op_comb in all_pos_op_comb:
        to_eval_list = []
        for i in range(len(arg) - 1):
            to_eval_list.append("(")
        for i in range(len(arg)):
            to_eval_list.append(str(arg[i]))
            if i > 0:
                app = True
                if i < len(op_comb):
                    if op_comb[i] == "||":
                        app = False
                if app:
                    to_eval_list.append(")")
            if i < len(op_comb):
                to_eval_list.append(op_comb[i])

        for ghg_index, ghg in enumerate(to_eval_list):
            if ghg == "||":
                to_eval_list[ghg_index - 1] = str(to_eval_list[ghg_index - 1]) + str(to_eval_list[ghg_index + 1])
                del to_eval_list[ghg_index:ghg_index + 2]

        # Ensure parentheses are balanced
        open_parens = to_eval_list.count("(")
        close_parens = to_eval_list.count(")")
        to_eval_list.extend(")" * (open_parens - close_parens))

        to_eval = ''.join(to_eval_list)
        result = eval(to_eval)

        if result == erg:
            ok = True
            print(f"Index: {index} right with {op_comb}")
            output += erg
            total += 1
            break
    if not ok:
        print(f"Index: {index} not right with {op_comb}")
        total += 1

    return total, output

def main(inp):
    one_total = 0
    one_output = 0
    two_total = 0
    two_output = 0
    for index, line in enumerate(inp):
        #one_total, one_output = part_one(one_total,one_output,index,line,inp)
        two_total, two_output = part_d(two_total,two_output,index,line,inp)

    #print("\n---\nTotal 1", one_output, f"in N={one_total}")
    print("\n---\nTotal 2", two_output, f"in N={two_total}")




test_inp = [
    "190: 10 19",
    "3267: 81 40 27",
    "83: 17 5",
    "156: 15 6",
    "7290: 6 8 6 15",
    "161011: 16 10 13",
    "192: 17 8 14",
    "21037: 9 7 18 13",
    "292: 11 6 16 20",
]

if __name__ == '__main__':
    main(test_inp)
    #main(load_input_file())