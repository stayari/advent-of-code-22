
def main():
    input = open('../input/input3.txt', 'r').read()
    input_list = input.rstrip().split('\n')
    res = []
    i = 0
    while i < len(input_list):
        res.append(get_priority(get_common_badge(input_list[i:i+3])))
        i = i + 3
    print(sum(res))

def get_common_badge(rucksacks):
    common_badge = dict()
    list_of_set = []
    for rucksack in rucksacks:
        # Convert to set to remove duplicates
        for c in set(rucksack):
            # Check how many times each letter appears
            if c in common_badge:
                common_badge[c] += 1
            else:
                common_badge[c] = 0
    return(max(common_badge, key=common_badge.get))

def get_priority(c):
    # ASCII but upper and lower case reversed 
    return int(ord(c)) - 38 if c.isupper() else int(ord(c)) - 96

if __name__ == '__main__':
    main()
