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

def find_closest_point(single_point, points_array):
    """
    Find the closest point to a given single point.
    
    Parameters:
    single_point -- Tuple of latitude and longitude (lat, lon)
    points_array -- List of tuples, each containing latitude and longitude (lat, lon)
    
    Returns:
    Tuple containing the closest point and its distance in kilometers.
    """
    lat1, lon1 = single_point
    min_distance = float('inf')
    closest_point = None
    
    for point in points_array:
        lat2, lon2 = point
        distance = haversine(lat1, lon1, lat2, lon2)
        if distance < min_distance:
            min_distance = distance
            closest_point = point
    
    return closest_point, min_distance

# Example usage:
single_point = (52.5200, 13.4050)  # Berlin, Germany
points_array = [
    (48.8566, 2.3522),   # Paris, France
    (51.5074, -0.1278),  # London, UK
    (40.7128, -74.0060), # New York, USA
    (41.9028, 12.4964)   # Rome, Italy
]

closest_point, distance = find_closest_point(single_point, points_array)
print(f"The closest point to {single_point} is {closest_point} with a distance of {distance:.2f} km.")