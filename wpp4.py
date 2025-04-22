
equivalence_classes = [[] for _ in range(5)]

for num in range(1, 10001):
    remainder = num % 5
    equivalence_classes[remainder].append(num)


valid = True
all_numbers = set()
for eq_class in equivalence_classes:
    all_numbers.update(eq_class)


original_set = set(range(1, 10001))
if all_numbers != original_set:
    valid = False


print("Equivalence Classes for Modulo 5:")
for i, eq_class in enumerate(equivalence_classes):
    print(f"Class {i}: {eq_class[:10]} ... (total {len(eq_class)} elements)")

print("\nAre the equivalence classes valid? ", "Yes" if valid else "No")
