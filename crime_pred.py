# -*- coding: utf-8 -*-
"""crime_pred.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1IbFAKIcfIOCyGVP060dr7GfSa5lhnsPU
"""

import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from scipy import stats

# Load the CSV file
file_path = "/content/nyc crime data.csv"
df = pd.read_csv(file_path)

# Step 1: Data Exploration and Understanding
print(df.head())  # Display the first few rows of the dataset
print(df.tail())
print(df.describe()) # Display information about the dataset

import pandas as pd

# Assuming your dataset is in a CSV file named 'dataset.csv'
# Replace 'dataset.csv' with the path to your actual dataset file
data = pd.read_csv('/content/nyc crime data.csv')

# Select 5500 rows randomly with replacement
sd = data.sample(n=12500, replace=True, random_state=42)

# Now 'sampled_data' contains your randomly selected 55000 rows
print(sd.head())

#missing value check
print(sd.isnull().sum())

# Fill missing values with mode
df_filled = sd.fillna(df.mode().iloc[0])

# Save the cleaned dataset to a new file
df_filled.to_csv("/content/nyc crime data.csv", index=False)

print(df_filled.isnull().sum())

import pandas as pd

# Assuming df_filled is your DataFrame with NaN values
# Replace NaN values with the mode of each column
for column in df_filled.columns:
    m_value = df_filled[column].mode()  # Calculate mode of the column
    df_filled[column].fillna(m_value, inplace=True)  # Fill NaN values with the mode
# Assuming df is your DataFrame and 'attribute_to_drop' is the name of the attribute you want to drop
df_filled.drop(columns=['TRANSIT_DISTRICT'], inplace=True)

# Verify that NaN values are replaced with mode
print(df_filled.head())

print(df_filled.info())

import matplotlib.pyplot as plt

# Specify numerical columns
numerical_cols = df_filled.select_dtypes(include=['int64', 'float64']).columns.tolist()

# Calculate the number of rows and columns for subplots
num_cols = len(numerical_cols)
num_rows = num_cols // 2 + num_cols % 2  # Calculate the number of rows needed

# Create a larger figure
plt.figure(figsize=(12, 8))  # Adjust the figure size as needed

# Plot boxplots for each numerical column
for i, col in enumerate(numerical_cols):
    plt.subplot(num_rows, 2, i+1)
    plt.boxplot(df_filled[col])
    plt.title(col)
    plt.grid(True)  # Add grid lines

plt.tight_layout()  # Adjust layout
plt.show()

import numpy as np
for a in numerical_cols:
  for x in [a]:
      Q3, Q1 = np.percentile(df.loc[:,x], [75,25])
      IQR = Q3 - Q1
      max = Q3 + (1.5*IQR)
      min = Q1 - (1.5*IQR)
      df.loc[df[x] < min,x] = np.nan
      df.loc[df[x] > max,x] = np.nan
  print(a,":\t")
  print(Q1)
  print(Q3)
  print(IQR)
  print()

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import LabelEncoder

label_encoder = LabelEncoder()

# Encode the target variable
y_encoded = label_encoder.fit_transform(sd['SUSP_SEX'])

# Separate features (X) and encoded target variable (y)
X = df_filled.drop(columns=['SUSP_SEX'])
y = y_encoded

# Convert string attributes to categorical variables
X = pd.get_dummies(X)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Initialize the Random Forest Regressor
rf_regressor = RandomForestClassifier(n_estimators=100, random_state=42)

# Train the model on the training data
rf_regressor.fit(X_train, y_train)

# Make predictions on the testing data
y_pred = rf_regressor.predict(X_test)



# Calculate accuracy score
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy:.2f}')

# Generate classification report
print('Classification Report:')
print(classification_report(y_test, y_pred))


# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
print(f'Mean Squared Error: {mse:.2f}')

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import LabelEncoder

label_encoder = LabelEncoder()

# Encode the target variable
y_encoded = label_encoder.fit_transform(sd['SUSP_AGE_GROUP'])

# Separate features (X) and encoded target variable (y)
X = df_filled.drop(columns=['SUSP_AGE_GROUP'])
y = y_encoded

# Convert string attributes to categorical variables
X = pd.get_dummies(X)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Initialize the Random Forest Regressor
rf_regressor = RandomForestClassifier(n_estimators=100, random_state=42)

