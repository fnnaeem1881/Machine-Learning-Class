
import pandas as pd
import matplotlib.pyplot as plt

print("=== Pandas Diagram Practice ===")

data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May"],
    "Sales": [1200, 1500, 1700, 1600, 2000]
}

df = pd.DataFrame(data)
print("\nData Table:\n", df)

# ------- Bar Chart -------
plt.figure()
plt.bar(df["Month"], df["Sales"])
plt.title("Monthly Sales Bar Chart")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()

# ------- Line Chart -------
plt.figure()
plt.plot(df["Month"], df["Sales"], marker='o')
plt.title("Monthly Sales Line Chart")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()

