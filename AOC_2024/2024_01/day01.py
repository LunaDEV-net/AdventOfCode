import sys

def load_input_file(path="input.txt"):
    with open(path) as f:
        return f.read()

def main():
    differenz_liste = []
    simi_liste = []
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
        differenz_liste.append(differenz)

    for i in range(0, len(data["l"])):
        left = data["l"][i]
        matches = [x for x in data["r"] if left == x]
        similarity_score = left * len(matches)
        simi_liste.append(similarity_score)


    ergebnis_differenz = 0
    for zahl in differenz_liste:
        ergebnis_differenz += zahl

    simil_ergbnis = 0
    for zahl in simi_liste:
        simil_ergbnis += zahl

    print(ergebnis_differenz)
    print(simil_ergbnis)

if __name__ == '__main__':
    main()