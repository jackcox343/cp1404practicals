COLOUR_TO_CODE = {"absolute zero": "#0048ba", "acid green": "#b0bf1a", "aliceblue": "#f0f8ff",
                  "alizarin crimson": "#e32636", "amaranth": "#e52b50",
                  "amber": "#ffbf00", "amethyst": "#9966cc", "antiqueWhite": "#faebd7", "antiquewhite1": "#ffefdb",
                  "antiquewhite2": "#eedfcc"}

colour_name = input("Colour name: ").lower()
while colour_name != "":
    if colour_name in COLOUR_TO_CODE:
        print(f"The name {colour_name} gives the {COLOUR_TO_CODE[colour_name]}")
    else:
        print("Invalid colour name")
    colour_name = input("Colour name: ").lower()