# Train the model on the training data
rf_regressor.fit(X_train, y_train)

# Make predictions on the testing data
y_pred = rf_regressor.predict(X_test)



# Calculate accuracy score
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy:.2f}')

# Generate classification report
print('Classification Report:')
print(classification_report(y_test, y_pred))


# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
print(f'Mean Squared Error: {mse:.2f}')

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import LabelEncoder

label_encoder = LabelEncoder()

# Encode the target variable
y_encoded = label_encoder.fit_transform(sd['SUSP_RACE'])

# Separate features (X) and encoded target variable (y)
X = df_filled.drop(columns=['SUSP_RACE'])
y = y_encoded

# Convert string attributes to categorical variables
X = pd.get_dummies(X)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Initialize the Random Forest Regressor
rf_regressor = RandomForestClassifier(n_estimators=100, random_state=42)

# Train the model on the training data
rf_regressor.fit(X_train, y_train)

# Make predictions on the testing data
y_pred = rf_regressor.predict(X_test)



# Calculate accuracy score
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy:.2f}')

# Generate classification report
print('Classification Report:')
print(classification_report(y_test, y_pred))


# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
print(f'Mean Squared Error: {mse:.2f}')

import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score


# Separate features and target variable
X = df_filled.drop('SUSP_SEX', axis=1)
y = df_filled['SUSP_SEX']

# Encode all columns with string values
le = LabelEncoder()
X_encoded = X.apply(lambda col: le.fit_transform(col.astype(str)) if col.dtype == 'object' else col)

# Standardize the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_encoded)

# Split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.3, random_state=42)

# Perform PCA for feature selection
pca = PCA(n_components=0.95)  # Retain 95% of variance
X_train_pca = pca.fit_transform(X_train)
X_test_pca = pca.transform(X_test)

# Train Random Forest classifier
rf_classifier = RandomForestClassifier(n_estimators=100, random_state=42)
rf_classifier.fit(X_train_pca, y_train)

# Predictions
y_pred = rf_classifier.predict(X_test_pca)

# Evaluate model
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score


# Separate features and target variable
X = df_filled.drop('SUSP_AGE_GROUP', axis=1)
y = df_filled['SUSP_AGE_GROUP']

# Encode all columns with string values
le = LabelEncoder()
X_encoded = X.apply(lambda col: le.fit_transform(col.astype(str)) if col.dtype == 'object' else col)

# Standardize the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_encoded)

# Split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.3, random_state=42)

# Perform PCA for feature selection
pca = PCA(n_components=0.95)  # Retain 95% of variance
X_train_pca = pca.fit_transform(X_train)
X_test_pca = pca.transform(X_test)

# Train Random Forest classifier
rf_classifier = RandomForestClassifier(n_estimators=100, random_state=42)
rf_classifier.fit(X_train_pca, y_train)

# Predictions
y_pred = rf_classifier.predict(X_test_pca)

# Evaluate model
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score


# Separate features and target variable
X = df_filled.drop('SUSP_RACE', axis=1)
y = df_filled['SUSP_RACE']

# Encode all columns with string values
le = LabelEncoder()
X_encoded = X.apply(lambda col: le.fit_transform(col.astype(str)) if col.dtype == 'object' else col)

# Standardize the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_encoded)

# Split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.3, random_state=42)

# Perform PCA for feature selection
pca = PCA(n_components=0.95)  # Retain 95% of variance
X_train_pca = pca.fit_transform(X_train)
X_test_pca = pca.transform(X_test)

# Train Random Forest classifier
rf_classifier = RandomForestClassifier(n_estimators=100, random_state=42)
rf_classifier.fit(X_train_pca, y_train)

# Predictions
y_pred = rf_classifier.predict(X_test_pca)

# Evaluate model
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score


# Separate features and target variable
X = df_filled.drop('SUSP_SEX', axis=1)
y = df_filled['SUSP_SEX']

# Encode all columns with string values
le = LabelEncoder()
X_encoded = X.apply(lambda col: le.fit_transform(col.astype(str)) if col.dtype == 'object' else col)

# Standardize the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_encoded)

# Split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.3, random_state=42)

