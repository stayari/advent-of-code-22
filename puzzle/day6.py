
def main():
    input = open('../input/input6.txt', 'r').read()
    return get_marker(input)

def get_marker(input):
    marker = []
    window = 14
    for i, c in enumerate(input):
        if len(marker)  == window: return i
        while c in marker:
            marker.pop(0)
        marker.append(c)

if __name__ == '__main__':
    print(main())
