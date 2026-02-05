import random

list_random_int = [random.randint(1, 10) for _ in range (100)]

print(sum(list_random_int))

print(sum(list_random_int) / len(list_random_int))