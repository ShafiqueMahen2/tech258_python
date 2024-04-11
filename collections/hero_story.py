story1 = {
    "start": "In a small village, a humble blacksmith named Gareth works away at his forge, dreaming of an adventure.",
    "middle": "A messenger brings news of a dragon invading, fuelling Gareth with the courage to confront the beast.",
    "end": "After a fierce battle, Gareth emerges victorious and returns home a hero, forever changed by this encounter and regarded as a hero by the townspeople."
}

# Print the entire dictionary
print(story1)

# Print the type of dictionary
print(type(story1))

# Print only the keys
print(story1.keys())

# Print only the values
print(story1.values())

# Print the individual values using the keys
print(story1["start"])
print(story1["middle"])
print(story1["end"])

# Add a new key:value pair --> 'hero': your_super_hero
story1["hero"] = "Gareth the Brave"
print(story1["hero"])
