def square_and_separate(start, end):
    """
    Create a list of square values between start and end,
    then separate them into even and odd lists.
    """
    squares = []
    even_squares = []
    odd_squares = []

    for num in range(start, end + 1):
        square = num ** 2
        squares.append(square)

        if square % 2 == 0:
            even_squares.append(square)
        else:
            odd_squares.append(square)

    return squares, even_squares, odd_squares


# Taking input from user
start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

if start > end:
    print("Error: Starting number should be less than or equal to ending number.")
else:
    squares, even_squares, odd_squares = square_and_separate(start, end)

    print("List of square values:", squares)
    print("Even square values:", even_squares)
    print("Odd square values:", odd_squares)