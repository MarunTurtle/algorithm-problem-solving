from itertools import permutations
import math

def solution(numbers):
    nums = set()
    for i in range(1, len(numbers) + 1):
        for p in permutations(numbers, i):
            num = int(''.join(p))
            nums.add(num)

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    return sum(1 for n in nums if is_prime(n))
