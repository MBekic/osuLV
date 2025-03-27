import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

df = pd.read_csv("data_C02_emission.csv")
# a)
features = ["Engine Size (L)", "Cylinders", "Fuel Consumption City (L/100km)", 
            "Fuel Consumption Hwy (L/100km)", "Fuel Consumption Comb (L/100km)"]
target = "CO2 Emissions (g/km)"
X_train, X_test, y_train, y_test = train_test_split(df[features], df[target], test_size=0.2, random_state=1)

# b)
plt.figure()
plt.scatter(X_train["Engine Size (L)"], y_train, color='blue', label='Trening skup', alpha=0.5)
plt.scatter(X_test["Engine Size (L)"], y_test, color='red', label='Testni skup', alpha=0.5)
plt.xlabel("Veličina motora (L)")
plt.ylabel("Emisija CO2 (g/km)")
plt.title("Ovisnost emisije CO2 o veličini motora")
plt.legend()
plt.show()

# c)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.hist(X_train["Engine Size (L)"], bins=20, color='blue', alpha=0.7)
plt.title("Prije standardizacije")
plt.subplot(1, 2, 2)
plt.hist(X_train_scaled[:, 0], bins=20, color='red', alpha=0.7)
plt.title("Nakon standardizacije")
plt.show()

# d)
model = LinearRegression()
model.fit(X_train_scaled, y_train)
print("Koeficijenti modela:", model.coef_)
print("Presjek s osi y:", model.intercept_)

# e)
y_pred = model.predict(X_test_scaled)
plt.figure(figsize=(8, 6))
plt.scatter(y_test, y_pred, color='purple', alpha=0.5)
plt.xlabel("Stvarna emisija CO2 (g/km)")
plt.ylabel("Predviđena emisija CO2 (g/km)")
plt.title("Ovisnost stvarnih i predviđenih vrijednosti")
plt.show()

# f)
mae = mean_absolute_error(y_test, y_pred)
print("Mean Absolute Error (MAE):", mae)
mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error (MSE):", mse)
rmse = mean_squared_error(y_test, y_pred) ** 0.5
print("Root Mean Squared Error (RMSE):", rmse)
r2 = r2_score(y_test, y_pred)
print("R-squared (R2):", r2)
