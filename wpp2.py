import random


random_integers = [random.randint(0, 1) for _ in range(100)]


max_run = 0
current_run = 0

for num in random_integers:
    if num == 0:
        current_run += 1
        if current_run > max_run:
            max_run = current_run
    else:
        current_run = 0

print("Generated List:", random_integers)
print("Longest Run of Zeros:", max_run)
