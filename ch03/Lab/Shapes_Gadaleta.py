#A
for row in range(4):
    for col in range(row):
        print('*', end='')
    print()
print('\n\n')

# B
for row in range(4):
    for col in range(4 - row):
        print('*', end='')
    print()
print('\n\n')

#C
stars = 0
for row in range(4,1,-1):
    stars += 1
    spaces = row - stars
    for space in range(spaces):
        print(' ', end='')
    for star in range(stars):
        print('*',end='')
    print()
