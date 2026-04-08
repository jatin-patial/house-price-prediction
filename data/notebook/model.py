import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import pickle

df = pd.read_csv("data/data.csv")

# preprocessing
df = df[['price','bedrooms','bathrooms','sqft_living']]
df.dropna(inplace=True)

X = df.drop("price", axis=1)
y = df["price"]

X_train, X_test, y_train, y_test = train_test_split(X, y)

model = RandomForestRegressor()
model.fit(X_train, y_train)

pickle.dump(model, open(r"data\models\model.pkl", "wb"))