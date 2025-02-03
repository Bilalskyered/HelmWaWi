from Model import HelmBestand

def finde_helme(groesse=None, max_preis=None, art=None, material_ausschluss=None):
    festeListe = list(HelmBestand.values())
    temporäreListe = []

    for helm in festeListe:
        if material_ausschluss and helm.material == material_ausschluss:
            temporäreListe.append(helm)

    for helm in temporäreListe:
        festeListe.remove(helm)

    gefundene_helme = []
    for helm in festeListe:
        if (groesse is None or helm.groesse == groesse) and \
           (max_preis is None or helm.preis <= max_preis) and \
           (art is None or helm.art == art):
            gefundene_helme.append(helm)
    return gefundene_helme