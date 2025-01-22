import math

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

def find_shortest_distance(array1, array2):
    """
    Find the shortest distance between two arrays of points.
    
    Parameters:
    array1 -- List of tuples, each containing latitude and longitude (lat, lon)
    array2 -- List of tuples, each containing latitude and longitude (lat, lon)
    
    Returns:
    Tuple containing the closest pair of points and their distance in kilometers.
    """
    min_distance = float('inf')
    closest_pair = None

    for point1 in array1:
        for point2 in array2:
            distance = haversine(point1[0], point1[1], point2[0], point2[1])
            if distance < min_distance:
                min_distance = distance
                closest_pair = (point1, point2)
    
    return closest_pair, min_distance

# Example usage:
array1 = [
    (52.5200, 13.4050),  # Berlin, Germany
    (48.8566, 2.3522),   # Paris, France
    (41.9028, 12.4964)   # Rome, Italy
]

array2 = [
    (51.5074, -0.1278),  # London, UK
    (40.7128, -74.0060), # New York, USA
    (55.7558, 37.6173)   # Moscow, Russia
]

closest_pair, distance = find_shortest_distance(array1, array2)
print(f"The closest pair of points is {closest_pair} with a distance of {distance:.2f} km.")