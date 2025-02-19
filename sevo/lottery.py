import random


class Lottery:
    _count: int
    _max: int
    _all_numbers: list[int]

    def __init__(self, count: int = 6, max: int = 49) -> None:
        self._count = count
        self._max = max
        self._all_numbers = []

    def reset(self, count: int = 6, max: int = 49) -> None:
        self.__init__(count, max)

    
    def generate_and_draw(self) -> list[int]:
        self._all_numbers = [num for num in range(1, self._max + 1)]
        numbers: list[int] = []
        for i in range(0, self._count):
            random.shuffle(self._all_numbers)
            numbers.append(self._all_numbers.pop(random.randint(0, len(self._all_numbers) - 1)))
        return numbers
    
    def get_draws(self, count: int=6) -> list[list[int]]:
        draws: list[list[int]] = []
        for i in range(0, count):
            draws.append(self.generate_and_draw())
        return draws