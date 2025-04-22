import math


points = []
for i in range(10):
    x = float(input(f"Enter x-coordinate for point {i + 1}: "))
    y = float(input(f"Enter y-coordinate for point {i + 1}: "))
    z = float(input(f"Enter z-coordinate for point {i + 1}: "))
    points.append((x, y, z))


nearest_neighbors = []

for i in range(len(points)):
    min_distance = float('inf')
    nearest_point = None
    for j in range(len(points)):
        if i != j:
            distance = math.sqrt((points[i][0] - points[j][0]) ** 2 +
                                 (points[i][1] - points[j][1]) ** 2 +
                                 (points[i][2] - points[j][2]) ** 2)
            if distance < min_distance:
                min_distance = distance
                nearest_point = points[j]
    nearest_neighbors.append((points[i], nearest_point))


print("\nPoint and its nearest neighbor:")
for point, neighbor in nearest_neighbors:
    print(f"Point: {point} -> Nearest Neighbor: {neighbor}")
