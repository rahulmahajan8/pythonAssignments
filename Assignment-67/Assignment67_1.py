# Customer Churn Prediction using Neural Network

import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# --------------------------------------------------
# 1. Create Dataset
# --------------------------------------------------

X = np.array([
    [25, 500, 12, 1, 2],
    [30, 700, 24, 0, 1],
    [45, 1200, 6, 5, 8],
    [50, 1500, 5, 6, 10],
    [28, 600, 18, 1, 1],
    [35, 800, 30, 0, 0],
    [48, 1400, 4, 7, 9],
    [52, 1600, 3, 8, 12],
    [27, 550, 20, 0, 1],
    [42, 1300, 8, 4, 7]
])

y = np.array([
    0, 0, 1, 1, 0,
    0, 1, 1, 0, 1
])

# --------------------------------------------------
# 2. Feature Meaning
# --------------------------------------------------
# [Age, Monthly Charges, Tenure, Complaints, Support Calls]

# 0 = Customer will stay
# 1 = Customer will leave

# --------------------------------------------------
# 3. Clean Dataset
# --------------------------------------------------

print("Missing values in X:", np.isnan(X).sum())
print("Missing values in y:", np.isnan(y).sum())

# --------------------------------------------------
# 4. Split Dataset
# --------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# --------------------------------------------------
# 5. Apply StandardScaler
# --------------------------------------------------

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# --------------------------------------------------
# 6. Create FNN Model
# --------------------------------------------------

model = Sequential()

model.add(Dense(16, input_dim=5, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

# --------------------------------------------------
# 7. Compile Model
# --------------------------------------------------

model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)

# --------------------------------------------------
# 8. Train Model
# --------------------------------------------------

model.fit(
    X_train,
    y_train,
    epochs=100,
    batch_size=2,
    verbose=1
)

# --------------------------------------------------
# 9. Evaluate Accuracy
# --------------------------------------------------

loss, accuracy = model.evaluate(X_test, y_test, verbose=0)

print("\nTest Accuracy:", accuracy * 100, "%")

# --------------------------------------------------
# 10. Test New Customer
# --------------------------------------------------

new_customer = np.array([
    [46, 1450, 5, 6, 9]
])

# Scale test input
new_customer_scaled = scaler.transform(new_customer)

# Prediction
prediction = model.predict(new_customer_scaled)

print("\nPrediction Probability:", prediction[0][0])

if prediction[0][0] >= 0.5:
    print("Prediction: Customer may leave")
else:
    print("Prediction: Customer will stay")