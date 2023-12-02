file = open("game_values.txt", "r")
games = file.readlines()
dice_variants = ["red", "green", "blue"]
lowest_values = []

for i in range(len(games)):
    valid_game = False
    games[i] = games[i].replace(":", "").replace("\n", "").removeprefix(f"Game {i + 1} ")
    dice_pulls = list(games[i].split("; "))
    game_pulls = {"red": 0, "green": 0, "blue": 0}
    for pulls in range(len(dice_pulls)):
        pull = list(dice_pulls[pulls].split(", "))

        for dice in range(len(pull)):
            dice_values = list(pull[dice].split(" "))
            if game_pulls[dice_values[1]] < int(dice_values[0]):
                game_pulls[dice_values[1]] = int(dice_values[0])
    print(dice_pulls)
    print(game_pulls)
    lowest_values.append([game_pulls["red"], game_pulls["green"], game_pulls["blue"]])
sum_of_powers = 0
print(len(lowest_values))
for i in range(len(lowest_values)):
    power = lowest_values[i][0] * lowest_values[i][1] * lowest_values[i][2]
    print(i + 1, lowest_values[i], power)
    sum_of_powers += power
print(sum_of_powers)


