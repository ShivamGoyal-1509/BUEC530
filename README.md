# BUEC530

This repository focuses on the course **EC530 (Software Engineering Principles)** for Spring 2025.

---

## Exercise 1: Shortest Distance Calculator Using Haversine Formula

### Overview

This project calculates the shortest distance between two sets of geographical points using the **Haversine formula**. It supports:
- Reading geographical data from CSV files.
- Validating latitude and longitude values.
- Converting coordinates in Degrees-Minutes-Seconds (DMS) format to decimal degrees.

---

### Features
1. **CSV File Input**:
   - Reads two CSV files containing `latitude` and `longitude` columns.
   - Automatically assigns column names if they are missing.

2. **Validation**:
   - Ensures latitude values are within `-90` to `90`.
   - Ensures longitude values are within `-180` to `180`.
   - Filters out invalid rows automatically.

3. **Haversine Distance Calculation**:
   - Computes the great-circle distance between points on Earth.

4. **DMS to Decimal Conversion**:
   - Converts coordinates in Degrees-Minutes-Seconds (DMS) format to decimal degrees for distance calculations.

5. **Shortest Distance**:
   - Finds the closest pair of points between two datasets and provides their distance in kilometers.

---

### Requirements

- **Python 3.6+**
- Required Python Libraries:
  - `pandas`
  - `math`

To install the required dependencies, run:
```bash
pip install pandas

Usage

1. Preparing CSV Files
	•	Ensure CSV files contain two columns: latitude and longitude.
	•	If column names are missing, the program will automatically assign them.

2. Running the Script

Save the Python script as shortest_distance.py, then modify and call the function:

closest_pair, distance = find_shortest_distance_from_csv('file1.csv', 'file2.csv')
print(f"The closest pair of points is {closest_pair} with a distance of {distance:.2f} km.")

3. DMS Conversion

Convert Degrees-Minutes-Seconds (DMS) to decimal degrees:

latitude_decimal = dms_to_decimal(degrees, minutes, seconds)
longitude_decimal = dms_to_decimal(degrees, minutes, seconds)

Replace degrees, minutes, and seconds with the appropriate values.

Functionality Overview

haversine(lat1, lon1, lat2, lon2)
	•	Calculates the great-circle distance between two points on Earth.
	•	Parameters:
	•	lat1, lon1: Latitude and Longitude of the first point (decimal degrees).
	•	lat2, lon2: Latitude and Longitude of the second point (decimal degrees).
	•	Returns: Distance in kilometers.

validate_lat_lon(lat, lon)
	•	Validates latitude and longitude values.
	•	Parameters:
	•	lat: Latitude in decimal degrees.
	•	lon: Longitude in decimal degrees.
	•	Returns: True if valid, False otherwise.

dms_to_decimal(degrees, minutes, seconds)
	•	Converts coordinates from Degrees-Minutes-Seconds (DMS) to decimal degrees.
	•	Parameters:
	•	degrees, minutes, seconds: Components of DMS format.
	•	Returns: Decimal degree equivalent.

load_csv(file_path)
	•	Loads geographical data from a CSV file and validates the data.
	•	Parameters:
	•	file_path: Path to the CSV file.
	•	Returns: A filtered DataFrame containing valid latitude and longitude values.

find_shortest_distance(array1, array2)
	•	Finds the shortest distance between two arrays of geographical points.
	•	Parameters:
	•	array1: List of tuples containing latitude and longitude (e.g., [(lat1, lon1), ...]).
	•	array2: List of tuples containing latitude and longitude (e.g., [(lat2, lon2), ...]).
	•	Returns: Closest pair of points and their distance in kilometers.

find_shortest_distance_from_csv(file1, file2)
	•	Finds the shortest distance between points in two CSV files.
	•	Parameters:
	•	file1: Path to the first CSV file.
	•	file2: Path to the second CSV file.
	•	Returns: Closest pair of points and their distance in kilometers.

Author

Shivam Goyal
