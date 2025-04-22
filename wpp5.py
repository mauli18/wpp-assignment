
student_names = []


for i in range(10):
    while True:
        name = input(f"Enter the name of student {i + 1}: ")
        if len(name) <= 15:
            student_names.append(name)
            break
        else:
            print("Name exceeds 15 characters. Please enter a shorter name.")


reversed_names = [name[::-1] for name in student_names]

print("\nReversed names of students:")
for name in reversed_names:
    print(name)
