import sys

def load_input_file(path="input.txt"):
    with open(path) as f:
        return f.read()

def main():
    ergebnis_liste = []
    data={"l": [], "r": []}
    data_in = load_input_file()
    # Split the Line into to numbers
    for line in data_in.splitlines():
        zahl_pro_line = line.split("   ")
        data["l"].append(int(zahl_pro_line[0]))
        data["r"].append(int(zahl_pro_line[1]))
    # sort the to
    data["l"] = sorted(data["l"])
    data["r"] = sorted(data["r"])

    if len(data["l"]) != len(data["r"]):
        sys.exit()

    for i in range(0, len(data["l"])):
        differenz = abs(data["l"][i] - data["r"][i])
        ergebnis_liste.append(differenz)

    ergebnis = 0
    for zahl in ergebnis_liste:
        ergebnis += zahl

    print(ergebnis)

if __name__ == '__main__':
    main()