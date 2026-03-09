import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Load cleaned dataset
df = pd.read_csv(r"C:\Users\polka\OneDrive\Desktop\Tourist influx prediction\Preprocessed_Tourism_Dataset.csv")

# Select only tourism columns (exclude weather columns)
tourism_cols = [col for col in df.columns if 'quarter' in col.lower()]

# Extract year from column names
years = sorted(list(set([col.split('_')[0] for col in tourism_cols])))

yearly_totals = {}

for year in years:
    cols = [col for col in tourism_cols if year in col]
    yearly_totals[year] = df[cols].sum().sum()

# Plot
plt.figure()
plt.plot(list(yearly_totals.keys()), list(yearly_totals.values()))
plt.xlabel("Year")
plt.ylabel("Total Tourist Inflow")
plt.title("Year-wise Tourist Inflow Trend")
plt.xticks(rotation=45)
plt.show()

# Calculate total inflow per country
df['Total_Inflow'] = df[tourism_cols].sum(axis=1)

top10 = df[['Country_of_Nationality', 'Total_Inflow']].sort_values(
    by='Total_Inflow', ascending=False).head(10)

plt.figure()
plt.bar(top10['Country_of_Nationality'], top10['Total_Inflow'])
plt.xticks(rotation=90)
plt.title("Top 10 Countries by Tourist Inflow")
plt.xlabel("Country")
plt.ylabel("Total Tourist Inflow")
plt.show()

import seaborn as sns

numeric_df = df.select_dtypes(include=['number'])

plt.figure()
sns.heatmap(numeric_df.corr(), annot=False)
plt.title("Correlation Heatmap")
plt.show()

#weather vs Tourist inflow
plt.figure()
plt.scatter(df['average_temp(*c)'], df['Total_Inflow'])
plt.xlabel("Average Temperature")
plt.ylabel("Total Tourist Inflow")
plt.title("Temperature vs Tourist Inflow")
plt.show()

#Quarterly Distribution (Boxplot)
plt.figure()
df[tourism_cols].boxplot(rot=90)
plt.title("Quarterly Tourist Distribution")
plt.show()