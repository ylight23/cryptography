
# k is size of num[] and rem[].
# Returns the smallest number x
# such that:
# x % num[0] = rem[0],
# x % num[1] = rem[1],
# ..................
# x % num[k-2] = rem[k-1]
# Assumption: Numbers in num[]
# are pairwise coprime (gcd for
# every pair is 1)
def findMinX(num, rem, k):
	x = 1; # Initialize result

	# As per the Chinise remainder
	# theorem, this loop will
	# always break.
	while(True):
		
		# Check if remainder of
		# x % num[j] is rem[j]
		# or not (for all j from
		# 0 to k-1)
		j = 0
		while(j < k):
			if (x % num[j] != rem[j]):
				break
			j += 1

		# If all remainders
		# matched, we found x
		if (j == k):
			return x

		# Else try next number
		x += 1

# x%5=2 =>x=2mod5
# x%11=3 =>x=3mod11
# x%17=5 =>x=5mod17
# Driver Code
num = [5, 11, 17]
rem = [2, 3, 5]
k = len(num)
print("x is", findMinX(num, rem, k));



## CACH 2
## for i in range(5*11*17):
##  if i%5==2 and i%11==3 and i%17==5:
#       print(i)    
