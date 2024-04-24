import pandas as pd
import sys

# Validate command line input
args = sys.argv
if len(args) != 2:
    print('ERROR: Invalid input')
    print('Usage: prune_ratings.py [P]')
    print('P: percentage of original ratings to take (0 <= P <= 100)')
    sys.exit()

p = float(args[1])
if p < 0 or p > 100:
    print('ERROR: Invalid input')
    print('Usage: prune_ratings.py [P]')
    print('P: percentage of original ratings to take (0 <= P <= 100)')
    sys.exit()

# Read in original data and take p% of data as a random sample
ratings = pd.read_csv('./ratings.dat',delimiter=',',names=['UserID', 'MovieID', 'Rating', 'Timestamp'],engine='python')
num_samples = int(p / 100 * ratings.shape[0])
small_ratings = ratings.sample(n=num_samples)

# Write to file
OUTPUT_PATH = 'ratings' + str(p) + '.dat'
pd.DataFrame.to_csv(small_ratings, OUTPUT_PATH, index=False, header=False)
