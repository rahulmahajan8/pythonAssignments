import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Step 1: Get Data
df = pd.read_csv("Advertising.csv")


df = df.drop("Unnamed: 0", axis=1)

print("Dataset:")
print(df)

# Step 2: Clean, Prepare and Manipulate Data


X = df[["TV", "radio", "newspaper"]]

Y = df["sales"]

# Step 3: Train Data


X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.5, random_state=42
)

model = LinearRegression()


model.fit(X_train, Y_train)

# Step 4: Test the Data


Y_pred = model.predict(X_test)

# Step 5: Display predicted and expected values

print("\nPredicted Values:")
print(Y_pred)

print("\nExpected Values:")
print(Y_test.values)