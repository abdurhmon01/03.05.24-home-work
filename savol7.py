def print_star_pattern(rows):
    for i in range(1, rows + 1):
        print('* ' * i)
    for i in range(rows - 1, 0, -1):
        print('* ' * i)

rows = int(input())
print_star_pattern(rows)