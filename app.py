from sevo import lottery

print("*********************************")
print("*** Lottery Drawing Generator ***")
print("*********************************\n")

count: int = int(input("Enter the count of draws: "))
print("\nYour draws: \n")

lottery_game: lottery.Lottery = lottery.Lottery()
lottery_game.generate_and_draw()


for index, item in enumerate(lottery_game.get_draws(count)):
    print(f"Draw #{index + 1}: {item}")