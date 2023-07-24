def print_border_line(n):
    print('*' * n + ' ' * (2*n-3) + '*' * n)

def print_mid_line(line, n):
    first_piece = ' ' * line + '*' + ' '* (n-2) + '*' # 1/3 조각
    second_piece = ' '*(2*n-3 - 2*line) # 2/3 조각
    third_piece = '*' + ' '* (n-2) + '*'    #3/3 조각
    print(first_piece+second_piece+third_piece)

def print_center_line(center_line, n):
    print(' ' * center_line + '*' + ' '*(n-2) + '*' + ' ' * (n-2) + '*')

def print_star(n):
    lines = 2*n - 1
    center_line = n - 1
    for line in range(lines):
        # 양끝
        if line == 0 or line == lines-1:
            print_border_line(n)
        # 위쪽 가운데
        elif line > 0 and line < center_line:
            print_mid_line(line, n)
        # 아래쪽 가운데
        elif line > center_line and line < lines-1:
            line_mod = 2*n-2 - line
            print_mid_line(line_mod, n)
        # 정가운데
        else:
            print_center_line(line, n)

n = int(input())
print_star(n)
