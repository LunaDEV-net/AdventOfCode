import re

txt = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
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

if __name__ == "__main__":
    print("hi")
    main(load_input_file())
