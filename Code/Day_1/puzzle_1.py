import pandas as pd

scrambled_values = pd.read_csv("scrambled_values.csv")
calibrated_total = 0
for value in scrambled_values["Scrambled Values"]:
    first = None
    last = None
    for character in value:
        print(character)
        if first is None and character.isnumeric():
            first = character
        if character.isnumeric():
            last = character
    calibrated_total += int(f"{first}{last}")
print(calibrated_total)
