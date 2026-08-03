# Python3 program to count number of ways to
# arrange three types of balls such that no
# two balls of same color are adjacent to each other
MAX = 100;

# table to store to store results of subproblems
dp = [[[[-1] * 4 for i in range(MAX)]
				for j in range(MAX)]
				for k in range(MAX)];

# Returns count of arrangements where last
# placed ball is 'last'. 'last' is 0 for 'p',
# 1 for 'q' and 2 for 'r'
def countWays(p, q, r, last):

	# if number of balls of any color becomes less
	# than 0 the number of ways arrangements is 0.
	if (p < 0 or q < 0 or r < 0):
		return 0;

	# If last ball required is of type P and the
	# number of balls of P type is 1 while number
	# of balls of other color is 0 the number of
	# ways is 1.
	if (p == 1 and q == 0 and
		r == 0 and last == 0):
		return 1;

	# Same case as above for 'q' and 'r'
	if (p == 0 and q == 1 and
		r == 0 and last == 1):
		return 1;
	if (p == 0 and q == 0 and
		r == 1 and last == 2):
		return 1;

	# If this subproblem is already evaluated
	if (dp[p][q][r][last] != -1):
		return dp[p][q][r][last];

	# if last ball required is P and the number
	# of ways is the sum of number of ways to
	# form sequence with 'p-1' P balls, q Q Balls
	# and r R balls ending with Q and R.
	if (last == 0):
		dp[p][q][r][last] = (countWays(p - 1, q, r, 1) +
							countWays(p - 1, q, r, 2));

	# Same as above case for 'q' and 'r'
	elif (last == 1):
		dp[p][q][r][last] = (countWays(p, q - 1, r, 0) +
							countWays(p, q - 1, r, 2));
	else:
		
		#(last==2)
		dp[p][q][r][last] = (countWays(p, q, r - 1, 0) +
							countWays(p, q, r - 1, 1));

	return dp[p][q][r][last];

# Returns count of required arrangements
def countUtil(p, q, r):
	
	# Three cases arise:
	# Last required balls is type P
	# Last required balls is type Q
	# Last required balls is type R
	return (countWays(p, q, r, 0) +
			countWays(p, q, r, 1) +
			countWays(p, q, r, 2));

# Driver Code
p, q, r = 1, 1, 1;
print(countUtil(p, q, r));

# This code is contributed by mits
