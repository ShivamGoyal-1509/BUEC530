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
