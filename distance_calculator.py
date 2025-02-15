import math

def geodesic(lat1, lon1, lat2, lon2, altitude1=0, altitude2=0, unit='km', mode='spherical'):
    if mode == 'ellipsoidal':
        a = 6378137.0
        f = 1 / 298.257223563
        e2 = 2 * f - f**2
        lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
        sin_phi1, cos_phi1 = math.sin(lat1), math.cos(lat1)
        sin_phi2, cos_phi2 = math.sin(lat2), math.cos(lat2)
        dphi = lat2 - lat1
        dlamb = lon2 - lon1

        A = math.sqrt((cos_phi2 * math.sin(dlamb))**2 + (cos_phi1 * sin_phi2 - sin_phi1 * cos_phi2 * math.cos(dlamb))**2)
        B = sin_phi1 * sin_phi2 + cos_phi1 * cos_phi2 * math.cos(dlamb)
        sigma = math.atan2(A, B)

        U1 = math.atan((1 - f) * math.tan(lat1))
        U2 = math.atan((1 - f) * math.tan(lat2))
        cos_U1, cos_U2 = math.cos(U1), math.cos(U2)
        sin_U1, sin_U2 = math.sin(U1), math.sin(U2)

        cos_sigma = math.cos(sigma)
        sin_sigma = math.sin(sigma)

        cos2_sigma_m = cos_sigma - 2 * sin_U1 * sin_U2 / math.cos(sigma)
        C = f / 16 * math.cos(sigma) ** 2 * (4 + f * (4 - 3 * math.cos(sigma) ** 2))

        distance = a * (sigma - C)
    else:
        radius = 6371.0 if unit == 'km' else 3958.8
        lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
        dlat = lat2 - lat1
        dlon = lon2 - lon1
        a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        distance = radius * c

    altitude_diff = altitude2 - altitude1
    total_distance = math.sqrt(distance**2 + altitude_diff**2)
    return total_distance

def get_coordinates(language):
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
            if not (-90 <= lat <= 90 and -180 <= lon <= 180):
                print("Invalid coordinates! Latitude must be between -90 and 90, Longitude between -180 and 180.")
                continue
            return lat, lon, alt
        except ValueError:
            print("Invalid input. Please enter valid numerical values.")

def choose_language():
    while True:
        language = input("Choose language / Choisissez la langue (en/fr): ").strip().lower()
        if language in ['en', 'fr']:
            return language
        else:
            print("Invalid language choice, defaulting to English.")
            return 'en'

def choose_mode(language):
    while True:
        if language == 'en':
            mode = input("Choose calculation mode (spherical/ellipsoidal): ").strip().lower()
        else:
            mode = input("Choisissez le mode de calcul (sphérique/ellipsoïdal): ").strip().lower()
        if mode in ['spherical', 'ellipsoidal']:
            return mode
        else:
            print("Invalid mode. Please choose 'spherical' or 'ellipsoidal'.")

def choose_unit(language):
    while True:
        if language == 'en':
            unit = input("Choose units for distance (km or mi): ").strip().lower()
        else:
            unit = input("Choisissez l'unité pour la distance (km ou mi) : ").strip().lower()
        if unit in ['km', 'mi']:
            return unit
        else:
            print("Invalid unit. Please choose 'km' or 'mi'.")

def main():
    language = choose_language()
    if language == 'en':
        print("\nAdvanced Geographical Distance Calculator")
    else:
        print("\nCalculateur Avancé de Distance Géographique")

    print("\nPoint 1:")
    lat1, lon1, alt1 = get_coordinates(language)

    print("\nPoint 2:")
    lat2, lon2, alt2 = get_coordinates(language)

    mode = choose_mode(language)
    unit = choose_unit(language)

    distance = geodesic(lat1, lon1, lat2, lon2, alt1, alt2, unit, mode)

    if language == 'en':
        print(f"\nThe distance between the two points is {distance:.2f} {unit}.")
    else:
        print(f"\nLa distance entre les deux points est de {distance:.2f} {unit}.")

if __name__ == "__main__":
    main()
