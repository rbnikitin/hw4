import random

def checksum(x: list[int]) -> int:
  chsum = 0
  for i in x:
    chsum = (chsum + i) * 113
  chsum = chsum % 10000007
  return chsum
def is_prime(x: int) -> bool:
    if x <= 1:
        return False

    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True
def primes(count: int) -> list[int]:
    primes_list = []
    num = 1
    while len(primes_list) < count:
        if is_prime(num):
            primes_list.append(num)
        num += 1
    return primes_list

def pipeline() -> int:
    numbers = primes(1000)
    random.Random(100).shuffle(numbers)
    return checksum(numbers)

if __name__ == '__main__':
    exit(main())
