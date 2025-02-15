import math

def haversine(lat1, lon1, lat2, lon2, altitude1=0, altitude2=0, unit='km'):
    """
    Calcule la distance Haversine en tenant compte de la courbure de la Terre et des différences d'altitude.

    Paramètres:
        lat1, lon1 : Coordonnées du premier point (en degrés décimaux).
        lat2, lon2 : Coordonnées du deuxième point (en degrés décimaux).
        altitude1, altitude2 : Altitude des deux points (en mètres, valeur par défaut 0).
        unit : Unité de distance pour le résultat ('km' pour kilomètres ou 'mi' pour miles).
    
    Retourne:
        total_distance : La distance 3D entre les points en tenant compte de l'altitude (en unité choisie).
    """
    rayon = 6371.0 if unit == 'km' else 3958.8

    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])

    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    surface_distance = rayon * c

    altitude_diff = altitude2 - altitude1

    total_distance = math.sqrt(surface_distance**2 + altitude_diff**2)

    return total_distance

def get_coordinates(language):
    """
    Demande à l'utilisateur d'entrer les coordonnées et l'altitude. 
    Gère la validation des entrées et prend en charge l'anglais et le français.

    Paramètres:
        language : Langue choisie ('en' pour l'anglais, 'fr' pour le français).
    
    Retourne:
        lat, lon, alt : Latitude, longitude et altitude entrées par l'utilisateur.
    """
    while True:
        try:
            if language == 'en':
                lat = float(input("Enter latitude (decimal degrees): "))
                lon = float(input("Enter longitude (decimal degrees): "))
                alt = float(input("Enter altitude (meters): "))
            else:
                lat = float(input("Entrez la latitude (degrés décimaux) : "))
                lon = float(input("Entrez la longitude (degrés décimaux) : "))
                alt = float(input("Entrez l'altitude (en mètres) : "))
            return lat, lon, alt
        except ValueError:
            print("Invalid input. Please enter valid numerical values.")

def choose_language():
    """
    Demande à l'utilisateur de choisir entre l'anglais ou le français. Si le choix est invalide, il retourne par défaut l'anglais.

    Retourne:
        language : La langue choisie ('en' ou 'fr').
    """
    while True:
        language = input("Choose language / Choisissez la langue (en/fr): ").strip().lower()
        if language in ['en', 'fr']:
            return language
        else:
            print("Invalid language choice, defaulting to English.")
            return 'en'

def main():
    """
    Fonction principale pour exécuter le programme de calcul de distance.
    Demande la sélection de la langue, les coordonnées et les unités de distance.
    Affiche la distance calculée entre les deux points.
    """
    language = choose_language()

    if language == 'en':
        print("\nAdvanced Geographical Distance Calculator")
    else:
        print("\nCalculateur Avancé de Distance Géographique")

  print("\nPoint 1:")
    lat1, lon1, alt1 = get_coordinates(language)

    print("\nPoint 2:")
    lat2, lon2, alt2 = get_coordinates(language)

    while True:
        if language == 'en':
            unit = input("Choose units for distance (km or mi): ").strip().lower()
        else:
            unit = input("Choisissez l'unité pour la distance (km ou mi) : ").strip().lower()

        if unit in ['km', 'mi']:
            break
        else:
            print("Invalid unit. Please choose 'km' or 'mi'.")

    distance = haversine(lat1, lon1, lat2, lon2, alt1, alt2, unit)

    if language == 'en':
        print(f"\nThe distance between the two points is {distance:.2f} {unit}.")
    else:
        print(f"\nLa distance entre les deux points est de {distance:.2f} {unit}.")

if __name__ == "__main__":
    main()
