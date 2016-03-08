"""
Sums odd Fobonnacci numbers which it's highest value is lower than 1.000.000
"""

# Set up variables
fibonnacci=[1,2]
length = len(fibonnacci)
summed = 1

# Calculate fibonnacci numbers
while(fibonnacci[-1] < 1e6):
	fibonnacci.append(fibonnacci[-1] + fibonnacci[-2])
	if not fibonnacci[-1] % 2 == 0:
		summed += fibonnacci[-1]

# Print result
print (summed)
