def longestPalin(S):
	# Get length of input String
	n = len(S)
	
	# All subStrings of length 1
	# are palindromes
	maxLength = 1
	start = 0
	
	# Nested loop to mark start
	# and end index
	for i in range(n):
		for j in range(i, n):
			flag = 1
			
			# Check palindrome
			for k in range(0, ((j - i) // 2) + 1):
				if (S[i + k] != S[j - k]):
					flag = 0

			# Palindrome
			if (flag != 0 and (j - i + 1) > maxLength):
				start = i
				maxLength = j - i + 1
				
	result = ""
	for i in range(start, start + maxLength):
		result = result+S[i]
	return result
#longestPalin("addaa")



