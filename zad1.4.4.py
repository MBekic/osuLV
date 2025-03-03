from collections import defaultdict
import string

rijeci_brojac = defaultdict(int)

try:
    with open("song.txt", "r", encoding="utf-8") as file:
        for linija in file:
            linija = linija.translate(str.maketrans("", "", string.punctuation)).lower()
            rijeci = linija.split()
            
            for rijec in rijeci:
                rijeci_brojac[rijec] += 1

    rijeci_samo_jednom = [rijec for rijec, broj in rijeci_brojac.items() if broj == 1]

    print(f"Ukupno riječi koje se pojavljuju samo jednom: {len(rijeci_samo_jednom)}")
    print("Riječi koje se pojavljuju samo jednom:")
    print(", ".join(rijeci_samo_jednom))

except FileNotFoundError:
    print("Greška: Datoteka 'song.txt' nije pronađena.")
