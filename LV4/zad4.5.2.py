import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score, max_error

df = pd.read_csv("data_C02_emission.csv")

numerical_features = ["Engine Size (L)", "Cylinders", "Fuel Consumption City (L/100km)", 
                      "Fuel Consumption Hwy (L/100km)", "Fuel Consumption Comb (L/100km)"]
categorical_feature = "Fuel Type"
target = "CO2 Emissions (g/km)"


ohe = OneHotEncoder(drop='first', sparse_output=False)
categorical_encoded = ohe.fit_transform(df[[categorical_feature]])
categorical_columns = ohe.get_feature_names_out([categorical_feature])
df_encoded = pd.DataFrame(categorical_encoded, columns=categorical_columns)

X = pd.concat([df[numerical_features], df_encoded], axis=1)
y = df[target]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

print("Koeficijenti modela:", model.coef_)
print("Presjek s osi y:", model.intercept_)

y_pred = model.predict(X_test)
plt.figure(figsize=(8, 6))
plt.scatter(y_test, y_pred, color='purple', alpha=0.5)
plt.xlabel("Stvarna emisija CO2 (g/km)")
plt.ylabel("Predviđena emisija CO2 (g/km)")
plt.title("Ovisnost stvarnih i predviđenih vrijednosti")
plt.show()

mae = mean_absolute_error(y_test, y_pred)
print("Mean Absolute Error (MAE):", mae)
mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error (MSE):", mse)
rmse = mean_squared_error(y_test, y_pred) ** 0.5
print("Root Mean Squared Error (RMSE):", rmse)
r2 = r2_score(y_test, y_pred)
print("R-squared (R2):", r2)
max_err = max_error(y_test, y_pred)
print("Maksimalna pogreška u procjeni emisije CO2 (g/km):", max_err)

errors = abs(y_test - y_pred)
max_error_index = errors.idxmax()
print("Vozilo s najvećom pogreškom:")
print(df.iloc[max_error_index])
