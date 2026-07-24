import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("netflix_titles.csv")
#Inspect the DataFrame with .info(), .describe(), and .head()
#print(df.head()) 
#print(df.info())
#print(df.decribe())
#print(df.isnull().sum())
df = df.drop_duplicates()

#print(df)
#Identify and handle missing values column by column
for col in df.columns:
    if  df[col].isnull().any():
        df[col] = df[col].fillna(df[col].mode()[0])
print(df.isnull().sum())
#Fix mixed-type columns (e.g., duration stored as "90 min")
# Create separate columns
df["duration_value"] = df["duration"].str.extract(r"(\d+)").astype(float)
df["duration_unit"] = df["duration"].str.extract(r"(min|Season|Seasons)")

print(df[["duration", "duration_value", "duration_unit"]].head())
#Parse date columns into proper datetime objects
# Convert date column
df.to_csv('cleaned_dataset.csv', index = False)