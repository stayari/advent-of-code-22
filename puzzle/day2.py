
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
    
    print(points[1][1], "HEJHEJ")
    my_points = 0
    for game in input_list: 
        x = translate(game.split(' ')[0])
        y = translate(game.split(' ')[1])
        #print("here is x,y", x, y)
        round_points = points[x][y]
        print("This round i got", round_points)
        my_points = my_points + round_points
    print(my_points)

def translate(c):
    if ( c == 'A' ) or ( c == 'X' ): return 0
    if ( c == 'B' ) or ( c == 'Y' ): return 1
    if ( c == 'C' ) or ( c == 'Z' ): return 2
    return
# def play(opponent, outcome):
#     # X Lose
#     if outcome == 'X':
#     # Y Draw
#     if outcome == 'Y':
#     # Z Win
#     if outcome == 'Z':

if __name__ == '__main__':
    main()
