from Controller.Logic import finde_helme

def benutzereingabe():
    groesse = input("Geben Sie die gewünschte Größe ein (S, M, L, XL): ")
    max_preis = input("Geben Sie den maximalen Preis ein: ")
    art = input("Geben Sie die Art des Helms ein (Sport, Enduro, Cruiser, Jethelm, Klapphelm): ")
    material_ausschluss = input("Geben Sie das auszuschließende Material ein (z.B. Polycarbonat): ")

    if max_preis:
        max_preis = int(max_preis)
    else:
        max_preis = None

    gefundene_helme = finde_helme(groesse, max_preis, art, material_ausschluss)
    if gefundene_helme:
        print("Gefundene Helme:")
        for helm in gefundene_helme:
            print(helm)
    else:
        print("Keine Helme gefunden, die den Kriterien entsprechen.")

if __name__ == "__main__":
    benutzereingabe()