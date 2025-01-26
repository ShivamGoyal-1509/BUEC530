import math
import pandas as pd

def haversine(lat1, lon1, lat2, lon2):
    """
    Calculate the great-circle distance between two points on the Earth.
    
    Parameters:
    lat1, lon1 -- Latitude and Longitude of point 1 in decimal degrees
    lat2, lon2 -- Latitude and Longitude of point 2 in decimal degrees
    
    Returns:
    Distance in kilometers.
    """
    R = 6371.0  # Radius of the Earth in kilometers
    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)
    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)

    dlat = lat2_rad - lat1_rad
    dlon = lon2_rad - lon1_rad

    a = math.sin(dlat / 2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return R * c

def validate_lat_lon(lat, lon):
    """
    Validate latitude and longitude values.
    
    Parameters:
    lat -- Latitude in decimal degrees
    lon -- Longitude in decimal degrees
    
    Returns:
    True if valid, False otherwise.
    """
    return -90 <= lat <= 90 and -180 <= lon <= 180

def dms_to_decimal(degrees, minutes, seconds):
    """
    Convert DMS (degrees, minutes, seconds) format to decimal degrees.
    
    Parameters:
    degrees -- Degrees
    minutes -- Minutes
    seconds -- Seconds
    
    Returns:
    Decimal degrees.
    """
    return degrees + (minutes / 60) + (seconds / 3600)

def load_csv(file_path):
    """
    Load latitude and longitude data from a CSV file. Handles cases where column names are missing.
    
    Parameters:
    file_path -- Path to the CSV file.
    
    Returns:
    DataFrame with latitude and longitude columns.
    """
    # Load the CSV file
    df = pd.read_csv(file_path)

    # Add column names if missing
    if df.columns.size == 0 or not {'latitude', 'longitude'}.issubset(df.columns):
        df.columns = ['latitude', 'longitude']
        print("Column names were missing; added 'latitude' and 'longitude'.")

    # Validate latitude and longitude values
    df = df[df.apply(lambda row: validate_lat_lon(row['latitude'], row['longitude']), axis=1)]
    print(f"Filtered invalid coordinates. Remaining rows: {len(df)}")
    
    return df

def find_shortest_distance_from_csv(file1, file2):
    """
    Find the shortest distance between points in two CSV files.
    
    Parameters:
    file1 -- Path to the first CSV file.
    file2 -- Path to the second CSV file.
    
    Returns:
    Closest pair of points and their distance in kilometers.
    """
    df1 = load_csv(file1)
    df2 = load_csv(file2)

    array1 = list(zip(df1['latitude'], df1['longitude']))
    array2 = list(zip(df2['latitude'], df2['longitude']))

    return find_shortest_distance(array1, array2)

# Example Usage with DMS
# Convert degrees, minutes, seconds to decimal and use for haversine
latitude_decimal = dms_to_decimal(52, 31, 0)  # Example: 52°31'0"
longitude_decimal = dms_to_decimal(13, 24, 18)  # Example: 13°24'18"
print(f"Decimal Coordinates: {latitude_decimal}, {longitude_decimal}")
