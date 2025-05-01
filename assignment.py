#Wine Quality Analysis - Red Wine Dataset 

# Task 1: Load and Explore the Dataset

import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

try: 
    df = pd.read_csv('winequality-red.csv', sep=';')
    print("Data loaded successfully.")
except FileNotFoundError:
    print("File not found. Please check the file path.")
    exit()
except Exception as e:
    print(f"An error occured: {e}")
    
print(df.head())

print("\nData Types: \n", df.dtypes)
print("\nMissing Values:\n", df.isnull().sum())

df_clean = df.dropna()

df.columns = df.columns.str.replace(' " ', '')

print("\nDataset shape after cleaning:", df_clean.shape)


# Task 2: Basic Data Analysis

print("\nBasic Statistics:\n", df_clean.describe())

#Grouping by quality and compute mean of numerical columns
grouped_quality = df_clean.groupby('quality').mean()
print("\nMean values grouped by wine quality:\n", grouped_quality)

#Observation: Check alcohol content by quality
print("\nAverage alcohol content by wine quality:\n", grouped_quality['alcohol'])


# Task 3: Data Visualization


sns.set(style="whitegrid")

#Line chart: Average alcohol content by quality

plt.figure(figsize=(8, 5))
sns.lineplot(x=grouped_quality.index, y=grouped_quality['alcohol'], marker='o')
plt.title('Average Alcohol Content by Wine Quality')
plt.xlabel('Wine Quality')
plt.ylabel('Average Alcohol (%)')
plt.show()

# Bar chart: Average volatile acidity by wine quality
plt.figure(figsize=(8,5))
sns.barplot(x=grouped_quality.index, y=grouped_quality['volatile acidity'], palette='viridis')
plt.title('Average Volatile Acidity by Wine Quality')
plt.xlabel('Wine Quality')
plt.ylabel('Volatile Acidity')
plt.show()

# Histogram: Distribution of Alcohol Content
plt.figure(figsize=(8,5))
plt.hist(df_clean['alcohol'], bins=20, color='skyblue', edgecolor='black')
plt.title('Distribution of Alcohol Content')
plt.xlabel('Alcohol (%)')
plt.ylabel('Frequency')
plt.show()

# Scatter plot: Alcohol vs. Density
plt.figure(figsize=(8,5))
sns.scatterplot(x='alcohol', y='density', data=df_clean, hue='quality', palette='coolwarm')
plt.title('Alcohol vs. Density (colored by Quality)')
plt.xlabel('Alcohol (%)')
plt.ylabel('Density')
plt.legend(title='Quality')
plt.show()

# Findings/Observations
print("""
      Findings: 
      - Higher quality wines generally have higher alcohol content.
      - Volatile acidity tends to decrease with increasing quality.
      - Alcohol content is mostly distributed between 8% and 14%.
      - There appears to be a negative relationship between alcohol and density; higher alcohol wines tend to have lower density.
      """)
      