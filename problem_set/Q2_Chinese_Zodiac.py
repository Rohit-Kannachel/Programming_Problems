# the Chinese Zodiac revolves in a 60 year cycle composed of 5 elements and 12 animals
# for simplicity this is the model we will follow
# Elements: Fire, Earth, Metal, Water, Wood
# Animals: Rat, Ox, Tiger, Rabbit, Dragon, Snake, Horse, Sheep, Monkey, Rooster, Dog, Pig

# we will say that this is the order it follows: The animals cycle for 12 years under 1 element
# then repeat again under another element to produce 60 unique combinations. After 60 years the cycle will repeat

# e.g. 2000: year of the Fire Rat --> 2001: Fire Ox --> 2013: Earth Rat ....

# write a function that takes the year as the input and produces the Zodiac for that year
# output should be in the format "2000 is the year of the Fire Rat"
chinese_dict= {
    'animals': ["Rat","Ox","Tiger","Rabbit","Dragon","Snake","Horse","Goat","Monkey","Rooster","Dog","Pig"],
    'elements': ["Fire", "Earth", "Metal", "Water", "Wood"]
}
year=2000
def chinese_new_year(x):
    x = int(x)
    year = (x-2024) % 60
    result=[]
    for element in chinese_dict["elements"]:
        for animal in chinese_dict["animals"]:
            order = f"{element} {animal}"
            result.append(order)
    Zodiac = result[year]
    if x<2024:
        Messege = f"{x} was the year of the {Zodiac}"
    else:
        Messege = f"{x} is the year of the {Zodiac}"
    return Messege

Zodiac = chinese_new_year(input("Input a year to determine it's associated Zodiac: "))
print(Zodiac)