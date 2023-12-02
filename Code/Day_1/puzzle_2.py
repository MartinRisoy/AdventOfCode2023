import pandas as pd


integer_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
number_list = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
scrambled_values = pd.read_csv("scrambled_values.csv")
calibrated_total = 0

for value in scrambled_values["Scrambled Values"]:
    first = None
    last = None
    for i in range(len(value)):
        if value[i].isnumeric() and int(value[i]) in integer_list:
            if first is None:
                first = value[i]
            last = value[i]

        if i <= (len(value) - 3) and (word := str(value[i] + value[i + 1] + value[i + 2])) in number_list:
            if first is None:
                first = number_list.index(word)
            last = number_list.index(word)

        if i <= (len(value) - 4) and (word := str(value[i] + value[i + 1] + value[i + 2] + value[i + 3])) in number_list:
            if first is None:
                first = number_list.index(word)
            last = number_list.index(word)

        if i <= (len(value) - 5) and (word := str(value[i] + value[i + 1] + value[i + 2] + value[i + 3] + value[i + 4])) in number_list:
            if first is None:
                first = number_list.index(word)
            last = number_list.index(word)

    calibrated_total += int(f"{first}{last}")
print(calibrated_total)
