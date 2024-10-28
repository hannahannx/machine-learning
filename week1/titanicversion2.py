# MY EXAMPLE


# Import pandas for data manipulation
import pandas as pd

# 1. Load the sample Titanic dataset from CSV file
url = r"/Users/hannah-ann/PycharmProjects/machine-learning/week1/titanic_sample.csv"  # Use raw string or forward slashes
df = pd.read_csv(url) # df stands for data frame

# 2. Inspect the dataset
print("Original dataset:")
print(df)

# 3. Handle missing values
# - Fill missing 'Age' with the median age
    # how would I change the bellow into this format to include the median
    # For example, when doing 'df[col].method(value, inplace=True)', try using 'df.method({col: value}, inplace=True)' or
    # df[col] = df[col].method(value) instead, to perform the operation inplace on the original object.
df['Age'].fillna(df['Age'].median(), inplace=True)

# - Drop the 'Cabin' column because it has too many missing values
df.drop('Cabin', axis=1, inplace=True)

# 3. Display the cleaned dataset
print("\nCleaned dataset:")
print(df)

# 4. Save the cleaned dataset to a new CSV file
df.to_csv("/Users/hannah-ann/PycharmProjects/machine-learning/week1/cleaned_titanic_sample.csv", index=False)

# 5. Final Review
    # The changes made in this data set
        # The cabin column had too many empty values so we dropped it, the age column had only 2 missing values so we put the average in both of these values
        # We then created a new file with the new information