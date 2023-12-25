with open("aoc-day-4-input.txt") as scratchcards_file:
    all_scratchcards = scratchcards_file.read()

split_scratchcards = all_scratchcards.splitlines()
score = 0

scratches = [1] * len(split_scratchcards)

for i, card in enumerate(split_scratchcards):
    numbers = (card.split(":")[1]).strip()
    (winning_numbers, my_numbers) = numbers.split("|")
    winning_numbers = winning_numbers.split()
    my_numbers = my_numbers.split()

    winning_numbers = [int(number) for number in winning_numbers]
    my_numbers = [int(number) for number in my_numbers]

    common_numbers = list(set(winning_numbers) & (set(my_numbers)))
    # Part One
    if len(common_numbers) > 0:
        card_score = 2**(len(common_numbers)-1)
        score += card_score

    # Part Two
    total_matches = 0
    for x in range(0, len(common_numbers)):
        total_matches += 1
        scratches[i + total_matches] += scratches[i]
        
print(f"Part One Score: {score}")
print(f"Part Two Total: {sum(scratches)}")
