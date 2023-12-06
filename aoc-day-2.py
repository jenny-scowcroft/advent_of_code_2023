with open("aoc-day-2-input.txt") as game_results_file:
    game_results = game_results_file.read()

game_results_list = game_results.splitlines()

colour_dict = {
"red": 12,
"green": 13,
"blue": 14,
}

game_index_total = 0
power_total = 0

for line in game_results_list:
    [game, results] = line.split(":")
    game_index = int(game.split()[1])
    game_index_total += game_index
    results_list = results.split(";")
    game_possible = True
    min_cubes_dict = {
    "red": 0,
    "green": 0,
    "blue": 0,
    }
    red_list = []
    green_list = []
    blue_list = []
    game_possible = True

    for game in results_list:
        colour_picks = game.split(",")
        for colour_pick in colour_picks:
            colour_pick = colour_pick.strip()
            [number, colour] = colour_pick.split()
            number = int(number)
            if colour == "red":
                red_list.append(number)
            if colour == "green":
                green_list.append(number)
            if colour == "blue":
                blue_list.append(number)
            if number > colour_dict[colour] and game_possible:
                game_index_total -= game_index
                game_possible = False
    if red_list:
        min_cubes_dict["red"] = max(red_list)
    if green_list:
        min_cubes_dict["green"] = max(green_list)
    if blue_list:
        min_cubes_dict["blue"] = max(blue_list)

    power = 1
    for minimum in min_cubes_dict.values():
        power *= minimum
    power_total += power
print(f"Part one answer: {game_index_total}")
print(f"Part two answer: {power_total}")
