import string

ham_broj_rijeci = 0
ham_broj_poruka = 0
spam_broj_rijeci = 0
spam_broj_poruka = 0
spam_usklicnik_broj = 0

try:
    with open("SMSSpamCollection.txt", "r", encoding="utf-8") as file:
        for linija in file:
            podaci = linija.strip().split("\t")
            
            if len(podaci) < 2:
                continue  

            tip = podaci[0] 
            poruka = podaci[1]

            rijeci = poruka.split()
            broj_rijeci = len(rijeci)

            if tip == "ham":
                ham_broj_rijeci += broj_rijeci
                ham_broj_poruka += 1
            elif tip == "spam":
                spam_broj_rijeci += broj_rijeci
                spam_broj_poruka += 1
                if poruka.endswith("!"):
                    spam_usklicnik_broj += 1

    print(f"Prosječan broj riječi u HAM porukama: {(ham_broj_rijeci / ham_broj_poruka if ham_broj_poruka > 0 else 0):.2f}")
    print(f"Prosječan broj riječi u SPAM porukama: {(spam_broj_rijeci / spam_broj_poruka if spam_broj_poruka > 0 else 0):.2f}")
    print(f"Broj SPAM poruka koje završavaju uskličnikom: {spam_usklicnik_broj}")

except FileNotFoundError:
    print("Greška: Datoteka 'SMSSpamCollection.txt' nije pronađena.")
