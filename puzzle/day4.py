
def main():
    input = open('../input/input4.txt', 'r').read()
    input_list = input.split('\n')
    ans_a = ans_b = 0

    for row in input_list: 
        if issubset(row):
            ans_a += 1
        if overlaps(row):
            ans_b += 1
    return ans_a, ans_b

def process(data):
    pair_1, pair_2 = data.split(',')
    min1, max1 = map(int, pair_1.split('-'))
    min2, max2 = map(int, pair_2.split('-'))
    return min1, max1, min2, max2

def issubset(pair):
    min1, max1, min2, max2 = process(pair)
    return (min1 <= min2 and max1 >= max2) or (min1 >= min2 and max1 <= max2)

def overlaps(pair):
    min1, max1, min2, max2 = process(pair)
    return not (max1 < min2 or max2 < min1)
 
if __name__ == '__main__':
    print(main())
