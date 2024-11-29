import pandas as pd

# URL of the Iris dataset
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"

# Define the column names (since the dataset doesn't have headers)
column_names = ["sepal_length", "sepal_width", "petal_length", "petal_width", "species"]

# Load the dataset from the URL
data = pd.read_csv(url, header=None, names=column_names)

# Display the first few rows
print("Iris Dataset:")
print(data.head())

# Perform basic data analysis
print("\nSummary Statistics:")
print(data.describe())
