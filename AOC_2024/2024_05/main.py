import random, csv

def random_sort(arr):
    # Create a copy of the original array to avoid modifying it directly
    shuffled = arr.copy()

    # Use the Fisher-Yates shuffle algorithm
    for i in range(len(shuffled) - 1, 0, -1):
        j = random.randint(0, i)
        shuffled[i], shuffled[j] = shuffled[j], shuffled[i]

    return shuffled


def load_files(path_pages="pages_input.txt", path_rules="rules_input.txt"):
    # Read the rules from the rules file
    with open(path_rules, 'r') as f:
        rules = f.read().splitlines()

    # Read the pages using csv.reader and parse rows as integers
    pages = []
    with open(path_pages, 'r') as f:
        csv_reader = csv.reader(f, delimiter=',')
        for row in csv_reader:
            pages.append([int(num) for num in row])

    return pages, rules

def is_sorted(list, rules):
    for i, page in enumerate(list):
        if page in rules:
            for later_page in rules[page]:
                if later_page in list and list.index(later_page) < i:
                    #print(f"Unsorted: {list}")
                    return False
    #print(f"Sorted: {list}")
    return True


def main(rules, pages):
    rules_as_dict = {}
    output_sorted = 0
    output_unsorted = 0
    # Clean Up Rules
    for rule in rules:
        x, y = map(int, rule.split('|'))
        if x not in rules_as_dict:
            rules_as_dict[x] = []
        rules_as_dict[x].append(y)
    for index, page in enumerate(pages):
        print("Start ", index)
        if is_sorted(page, rules_as_dict):
            middle_index = len(page)//2
            output_sorted += page[middle_index]
        else:
            while not is_sorted(page, rules_as_dict):
                page = random_sort(page)
            middle_index = len(page)//2
            output_unsorted += page[middle_index]
        print("finished ", index)
    print("Sort", output_sorted)
    print("Unsort", output_unsorted)



testing_rules = [
    "47|53",
    "97|13",
    "97|61",
    "97|47",
    "75|29",
    "61|13",
    "75|53",
    "29|13",
    "97|29",
    "53|29",
    "61|53",
    "97|53",
    "61|29",
    "47|13",
    "75|47",
    "97|75",
    "47|61",
    "75|61",
    "47|29",
    "75|13",
    "53|13",
]
testing_pages = [
    [75,47,61,53,29],
    [97,61,53,29,13],
    [75,29,13],
    [75,97,47,61,53],
    [61,13,29],
    [97,13,75,29,47],
]

if __name__ == '__main__':
    pages, rules = load_files()
    main(rules, pages)
    #main(testing_rules, testing_pages)