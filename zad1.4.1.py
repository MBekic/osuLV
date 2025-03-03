def total_euro(radni_sati, placa_po_satu):
    return radni_sati*placa_po_satu

radni_sati = float(input("Unesite broj radnih sati: "))
placa_po_satu = float(input("Unesite placu po satu: "))
print(f"Ukupno: {radni_sati*placa_po_satu} eura35")
ukupno = total_euro(radni_sati, placa_po_satu)
print(f"Ukupno: {ukupno} eura")

