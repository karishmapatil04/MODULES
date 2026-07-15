# Tallest Bar Scanner

# 1. Calculate Stock Profit
def stock_profit(prices):
    profit = 0

    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            profit += prices[i] - prices[i - 1]

    print("Maximum Profit =", profit)


# 2. Build Left Tallest Bar Array
def left_max_array(height):
    left = [0] * len(height)
    left[0] = height[0]

    for i in range(1, len(height)):
        left[i] = max(left[i - 1], height[i])

    print("Left Max Array:", left)
    return left


# 3. Build Right Tallest Bar Array
def right_max_array(height):
    n = len(height)
    right = [0] * n
    right[n - 1] = height[n - 1]

    for i in range(n - 2, -1, -1):
        right[i] = max(right[i + 1], height[i])

    print("Right Max Array:", right)
    return right


# 4. Rainwater Trapped
def rainwater(height):
    left = left_max_array(height)
    right = right_max_array(height)

    water = 0

    for i in range(len(height)):
        water += min(left[i], right[i]) - height[i]

    print("Total Rainwater Trapped =", water)


# Main Menu
while True:
    print("\n===== Tallest Bar Scanner =====")
    print("1. Calculate Stock Profit")
    print("2. Build Left Tallest Bar Array")
    print("3. Build Right Tallest Bar Array")
    print("4. Calculate Rainwater Trapped")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        prices = list(map(int, input("Enter stock prices: ").split()))
        stock_profit(prices)

    elif choice == 2:
        bars = list(map(int, input("Enter bar heights: ").split()))
        left_max_array(bars)

    elif choice == 3:
        bars = list(map(int, input("Enter bar heights: ").split()))
        right_max_array(bars)

    elif choice == 4:
        bars = list(map(int, input("Enter bar heights: ").split()))
        rainwater(bars)

    elif choice == 5:
        print("Program Ended.")
        break

    else:
        print("Invalid Choice!")