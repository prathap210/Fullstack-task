import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

# 1. Data Preprocessing (Simulated Data)
data = {
    'StudyHours': [2, 5, 1, 8, 4, 10, 3, 7, 6, 9],
    'PrevGrades': [60, 75, 50, 90, 70, 95, 65, 85, 80, 92],
    'PerformanceScore': [65, 78, 55, 92, 72, 98, 68, 88, 82, 95]
}

df = pd.DataFrame(data)

# Features (X) and Target (y)
X = df[['StudyHours', 'PrevGrades']]
y = df['PerformanceScore']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 2. Model Training
model = LinearRegression()
model.fit(X_train, y_train)

# 3. Model Prediction
y_pred = model.predict(X_test)

# 4. Evaluation Metrics
print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))
print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))
print('R-squared Score:', metrics.r2_score(y_test, y_pred))

# Example Prediction
new_student = np.array([[6, 85]])
predicted_score = model.predict(new_student)
print(f'Predicted Performance Score for 6 study hours and 85 prev grade: {predicted_score[0]}')
