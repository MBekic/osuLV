import pandas as pd 

# Učitavanje podataka
data = pd.read_csv('data_C02_emission.csv')

# a) Osnovna analiza i čišćenje podataka
print(f'DataFrame sadrži {len(data)} mjerenja')

print("Tipovi podataka po stupcima:")
print(data.dtypes)

# Provjera izostalih i dupliciranih vrijednosti
print(f"Izostale vrijednosti po stupcima:\n{data.isnull().sum()}")
print(f"Broj dupliciranih redaka: {data.duplicated().sum()}")

# Brisanje redaka s null vrijednostima i duplikata
data.dropna(inplace=True)
data.drop_duplicates(inplace=True)

# Konverzija kategorijskih stupaca
categorical_columns = ['Make', 'Model', 'Fuel Type', 'Transmission', 'Vehicle Class']
for col in categorical_columns:
    data[col] = data[col].astype('category')

# b) Automobili s najvećom i najmanjom gradskom potrošnjom
least_consuming = data.nsmallest(3, 'Fuel Consumption City (L/100km)')
most_consuming = data.nlargest(3, 'Fuel Consumption City (L/100km)')

print('Najveća gradska potrošnja: ')
print(most_consuming[['Make', 'Model', 'Fuel Consumption City (L/100km)']])
print('Najmanja gradska potrošnja: ')
print(least_consuming[['Make', 'Model', 'Fuel Consumption City (L/100km)']])

# c) Vozila s veličinom motora između 2.5 i 3.5 L
selected_data = data[(data['Engine Size (L)'] >= 2.5) & (data['Engine Size (L)'] <= 3.5)]
print(f"Broj vozila s motorom između 2.5 i 3.5 L: {len(selected_data)}")
print(f"Prosječna emisija CO2 za ta vozila: {selected_data['CO2 Emissions (g/km)'].mean()} g/km")

# d) Vozila marke Audi
audi_data = data[data['Make'] == 'Audi']
print(f"Broj mjerenja za Audi: {len(audi_data)}")

audi_4cyl = audi_data[audi_data['Cylinders'] == 4]
print(f"Prosječna emisija CO2 za Audi s 4 cilindra: {audi_4cyl['CO2 Emissions (g/km)'].mean()} g/km")

# e) Broj vozila po broju cilindara i prosječna emisija CO2
cylinder_counts = data['Cylinders'].value_counts().sort_index()
print("Broj vozila po broju cilindara:")
print(cylinder_counts)

cylinder_emissions = data.groupby('Cylinders')['CO2 Emissions (g/km)'].mean()
print("Prosječna emisija CO2 po broju cilindara:")
print(cylinder_emissions)

# f) Prosječna i medijalna gradska potrošnja goriva za dizel i benzin
diesel_vehicles = data[data['Fuel Type'] == 'D']
gasoline_vehicles = data[data['Fuel Type'].isin(['Z', 'X'])] 

print("Dizel:")
print(f"Prosječna potrošnja: {diesel_vehicles['Fuel Consumption City (L/100km)'].mean()} L/100km")
print(f"Medijalna potrošnja: {diesel_vehicles['Fuel Consumption City (L/100km)'].median()} L/100km")

print("Benzin:")
print(f"Prosječna potrošnja: {gasoline_vehicles['Fuel Consumption City (L/100km)'].mean()} L/100km")
print(f"Medijalna potrošnja: {gasoline_vehicles['Fuel Consumption City (L/100km)'].median()} L/100km")

# g) Najveća potrošnja za 4-cilindrično dizel vozilo
most_consuming_diesel_4cyl = diesel_vehicles[diesel_vehicles['Cylinders'] == 4].nlargest(1, 'Fuel Consumption City (L/100km)')
print("Najveća gradska potrošnja za 4-cilindrično dizel vozilo:")
print(most_consuming_diesel_4cyl[['Make', 'Model', 'Fuel Consumption City (L/100km)']])

# h) Broj vozila s ručnim mjenjačem
manual_vehicles = data[data['Transmission'].str.startswith('M', na=False)]
print(f"Broj vozila s ručnim mjenjačem: {len(manual_vehicles)}")

# i) Korelacija između numeričkih veličina
correlation_matrix = data.corr(numeric_only=True)
print("Korelacija između numeričkih veličina:")
print(correlation_matrix)
