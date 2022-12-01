
def main():
    input = open('../input/input1.txt', 'r').read()
    input_list = input.rstrip().split('\n')

    total_cal = 0
    # List of each elfs calories
    cal_list = []
    max_cal = 0
    # List of the 
    max_list = []
    for cal in input_list: 
        if cal: 
            total_cal = total_cal + int(cal)
        else:
            cal_list.append(total_cal)
            if total_cal > max_cal: 
                max_cal = total_cal
                max_list.append(max_cal)
            total_cal = 0
    print(max_cal)
    three_max = sum(sorted(cal_list)[-3:])
    
    print(three_max)

    return



if __name__ == '__main__':
    main()
