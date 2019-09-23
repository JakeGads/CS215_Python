'''
Organisms
Jake Gadaleta
9/22/19
'''

starting_num_organisms = int(input('Starting number of organisms: '))
daily_increase_percentage = int(input('Average daily increase (as a percent): ')) / 100
num_days = int(input("Number of days to multiply: "))


current_organisms = starting_num_organisms


print('Days Approximate\tPopulation')
print(f'0\t\t\t{starting_num_organisms}')
for i in range(num_days):
    current_organisms += (current_organisms * daily_increase_percentage)
    print(f'{i + 1}\t\t\t{current_organisms:.2f}')


current_organisms = starting_num_organisms
counter = 0 # This is for the while loop


print('\n\nDays Approximate\tPopulation')
print(f'0\t\t\t{starting_num_organisms}')
while counter < num_days:
    current_organisms += (current_organisms * daily_increase_percentage)
    print(f'{counter+1}\t\t\t{current_organisms:.2f}')
    counter += 1