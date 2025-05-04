squares = [num ** 2 for num in range(1, 11)]

for num, square in enumerate(squares, start=1):
    print(f"Number: {num}, Square: {square}")