"""
Lab5E_DiceSimulartions_JakeGadaleta.py
Preforms various tests on dice data to answer questions as listed in teh Lab Doc
author: Jake Gadaleta
"""

import matplotlib.pyplot as plt
import numpy as np
import random
import seaborn as sns


def create_bar_chart(results, title, x_title, y_title):

    values, frequencies = np.unique(results, return_counts=True)

    sns.set_style('whitegrid')

    axes = sns.barplot(x=values, y=frequencies, palette='bright')
    axes.set_title(title)

    axes.set(xlabel=x_title, ylabel=y_title)

    axes.set_ylim(top=max(frequencies) * 1.1)


    for bar, frequency in zip(axes.patches, frequencies):
        text_x = bar.get_x() + float(bar.get_width() / 2)
        text_y = bar.get_height()
        text = f'{frequency:,}\n{frequency/len(results):.3%}'
        axes.text(text_x, text_y, text, fontsize=11, ha='center', va='bottom')

    plt.show()

def test():
    rolls = [random.randrange(1,7) for i in range(1_000)]
    title = f'Rolling a Six-Sided Die {len(rolls):,} times'

    create_bar_chart(rolls, title, 'Die Value', 'Frequency')


def q1():
    rolls = []

    for i in range(1_000):
        count = 0
        for h in range(5):
            if random.randint(1,6) == 1:
                count += 1
        rolls.append(count)

    title = "Chance of rolling 1's"
    create_bar_chart(rolls, title, 'Amount of 1\'s', 'Frequency')


def q2():
    trails = []

    for i in range(1_000):
        count = 0
        for h in range(25):
            if random.randint(1,6) == 1 and random.randint(1,6) == 1:
                count += 1
        trails.append(count)

    title = "Chances of Snake Eyes (24 trials)"
    create_bar_chart(trails, title, 'Snake Eyes amount', 'Frequency')


def q3():
    X = [i for i in range(4,11) if i != 7]
    results = []
    for i in range(1_000):
        for x in X:
            while(True):
                if random.randint(1,6) + random.randint(1,6) == 7:
                    results.append(7)
                    break
                
                if random.randint(1,6) + random.randint(1,6) == x:
                    results.append(x)
                    break

    title = "Chances of Winning Craps"
    create_bar_chart(results, title, 'Rolled Amount', 'Frequency')
        
    
if __name__ == "__main__":
    # test()
    q1()
    q2()
    q3()
    

