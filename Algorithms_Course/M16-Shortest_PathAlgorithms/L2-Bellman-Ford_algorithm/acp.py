# Check if a given string is a Sum-String

def is_sum_string(s):
    n = len(s)

    def check(start, len1, len2):
        num1 = s[start:start + len1]
        num2 = s[start + len1:start + len1 + len2]

        # Avoid numbers with leading zeros
        if (len(num1) > 1 and num1[0] == '0') or (len(num2) > 1 and num2[0] == '0'):
            return False

        sum_str = str(int(num1) + int(num2))
        sum_len = len(sum_str)

        next_start = start + len1 + len2

        if next_start + sum_len > n:
            return False

        if s[next_start:next_start + sum_len] != sum_str:
            return False

        if next_start + sum_len == n:
            return True

        return check(start + len1, len2, sum_len)

    for len1 in range(1, n):
        for len2 in range(1, n - len1):
            if check(0, len1, len2):
                return True

    return False


# Driver Code
string = input("Enter a numeric string: ")

if is_sum_string(string):
    print("The given string is a Sum-String.")
else:
    print("The given string is NOT a Sum-String.")