# Water Jug Problem without Queue

# Jug A = 4L
# Jug B = 3L
# Goal = get 2L

a = 0
b = 0

while True:

    # Fill Jug B if empty
    if b == 0:
        b = 3
        print("Fill Jug B:", a, b)

    # Pour water from B to A
    transfer = min(b, 4 - a)
    a = a + transfer
    b = b - transfer

    print("Pour B -> A:", a, b)

    # Check goal
    if a == 2 or b == 2:
        print("Goal Reached!")
        break

    # If Jug A becomes full, empty it
    if a == 4:
        a = 0
        print("Empty Jug A:", a, b)
