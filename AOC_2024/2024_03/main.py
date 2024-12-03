import re

txt = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"

def main(inp):
  q = "mul\([0-9]+?,[0-9]+?\)/g"
  all_mul = re.findall(q, inp)
  for mul in all_mul:
    print(mul)

if __name__ == "__main__":m 
  print("hi")
  main(txt)
