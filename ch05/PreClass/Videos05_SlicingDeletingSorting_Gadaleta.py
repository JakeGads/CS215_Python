numbers = [2,3,4,7,11,113,17,19]
numbers[2:6]
numbers[:6]
numbers[6:]
numbers[:]
numbers[::2]
numbers[::-1]
numbers[-1:-9:-1]
numbers[0:3] = ['two', 'three', 'five']
numbers
numbers[0:3] = []
numbers
numbers[::2] = [100, 100, 100]
numbers
id(numbers)
numbers[:] = []
id(numbers)
numbers = list(range(10))
del numbers[-1]
del numbers[0:2]
del numbers[::2]
numbers = list(range(17))
numbers
numbers.sort()
numbers
numbers.sort(reverse=True)
numbers
acending_numbers = sorted(numbers)
acending_numbers
letters = "sdakljfklsdjfklcjawejisdfjc"
acending_letters = sorted(letters)
acending_letters
colors = ('red', 'blue', 'yello')
acendingcolors = sorted(colors)