import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Load dataset
data = pd.read_csv("diabates.csv")

# Check if Outcome column exists
if "Outcome" not in data.columns:
    print("❌ Error: 'Outcome' column not found in your CSV file!")
    print("Your columns are:", list(data.columns))
    exit()

# Split data into features (X) and target (y)
X = data.drop("Outcome", axis=1)
y = data["Outcome"]

# Normalize the data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split into train/test
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Build ANN model
model = Sequential([
    Dense(16, input_dim=X.shape[1], activation='relu'),
    Dense(8, activation='relu'),
    Dense(1, activation='sigmoid')
])

# Compile model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train model
print("\n🧠 Training the ANN model, please wait...\n")
model.fit(X_train, y_train, epochs=100, batch_size=10, verbose=0)

# Evaluate model
loss, accuracy = model.evaluate(X_test, y_test, verbose=0)
print(f"✅ Model trained successfully! Accuracy: {accuracy*100:.2f}%\n")

# Take user input
print("Enter patient details to predict diabetes:\n")
features = []
for col in X.columns:
    value = float(input(f"{col}: "))
    features.append(value)

# Scale user input using same scaler
user_input_scaled = scaler.transform([features])
prediction = model.predict(user_input_scaled)

# Output prediction
if prediction[0][0] > 0.5:
    print("\n💡 The model predicts: DIABETIC 🩸")
else:
    print("\n💚 The model predicts: NOT DIABETIC")
