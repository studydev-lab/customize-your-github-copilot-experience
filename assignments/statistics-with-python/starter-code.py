# Starter Code: Statistics with Python

import numpy as np
import pandas as pd


# 1. Load data
# Replace 'data.csv' with the dataset for this assignment.
df = pd.read_csv('data.csv')

# 2. Quick exploration
print('Shape:', df.shape)
print('Columns:', list(df.columns))
print(df.head())
print('\nMissing values by column:')
print(df.isna().sum())

# 3. Choose a numeric column to analyze
# Replace 'your_numeric_column' with an actual column name.
column_name = 'your_numeric_column'
values = df[column_name].dropna().to_numpy()

# 4. Statistical calculations with numpy
mean_value = np.mean(values)
median_value = np.median(values)
std_value = np.std(values)
min_value = np.min(values)
max_value = np.max(values)
p75_value = np.percentile(values, 75)

print(f'\nStatistics for {column_name}:')
print('Mean:', mean_value)
print('Median:', median_value)
print('Std Dev:', std_value)
print('Min:', min_value)
print('Max:', max_value)
print('75th Percentile:', p75_value)

# 5. Add insight statements
# Example:
# print('Insight 1: ...')
# print('Insight 2: ...')
