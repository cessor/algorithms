from shuffle import shuffle
import sys

if len(sys.argv) < 2:
	print 'Usage: ', __file__, '<count>'
	exit()

count = int(sys.argv[1])
print ','.join(str(c) for c in shuffle(range(count)))