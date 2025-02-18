import random


class Lottery:
    _count: int
    _max: int
    _all_numbers: list[int]

    def __init__(self, count:int=6, max:int=49):
        self._count = count
        self._max = max
        self._all_numbers = []

    def reset(self, count:int=6, max:int=49):
        self.__init__(count, max)

    
    def generate_and_draw(self):
        self._all_numbers = [num for num in range(1, self._max + 1)]
        numbers = []
        for i in range(0, self._count):
            random.shuffle(self._all_numbers)
            numbers.append(self._all_numbers.pop(random.randint(0, len(self._all_numbers) - 1)))
        return numbers
    
    def get_draws(self, count: int=6):
        draws = []
        for i in range(0, count):
            draws.append(self.generate_and_draw())
        return draws





def generate_game(count=6, max=49):
    all_numbers = [num for num in range(1, max + 1)]
    numbers = []
    for i in range(0, 6):
        random.shuffle(all_numbers)
        numbers.append(all_numbers.pop(random.randint(0, len(all_numbers) - 1)))
    return numbers


def get_games(game_count=7):
    games = []
    for i in range(0, game_count):
        games.append(generate_game())
    return games



