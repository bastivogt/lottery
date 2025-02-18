from sevo import lottery


print("*** Lottery Drawing Generator ***")
count = int(input("Enter the count of draws: "))
print("Your draws: \n")

lottery_game = lottery.Lottery()
lottery_game.generate_and_draw()


for index, item in enumerate(lottery_game.get_draws(count)):
    print(f"Draw #{index + 1}: {item}")