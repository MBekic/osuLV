brojevi = []

while True:
    unos = input("Unesite broj (ili 'Done' za kraj petlje): ")

    if unos.lower()=="done":
        break

    try:
        brojevi.append(float(unos))

    except ValueError:
        print("Greška: Molimo unesite ispravan broj!")

if brojevi:
    print(f"Broj unosa: {len(brojevi)}")
    print(f"Srednja vrijednost: {sum(brojevi)/len(brojevi)}")
    print(f"Min vrijednost: {min(brojevi)}")
    print(f"Max vrijednost: {max(brojevi)}")

    brojevi.sort()
    print(f"Sortirana lista: {brojevi}")

else:
    print("Lista je prazna!")

    
