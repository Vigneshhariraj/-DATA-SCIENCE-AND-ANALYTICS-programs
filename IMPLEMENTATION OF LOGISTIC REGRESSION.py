import pandas as pd 
from matplotlib import pyplot as plt 
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LogisticRegression

# Load the dataset
df = pd.read_csv("insurance_data.csv") 

# Display the first few rows
print(df.head()) 

# Plot the data
plt.scatter(df.age, df.bought_insurance, marker='+', color='red')
plt.xlabel('Age')
plt.ylabel('Bought Insurance')
plt.title('Insurance Data')
plt.show()

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(df[['age']], df.bought_insurance, train_size=0.8, random_state=42) 

# Create and train the model
model = LogisticRegression() 
model.fit(X_train, y_train) 

# Predict on test data
y_predicted = model.predict(X_test) 

# Print predicted probabilities
print("Predicted Probabilities:\n", model.predict_proba(X_test))

# Calculate accuracy
accuracy = model.score(X_test, y_test) 
print("Model Accuracy: ", accuracy)

# Print predictions
print("Predictions:\n", y_predicted)

# Print model coefficients and intercept
print("Model Coefficient: ", model.coef_) 
print("Model Intercept: ", model.intercept_) 

# Save predictions to CSV
output_df = pd.DataFrame({
    'Age': X_test['age'],
    'Actual': y_test,
    'Predicted': y_predicted
})
output_df.to_csv('insurance_predictions.csv', index=False)

print("Predictions saved to 'insurance_predictions.csv'")
