# Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# Load the Titanic dataset
url = "https://web.stanford.edu/class/archive/cs/cs109/cs109.1166/stuff/titanic.csv"
titanic_df = pd.read_csv(url)

# Explore the dataset
# (you may want to do more detailed exploratory data analysis depending on your goals)

# Drop unnecessary columns or handle missing values
titanic_df = titanic_df.drop(['Name', 'Ticket', 'Cabin', 'Embarked', 'PassengerId'], axis=1)
titanic_df = titanic_df.dropna()

# Convert categorical features to numerical using one-hot encoding
titanic_df = pd.get_dummies(titanic_df, columns=['Sex', 'Pclass'], drop_first=True)

# Separate features and target variable
X = titanic_df.drop('Survived', axis=1)
y = titanic_df['Survived']

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a Random Forest Classifier
classifier = RandomForestClassifier(n_estimators=100, random_state=42)
classifier.fit(X_train, y_train)

# Make predictions on the test set
predictions = classifier.predict(X_test)

# Evaluate the classifier
accuracy = accuracy_score(y_test, predictions)
report = classification_report(y_test, predictions)

print(f"Accuracy: {accuracy}")
print("Classification Report:")
print(report)