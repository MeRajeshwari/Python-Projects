# Import necessary libraries
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report

# Sample SMS dataset
messages = [
    {'text': 'Hello, how are you?', 'label': 'ham'},
    {'text': 'Win a free iPhone now!', 'label': 'spam'},
    # Add more messages with labels as needed
]

# Separate text and labels
texts = [message['text'] for message in messages]
labels = [message['label'] for message in messages]

# Convert labels to numerical values
label_mapping = {'ham': 0, 'spam': 1}
numeric_labels = [label_mapping[label] for label in labels]

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(texts, numeric_labels, test_size=0.2, random_state=42)

# Vectorize the text data
vectorizer = CountVectorizer()
X_train_vectorized = vectorizer.fit_transform(X_train)
X_test_vectorized = vectorizer.transform(X_test)

# Train a Naive Bayes classifier
classifier = MultinomialNB()
classifier.fit(X_train_vectorized, y_train)

# Make predictions on the test set
predictions = classifier.predict(X_test_vectorized)

# Evaluate the classifier
accuracy = accuracy_score(y_test, predictions)
report = classification_report(y_test, predictions)

print(f"Accuracy: {accuracy}")
print("Classification Report:")
print(report)