# Train Random Forest classifier without PCA
rf_classifier_without_pca = RandomForestClassifier(n_estimators=100, random_state=42)
rf_classifier_without_pca.fit(X_train, y_train)
y_pred_without_pca = rf_classifier_without_pca.predict(X_test)
accuracy_without_pca = accuracy_score(y_test, y_pred_without_pca)
print("Accuracy without PCA:", accuracy_without_pca)

# Perform PCA for feature selection
pca = PCA(n_components=0.95)  # Retain 95% of variance
X_train_pca = pca.fit_transform(X_train)
X_test_pca = pca.transform(X_test)

# Train Random Forest classifier with PCA
rf_classifier_with_pca = RandomForestClassifier(n_estimators=100, random_state=42)
rf_classifier_with_pca.fit(X_train_pca, y_train)
y_pred_with_pca = rf_classifier_with_pca.predict(X_test_pca)
accuracy_with_pca = accuracy_score(y_test, y_pred_with_pca)
print("Accuracy with PCA:", accuracy_with_pca)

import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_selection import SelectFromModel
from sklearn.metrics import accuracy_score


# Separate features and target variable
X = df_filled.drop('SUSP_SEX', axis=1)
y = df_filled['SUSP_SEX']

# Encode all columns with string values
le = LabelEncoder()
X_encoded = X.apply(lambda col: le.fit_transform(col.astype(str)) if col.dtype == 'object' else col)

# Standardize the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_encoded)

# Split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.3, random_state=42)

# Train Random Forest classifier without feature selection
rf_classifier_without_fs = RandomForestClassifier(n_estimators=100, random_state=42)
rf_classifier_without_fs.fit(X_train, y_train)
y_pred_without_fs = rf_classifier_without_fs.predict(X_test)
accuracy_without_fs = accuracy_score(y_test, y_pred_without_fs)
print("Accuracy without feature selection:", accuracy_without_fs)

# Train Random Forest classifier with feature selection
rf_classifier_with_fs = RandomForestClassifier(n_estimators=100, random_state=42)
# Perform feature selection using Random Forest feature importance
sfm = SelectFromModel(rf_classifier_with_fs, threshold=0.1)  # Adjust threshold as needed
sfm.fit(X_train, y_train)
X_train_selected = sfm.transform(X_train)
X_test_selected = sfm.transform(X_test)
rf_classifier_with_fs.fit(X_train_selected, y_train)
y_pred_with_fs = rf_classifier_with_fs.predict(X_test_selected)
accuracy_with_fs = accuracy_score(y_test, y_pred_with_fs)
print("Accuracy with feature selection:", accuracy_with_fs)

import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score


# Separate features and target variable
X = df_filled.drop('SUSP_AGE_GROUP', axis=1)
y = df_filled['SUSP_AGE_GROUP']

# Encode all columns with string values
le = LabelEncoder()
X_encoded = X.apply(lambda col: le.fit_transform(col.astype(str)) if col.dtype == 'object' else col)

# Standardize the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_encoded)

# Split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.3, random_state=42)

# Train Random Forest classifier without PCA
rf_classifier_without_pca = RandomForestClassifier(n_estimators=100, random_state=42)
rf_classifier_without_pca.fit(X_train, y_train)
y_pred_without_pca = rf_classifier_without_pca.predict(X_test)
accuracy_without_pca = accuracy_score(y_test, y_pred_without_pca)
print("Accuracy without PCA:", accuracy_without_pca)

# Perform PCA for feature selection
pca = PCA(n_components=0.95)  # Retain 95% of variance
X_train_pca = pca.fit_transform(X_train)
X_test_pca = pca.transform(X_test)

# Train Random Forest classifier with PCA
rf_classifier_with_pca = RandomForestClassifier(n_estimators=100, random_state=42)
rf_classifier_with_pca.fit(X_train_pca, y_train)
y_pred_with_pca = rf_classifier_with_pca.predict(X_test_pca)
accuracy_with_pca = accuracy_score(y_test, y_pred_with_pca)
print("Accuracy with PCA:", accuracy_with_pca)

import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_selection import SelectFromModel
from sklearn.metrics import accuracy_score


# Separate features and target variable
X = df_filled.drop('SUSP_AGE_GROUP', axis=1)
y = df_filled['SUSP_AGE_GROUP']

# Encode all columns with string values
le = LabelEncoder()
X_encoded = X.apply(lambda col: le.fit_transform(col.astype(str)) if col.dtype == 'object' else col)

