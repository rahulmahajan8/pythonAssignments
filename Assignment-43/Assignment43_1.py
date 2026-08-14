import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# -------------------------------------------------
# Step 1: Get Data
# -------------------------------------------------

data = pd.read_csv("MarvellousInfosystems_PlayPredictor.csv")

print("Original Dataset:")
print(data)

# -------------------------------------------------
# Step 2: Clean, Prepare and Manipulate Data
# -------------------------------------------------

weather_encoder = LabelEncoder()
temperature_encoder = LabelEncoder()
play_encoder = LabelEncoder()

data["Weather"] = weather_encoder.fit_transform(data["Weather"])
data["Temperature"] = temperature_encoder.fit_transform(data["Temperature"])
data["Play"] = play_encoder.fit_transform(data["Play"])

print("\nEncoded Dataset:")
print(data)

X = data[["Weather", "Temperature"]]

Y = data["Play"]

# -------------------------------------------------
# Step 3: Train Data
# -------------------------------------------------

X_train, X_test, Y_train, Y_test = train_test_split(
    X,
    Y,
    test_size=0.5,
    random_state=42
)

K = 3

model = KNeighborsClassifier(n_neighbors=K)

model.fit(X_train, Y_train)

# -------------------------------------------------
# Step 4: Test Data
# -------------------------------------------------

print("\nEnter information for prediction")

print("\nWeather Options:")
print("1. Sunny")
print("2. Overcast")
print("3. Rainy")

weather_input = input("Enter Weather: ")

print("\nTemperature Options:")
print("1. Hot")
print("2. Mild")
print("3. Cool")

temperature_input = input("Enter Temperature: ")

weather_value = weather_encoder.transform([weather_input])[0]
temperature_value = temperature_encoder.transform([temperature_input])[0]

new_data = [[weather_value, temperature_value]]

prediction = model.predict(new_data)

result = play_encoder.inverse_transform(prediction)

print("\nPredicted Result:", result[0])

# -------------------------------------------------
# Step 5: Calculate Accuracy
# -------------------------------------------------

def CheckAccuracy(k):

    model = KNeighborsClassifier(n_neighbors=k)

    model.fit(X_train, Y_train)

    prediction = model.predict(X_test)

    accuracy = accuracy_score(Y_test, prediction)

    return accuracy * 100


print("\nAccuracy Results:")

for k in [1, 3, 5]:
    
    if k <= len(X_train):
        accuracy = CheckAccuracy(k)
        print("K =", k, "Accuracy =", accuracy, "%")
    else:
        print("K =", k, "is not possible with this training data")