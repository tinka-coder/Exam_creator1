# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.preprocessing import StandardScaler

# Step 1: Load the dataset (assumed CSV file with appropriate data)
data = pd.read_csv('disease_data.csv')

# Display first few rows of the dataset
print(data.head())

# Step 2: Preprocess the data
# Assuming the dataset has columns: ['region', 'temperature', 'rainfall', 'population_density', 'sanitation_index', 'outbreak']

# Handle missing values (if any)
data = data.fillna(data.mean())

# Define features (X) and target (y)
X = data[['temperature', 'rainfall', 'population_density', 'sanitation_index']]  # Features
y = data['outbreak']  # Target (1 for outbreak, 0 for no outbreak)

# Split the data into training and testing sets (80% training, 20% testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 3: Scale the features (optional but often helps with performance)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Step 4: Train the RandomForestClassifier model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Step 5: Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy * 100:.2f}%")

# Print classification report and confusion matrix
print("Classification Report:")
print(classification_report(y_test, y_pred))

print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))

# Step 6: Visualize feature importance
importances = model.feature_importances_
features = ['temperature', 'rainfall', 'population_density', 'sanitation_index']
indices = np.argsort(importances)

plt.figure(figsize=(8, 6))
plt.title('Feature Importance')
plt.barh(range(len(indices)), importances[indices], align='center')
plt.yticks(range(len(indices)), [features[i] for i in indices])
plt.xlabel('Relative Importance')
plt.show()
