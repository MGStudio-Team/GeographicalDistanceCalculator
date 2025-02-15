# **GeographicalDistanceCalculator**

## **Description**

This tool calculates the **distance between two geographical points** using the **Haversine formula**. It takes into account **latitude, longitude,** and **altitude** differences, providing a more precise 3D distance measurement. The user can choose between two units for distance: **kilometers (km)** or **miles (mi)**. The program also allows you to choose your preferred language (**English** or **French**) at runtime.

---

## **Features**

- **Haversine Distance Calculation**: Computes the great-circle distance between two points on the Earth's surface.
- **Altitude Consideration**: Calculates the 3D distance by considering the altitude differences of the two points.
- **Multiple Units**: Choose between kilometers (km) or miles (mi) for the final distance.
- **Multi-Language Support**: Choose the interface language (English or French) at runtime.
- **Precise Calculation**: Uses Earth’s average radius (mean radius of 6371 km or 3958.8 mi) for accurate results.

---

## **Usage**

### **Step 1: Clone the repository**

To clone this repository to your local machine, use the following command:

```bash
git clone https://github.com/MGStudio-Team/GeographicalDistanceCalculator.git
```

### **Step 2: Run the Script**

After cloning the repository, navigate to the project directory and run the script.

```bash
cd GeographicalDistanceCalculator
python3 distance_calculator.py
```

### **Step 3: Language Selection**

Upon starting the script, you will be prompted to choose your language. Enter either `en` for English or `fr` for French.

```bash
Choose language / Choisissez la langue (en/fr):
```

### **Step 4: Enter Coordinates**

After selecting the language, you will be prompted to input the coordinates (latitude, longitude) and altitude (in meters) for two points.

```bash
Point 1:
Enter latitude:
Enter longitude:
Enter altitude (in meters):

Point 2:
Enter latitude:
Enter longitude:
Enter altitude (in meters):
```

### **Step 5: Choose Units**

Next, select the unit of measurement for the distance calculation, either **kilometers (km)** or **miles (mi)**.

```bash
Choose units for distance (km or mi):
```

### **Step 6: View the Result**

The program will calculate and display the distance between the two points in the selected unit.

```bash
The distance between the two points is 100.34 km.
```

---

## **Example**

### **Example 1 (English)**

```bash
Choose language / Choisissez la langue (en/fr): en
Advanced Geographical Distance Calculator

Point 1:
Enter latitude: 51.5074
Enter longitude: -0.1278
Enter altitude (in meters): 35

Point 2:
Enter latitude: 48.8566
Enter longitude: 2.3522
Enter altitude (in meters): 130

Choose units for distance (km or mi): km

The distance between the two points is 343.80 km.
```

### **Example 2 (Français)**

```bash
Choisissez la langue (en/fr) : fr
Calculateur Avancé de Distance Géographique

Point 1 :
Entrez la latitude : 51.5074
Entrez la longitude : -0.1278
Entrez l'altitude (en mètres) : 35

Point 2 :
Entrez la latitude : 48.8566
Entrez la longitude : 2.3522
Entrez l'altitude (en mètres) : 130

Choisissez l'unité de la distance (km ou mi) : km

La distance entre les deux points est de 343.80 km.
```

---

## **How It Works**

1. **Haversine Formula**: This formula is used to calculate the great-circle distance between two points on the Earth's surface, considering Earth's curvature. It takes latitude and longitude in radians.
   
2. **Altitude Difference**: The distance is further enhanced by considering the altitude difference between the two points, making the measurement 3D.

3. **User Interaction**: The user selects the language, inputs coordinates, and chooses the unit for the distance (km or mi), making the program flexible and adaptable.

---

## **Installation**

If you'd like to use or modify the project locally, follow these steps:

1. **Install Python 3.x**: This script is written in Python, so make sure Python 3.x is installed on your system.

2. **Install Required Libraries**:
   The script uses basic Python libraries, and there are no external dependencies required.

3. **Run the Script**:
   Use the command line to execute the script as shown above.

---

## **Contributing**

Contributions are welcome! If you find any bugs or would like to suggest improvements, feel free to submit an issue or a pull request.

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Create a new pull request.

## **Acknowledgments**

- Thanks to the **Python community** for providing great resources.
- The **Haversine formula** is based on well-known mathematical principles.
- The **altitude consideration** is a basic enhancement for more precise 3D measurements.
