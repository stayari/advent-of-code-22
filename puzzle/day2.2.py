
test = """A Y
B X
C Z
"""
def main():
    input = open('../input/input2.txt', 'r').read()
    input_list = input.rstrip().split('\n')
    #print(test)
  # A X Rock    1p
  # B Y Paper   2p
  # C Z Scissor 3p

  #   X  Y  Z
  # A 4  8  3
  # B 1  5  9 
  # C 7  2  6
    points = [[4, 8, 3 ],
                [1, 5, 9 ],
                [7, 2, 6 ]]
    
    my_points = 0
    for game in input_list: 
        x = game.split(' ')[0]
        y = game.split(' ')[1]
        pl = play(x, y)

        round_points = points[translate(x)][translate(pl)]
        print("This round i got", round_points)
        my_points = my_points + round_points
    print(my_points)

def translate(c):
    if ( c == 'A' ) or ( c == 'X' ): return 0
    if ( c == 'B' ) or ( c == 'Y' ): return 1
    if ( c == 'C' ) or ( c == 'Z' ): return 2
    return
def play(opponent, outcome):
    # X Lose
    if outcome == 'Z':
        if(opponent == 'A'): return 'B'
        if(opponent == 'B'): return 'C'
        if(opponent == 'C'): return 'A'
    # Y Draw
    if outcome == 'Y':
        return opponent
    # Z Win
    if outcome == 'X':
        if(opponent == 'A'): return 'C'
        if(opponent == 'B'): return 'A'
        if(opponent == 'C'): return 'B'

if __name__ == '__main__':
    main()
