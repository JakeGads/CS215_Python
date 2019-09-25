max_size = int(input('How large would you like the triangles:\t')) + 1
max_size_s = max_size - 1
#A
for row in range(max_size):
    for col in range(row):
        print('*', end='')
    print()
print('\n\n')

# B 
for row in range(max_size):
    for col in range(max_size - row -1):
        print('*', end='')
    print()
print('\n\n')

#C 
for row in range(max_size):
    for space in range(max_size_s - (max_size_s-row)):
        print(' ', end='')
    for star in range(max_size_s - row):
        print('*', end='')
    print()
print('\n\n')

#D
for row in range(max_size):
    for space in range(max_size - row):
        print(' ', end='')
    for star in range(max_size - (max_size-row)):
        print('*', end='')
    print()


'''
    /\\     # 4, /, 0, \\
   /  \\    # 3, /, 2, \\
  /    \\   # 2, /, 4, \\
 /      \\  # 1, / ,6, \\
/________\\ # 0, /, 8, \\
'''

print('\n\n')

space = 0
for i in range(max_size):
    for h in range(max_size - i):
        print(' ', end='')
    print('/', end='')
    for h in range(space):
        if i is not max_size - 1:
            print('  ', end='')
        else:
            print('__', end='')
    space += 1
    print('\\')

