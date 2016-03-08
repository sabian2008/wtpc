"""
Finds prime max divisor
"""

# Lib import
import math

# Target number
target = 600851475143
targetsqrt = math.sqrt(target)

# Known primes
primes = [2,3,5,7,11,13,17,19,23,29]

# Current divisor index (starts at three because odd)
current = 1

# Enlarge prime collection on demand
def next_prime():
	now = primes[-1] + 2 # It has to be, at least, the next odd
	while (True):
		if all(not now % item == 0 for item in primes): # Check if any prime can divide it
			primes.append(now)
			return 1
		else:
			now += 2

maxdivisor = 3
while(True):
	if primes[current] > target:
		break
	elif target % primes[current] == 0:
		target = target / primes[current]
		targetsqrt = math.sqrt(target)
		maxdivisor = primes[current]
	elif current == len(primes) -1:
		next_prime()
		current += 1
	else:
		current += 1


print max([primes[-1], target])
