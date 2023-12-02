file = open("game_values.txt", "r")
games = file.readlines()
dice_variants = ["red", "green", "blue"]
red, green, blue = 12, 13, 14
valid_games = []

for i in range(len(games)):
    valid_game = False
    games[i] = games[i].replace(":", "").replace("\n", "").removeprefix(f"Game {i + 1} ")
    dice_pulls = list(games[i].split("; "))

    for pulls in dice_pulls:
        pull = list(pulls.split(", "))
        game_pulls = {"red": 0, "green": 0, "blue": 0}

        for dice in pull:
            dice_values = list(dice.split(" "))
            game_pulls[dice_values[1]] = int(dice_values[0])
            if red < game_pulls["red"] or green < game_pulls["green"] or blue < game_pulls["blue"]:
                valid_game = False
                break
            else:
                valid_game = True
        if not valid_game:
            break
    if valid_game:
        valid_games.append(i + 1)
        #testerman

print(sum(valid_games))
