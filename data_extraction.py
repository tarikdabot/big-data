import pandas as pd

# Load the dataset (use the correct file path)
df = pd.read_csv("../data/bigdatasate.csv")  # Relative path for local machine

# Display the first 5 rows of the dataset

print(df.head(10))

# Check the number of rows and columns
print(df.shape)