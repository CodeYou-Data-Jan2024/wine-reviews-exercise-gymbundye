# add your code here
import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
df = pd.read_csv('data/winemag-data-130k-v2.csv.zip', compression='zip')

# Calculate the summary data
summary = df.groupby('country').agg(count=('country', 'count'), points=('points', 'mean')).reset_index()
summary['points'] = summary['points'].round(1)

# Write the summary data to a new CSV file
summary.to_csv('data/reviews-per-country.csv', index=False)


# Read the CSV file
df = pd.read_csv('data/reviews-per-country.csv')

# Sort the data by count in descending order
df = df.sort_values(by='count', ascending=False)

# Create a bar chart
plt.figure(figsize=(10, 8))
plt.bar(df['country'], df['count'], color='red')
plt.xlabel('Country')
plt.ylabel('Number of Reviews')
plt.title('Number of Wine Reviews by Country')
plt.xticks(rotation=90)
plt.tight_layout()

# Display the chart
plt.show()

df = pd.read_csv('data/reviews-per-country.csv')

# Sort the data by points in descending order
df = df.sort_values(by='points', ascending=False)

# Create a bar chart
plt.figure(figsize=(10, 6))
plt.bar(df['country'], df['points'], color='purple')
plt.xlabel('Country')
plt.ylabel('Average Points')
plt.title('Average Wine Points by Country')
plt.xticks(rotation=90)
plt.tight_layout()

# Display the chart
plt.show()