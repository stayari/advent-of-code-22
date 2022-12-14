
def main():
    input = open('../input/input5.txt', 'r').read()
    boxes, instructions = input.rstrip().split('\n\n')
    ans = ''
    boxes = box_processer(boxes)

    for instruction in instructions.split('\n'):
        move_boxes_2(boxes, instruction)
    for box in boxes:
        if box: ans += str(box[0])
    return ans

def move_boxes(boxes, instruction):
    amount, frm, to = [int(s) for s in instruction.split() if s.isdigit()]
    for i in range(amount):
        to_move = boxes[frm-1].pop(0)
        boxes[to-1].insert(0, to_move)

def move_boxes_2(boxes, instruction):
    amount, frm, to = [int(s) for s in instruction.split() if s.isdigit()]
    boxes[to-1]= boxes[frm-1][:amount] + boxes[to-1]
    boxes[frm-1] = boxes[frm-1][amount:]

def box_processer(boxes):
    lists = [[] for i in range(len(boxes.split('\n')[0])//4 + 1)] # Creates empty lists
    for row in boxes.split('\n')[:-1]: # Skip last row since its only numbers
        for i, c in enumerate(row):
            if i % 4 == 1 and not c == ' ':
                lists[int((i - 1)/4)].append(c)
    return lists

if __name__ == '__main__':
    print(main())
