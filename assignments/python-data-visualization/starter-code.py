# Starter Code: Python Data Visualization

import pandas as pd

# Choose one library path by uncommenting the section you want.
# --- Option A: matplotlib ---
import matplotlib.pyplot as plt

# --- Option B: plotly ---
# import plotly.express as px


# 1. Load your dataset
# Replace 'data.csv' with your file path.
df = pd.read_csv('data.csv')

# 2. Print a quick preview
print(df.head())
print(df.describe(include='all'))

# 3. Create charts (replace column names)
# Example matplotlib charts:
# plt.figure()
# df.plot(x='date', y='sales', kind='line', title='Sales Over Time')
# plt.xlabel('Date')
# plt.ylabel('Sales')
# plt.grid(True)
# plt.tight_layout()
# plt.savefig('line_chart.png')

# plt.figure()
# df.plot(x='category', y='value', kind='bar', title='Category Comparison')
# plt.xlabel('Category')
# plt.ylabel('Value')
# plt.tight_layout()
# plt.savefig('bar_chart.png')

# plt.figure()
# plt.scatter(df['x_value'], df['y_value'])
# plt.title('X vs Y')
# plt.xlabel('X')
# plt.ylabel('Y')
# plt.tight_layout()
# plt.savefig('scatter_plot.png')

# If using plotly, you can do:
# fig = px.line(df, x='date', y='sales', title='Sales Over Time')
# fig.write_html('line_chart.html')

print('Starter setup complete. Add your column names and chart logic.')
