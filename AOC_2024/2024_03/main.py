import re

txt = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"

def main(inp):
    data = []
    q = r"mul\(\d+,\d+\)"
    all_mul = re.findall(q, inp)
    for mul in all_mul:
        mul = re.split(r",", mul)
        left = re.findall(r"\d", mul[0])
        right = re.findall(r"\d", mul[1])
        print(left, right)
        data.append([left])
        print(mul)

if __name__ == "__main__":
    print("hi")
    main(txt)
