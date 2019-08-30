"""
2.14 (TARGET HEART-RATE CALCULATOR) 
While exercising, you can use a heart-rate monitor to see that your heart rate stays 
within a safe range suggested by your doctors and trainers. 
According to the American Heart Association (AHA) (http://bit.ly/AHATargetHeartRates), 
the formula for calculating your maximum heart rate in beats per minute is 220 minus your age in years. 
Your target heart rate is 50–85% of your maximum heart rate. 
Write a script that prompts for and inputs the user’s age and calculates and displays the user’s maximum 
heart rate and the range of the user’s target heart rate. 
[These formulas are estimates provided by the AHA; maximum and target heart rates may vary based on the health, 
fitness and gender of the individual. Always consult a physician or qualified healthcare professional 
before beginning or modifying an exercise program.]
"""

# Will and I wanted to see who could do it in the least amount of lines
user_age = int(input("What is your Age\t"))
print("\n\nUser Age: {age}\nMax Heart Rate: {max}\n\tLow Range:\t{low}\n\tHigh Range:\t{high}".format(age=user_age, max=(220-user_age), low=round(((220-user_age) * .50),2), high=round(((220-user_age) *.85))))


user_maxBBM = 220 - user_age
healthy_max = user_maxBBM * .85
healthy_min = user_maxBBM * .5

print(
    """
    User Age:\t\t{age}
    Max Heart Rate:\t{max} BBM
    \tLow Range:\t{low} BBM
    \tHigh Range:\t{high} BBM
    """.format(
        age = user_age,
        max = user_maxBBM,
        low = round(healthy_min,2),
        high = round(healthy_max,2),
    )
)