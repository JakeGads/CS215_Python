"""
TemputureConversion_Gadaleta.py
Takes in temperatures in c and converts it to f, 4.9 in the text book
@author Jake Gadaleta (Python Genius)
"""


"""
4.9 (TEMPERATURE CONVERSION) 
Implement a fahrenheit function that returns the Fahrenheit equivalent of a Celsius temperature. 

Use the following formula:
F = (9 / 5) * C + 32

Use this function to print a chart showing the Fahrenheit equivalents of all Celsius temperatures in the range 0–100 degrees. 
Use one digit of precision for the results. Print the outputs in a neat tabular format
"""


def convert_temp(c):
    """takes in a Celsius temperature and converts it Fahrenheit"""
    return (9 / 5) * c + 32  # uses the provided formula


if __name__ == "__main__":
    print("C\tF")  # header
    for c in range(101):  # for statement that runs between 0 and 100
        print(
            f"{c}\t{convert_temp(c):.2f}"
        )  # prints the currect celsius and the converted fahrenheit
