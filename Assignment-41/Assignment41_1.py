import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# --------------------------------------------------
# Step 1: Get Data
# --------------------------------------------------

data = pd.read_csv("MarvellousInfosystems_PlayPredictor.csv")

print("Dataset:")
print(data)


# --------------------------------------------------
# Step 2: Clean, Prepare and Manipulate Data
# --------------------------------------------------

# Create LabelEncoder objects
weather_encoder = LabelEncoder()
temperature_encoder = LabelEncoder()
play_encoder = LabelEncoder()

# Convert Weather into numeric values
data["Weather"] = weather_encoder.fit_transform(data["Weather"])

# Convert Temperature into numeric values
data["Temperature"] = temperature_encoder.fit_transform(data["Temperature"])

# Convert Play into numeric values
data["Play"] = play_encoder.fit_transform(data["Play"])

print("\nEncoded Dataset:")
print(data)


# --------------------------------------------------
# Features and Target
# --------------------------------------------------

X = data[["Weather", "Temperature"]]
Y = data["Play"]


# --------------------------------------------------
# Step 3: Train Data
# --------------------------------------------------

# Use whole dataset for training as mentioned in assignment
K = 3

model = KNeighborsClassifier(n_neighbors=K)

model.fit(X, Y)

print("\nModel trained successfully.")


# --------------------------------------------------
# Step 4: Test Data
# --------------------------------------------------

print("\nEnter Weather and Temperature")

print("\nWeather:")
print("Sunny")
print("Overcast")
print("Rainy")

weather = input("Enter Weather: ")

print("\nTemperature:")
print("Hot")
print("Mild")
print("Cool")

temperature = input("Enter Temperature: ")


# Convert user input into numeric values
weather_value = weather_encoder.transform([weather])[0]
temperature_value = temperature_encoder.transform([temperature])[0]


# Create new data
new_data = [[weather_value, temperature_value]]


# Predict result
prediction = model.predict(new_data)


# Convert numeric result back to Yes/No
result = play_encoder.inverse_transform(prediction)


print("\nPredicted Result:", result[0])


# --------------------------------------------------
# Step 5: Calculate Accuracy
# --------------------------------------------------

def CheckAccuracy(k):

    X_train, X_test, Y_train, Y_test = train_test_split(
        X,
        Y,
        test_size=0.5,
        random_state=42
    )

    classifier = KNeighborsClassifier(n_neighbors=k)

    # Train model
    classifier.fit(X_train, Y_train)

    # Predict test data
    Y_pred = classifier.predict(X_test)

    # Calculate accuracy
    accuracy = accuracy_score(Y_test, Y_pred)

    return accuracy * 100


print("\nAccuracy:")

for k in [1, 3, 5]:

    accuracy = CheckAccuracy(k)

    print("K =", k, "Accuracy =", accuracy, "%")