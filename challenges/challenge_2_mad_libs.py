"""
Mad Libs
"""

# Todo: prompt the user to provide the missing words
colour = input("Colour:").strip().upper()
adjective = input("Adjective:").strip().upper()

text = f"""
Roses are {colour},
Violets are blue,
Sugar is {adjective},
And so are you!
"""

# Todo: print the final text
print(text.format(colour, adjective))
