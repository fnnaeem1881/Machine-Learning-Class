import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

data = {"Hours_Studied": [1,2,3,4,5], "Marks": [55,60,65,70,75]}
df = pd.DataFrame(data)

plt.figure()
plt.bar(df["Hours_Studied"], df["Marks"])
plt.show()

plt.figure()
plt.plot(df["Hours_Studied"], df["Marks"], marker='o')
plt.show()

X = df[["Hours_Studied"]]
y = df["Marks"]

model = LinearRegression()
model.fit(X, y)

predicted = model.predict(pd.DataFrame({"Hours_Studied":[6]}))
print("Prediction for 6 hours study:", predicted[0])
