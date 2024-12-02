import csv
from os import sep
import numpy as np
import pandas as pd

file_name = 'input.csv'

df = pd.read_csv(file_name, header=None, names=('list_a', 'list_b'), delimiter="   ", engine = 'python')

# part 1 - distance between numbers

sorted_df = df.apply(lambda x: x.sort_values().values)
sorted_df['distance'] = abs(sorted_df['list_a'] - sorted_df['list_b'])
total_distance = sorted_df['distance'].sum()

print("part 1 solution is:", total_distance)

# part 2 - similarity score

left_column = sorted_df['list_a']
right_column = sorted_df['list_b']

similarity_score = 0

for value in sorted_df['list_a']:
  count = sorted_df['list_b'].value_counts().get(value,0)
  similarity_score = similarity_score + count * value

print("part 2 solution is:", similarity_score)




