
def main():
    input = open('../input/input3.txt', 'r').read()
    input_list = input.rstrip().split('\n')
    res = []
    for rucksack in input_list:
        res.append(get_priority(get_duplicate_item(rucksack)))
    print(sum(res))

def get_duplicate_item(rucksack):
    comp_1 = rucksack[:len(rucksack)//2]
    comp_2 = rucksack[len(rucksack)//2:]
    for item in comp_2: 
        if item in comp_1:
            return item

def get_priority(c):
    return int(ord(c)) - 38 if c.isupper() else int(ord(c)) - 96

if __name__ == '__main__':
    main()
