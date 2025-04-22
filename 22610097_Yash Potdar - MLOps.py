from sklearn.datasets import load_wine
import pandas as pd
import joblib

wine = load_wine()
df = pd.DataFrame(wine.data)
df['target'] = wine.target

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

x = df.drop('target', axis=1)
y = df['target']

x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=42, test_size=0.2)

model = LogisticRegression(max_iter=100)
model.fit(x_train, y_train)
pred = model.predict(x_test)
print(f"{accuracy_score(pred, y_test)}")

joblib.dump(filename="model.pkl", value=model)

# Loading the model for future use
loaded_model = joblib.load(filename="model.pkl")
y_pred = loaded_model.predict(x_test)
print(f"{accuracy_score(pred, y_test)}")