# Standardize the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_encoded)

# Split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.3, random_state=42)

# Train Random Forest classifier without feature selection
rf_classifier_without_fs = RandomForestClassifier(n_estimators=100, random_state=42)
rf_classifier_without_fs.fit(X_train, y_train)
y_pred_without_fs = rf_classifier_without_fs.predict(X_test)
accuracy_without_fs = accuracy_score(y_test, y_pred_without_fs)
print("Accuracy without feature selection:", accuracy_without_fs)

# Train Random Forest classifier with feature selection
rf_classifier_with_fs = RandomForestClassifier(n_estimators=100, random_state=42)
# Perform feature selection using Random Forest feature importance
sfm = SelectFromModel(rf_classifier_with_fs, threshold=0.1)  # Adjust threshold as needed
sfm.fit(X_train, y_train)
X_train_selected = sfm.transform(X_train)
X_test_selected = sfm.transform(X_test)
rf_classifier_with_fs.fit(X_train_selected, y_train)
y_pred_with_fs = rf_classifier_with_fs.predict(X_test_selected)
accuracy_with_fs = accuracy_score(y_test, y_pred_with_fs)
print("Accuracy with feature selection:", accuracy_with_fs)

import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score


# Separate features and target variable
X = df_filled.drop('SUSP_RACE', axis=1)
y = df_filled['SUSP_RACE']

# Encode all columns with string values
le = LabelEncoder()
X_encoded = X.apply(lambda col: le.fit_transform(col.astype(str)) if col.dtype == 'object' else col)

# Standardize the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_encoded)

# Split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.3, random_state=42)

# Train Random Forest classifier without PCA
rf_classifier_without_pca = RandomForestClassifier(n_estimators=100, random_state=42)
rf_classifier_without_pca.fit(X_train, y_train)
y_pred_without_pca = rf_classifier_without_pca.predict(X_test)
accuracy_without_pca = accuracy_score(y_test, y_pred_without_pca)
print("Accuracy without PCA:", accuracy_without_pca)

# Perform PCA for feature selection
pca = PCA(n_components=0.95)  # Retain 95% of variance
X_train_pca = pca.fit_transform(X_train)
X_test_pca = pca.transform(X_test)

# Train Random Forest classifier with PCA
rf_classifier_with_pca = RandomForestClassifier(n_estimators=100, random_state=42)
rf_classifier_with_pca.fit(X_train_pca, y_train)
y_pred_with_pca = rf_classifier_with_pca.predict(X_test_pca)
accuracy_with_pca = accuracy_score(y_test, y_pred_with_pca)
print("Accuracy with PCA:", accuracy_with_pca)

import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_selection import SelectFromModel
from sklearn.metrics import accuracy_score


# Separate features and target variable
X = df_filled.drop('SUSP_RACE', axis=1)
y = df_filled['SUSP_RACE']

# Encode all columns with string values
le = LabelEncoder()
X_encoded = X.apply(lambda col: le.fit_transform(col.astype(str)) if col.dtype == 'object' else col)

# Standardize the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_encoded)

# Split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.3, random_state=42)

# Train Random Forest classifier without feature selection
rf_classifier_without_fs = RandomForestClassifier(n_estimators=100, random_state=42)
rf_classifier_without_fs.fit(X_train, y_train)
y_pred_without_fs = rf_classifier_without_fs.predict(X_test)
accuracy_without_fs = accuracy_score(y_test, y_pred_without_fs)
print("Accuracy without feature selection:", accuracy_without_fs)

# Train Random Forest classifier with feature selection
rf_classifier_with_fs = RandomForestClassifier(n_estimators=100, random_state=42)
# Perform feature selection using Random Forest feature importance
sfm = SelectFromModel(rf_classifier_with_fs, threshold=0.1)  # Adjust threshold as needed
sfm.fit(X_train, y_train)
X_train_selected = sfm.transform(X_train)
X_test_selected = sfm.transform(X_test)
rf_classifier_with_fs.fit(X_train_selected, y_train)
y_pred_with_fs = rf_classifier_with_fs.predict(X_test_selected)
accuracy_with_fs = accuracy_score(y_test, y_pred_with_fs)
print("Accuracy with feature selection:", accuracy_with_fs)