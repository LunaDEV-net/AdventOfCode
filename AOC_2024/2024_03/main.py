import re

txt = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
sec_txt = r"xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
hi = "mul(11,13)"



def load_input_file(path="input.txt"):
    with open(path) as f:
        return f.read()

def main(inp):
    ergebnis = 0
    data = []
    q = r"mul\(\d+,\d+\)"
    all_mul = re.findall(q, inp)
    for mul in all_mul:
        mul = re.split(r",", mul)
        left = int("".join(re.findall(r"\d", mul[0])))
        right = int("".join(re.findall(r"\d", mul[1])))
        data.append([left,right])
    print(data)
    for multi in data:
        ergebnis += multi[0]*multi[1]
    print(ergebnis)

def secound_level(inp):
    ergebnis = 0
    data = []
    q = r"mul\(\d+,\d+\)|do\(\)|don't\(\)"
    all_instrucs = re.findall(q, inp)
    print(all_instrucs)
    do_dont = True
    for instrc in all_instrucs:
        if instrc.startswith("mul"):
            if do_dont:
                l_r = re.split(r",", instrc)
                left = int("".join(re.findall(r"\d", l_r[0])))
                right = int("".join(re.findall(r"\d", l_r[1])))
                data.append([left, right])
        if instrc == "do()":
            do_dont = True
        elif instrc == "don't()":
            do_dont = False
    print(data)
    for multi in data:
        ergebnis += multi[0]*multi[1]
    print(ergebnis)

if __name__ == "__main__":
    #main(load_input_file())
    secound_level(load_input_file())
