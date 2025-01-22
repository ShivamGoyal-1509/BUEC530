import math

def haversine(lat1, lon1, lat2, lon2):

    # Radius of the Earth in kilometers
    R = 6371.0
    
    # Convert latitude and longitude from degrees to radians

    # lat1, lon1 -- Latitude and Longitude of point 1 in decimal degrees
    # lat2, lon2 -- Latitude and Longitude of point 2 in decimal degrees

    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)
    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)
    
    # Compute differences
    dlat = lat2_rad - lat1_rad
    dlon = lon2_rad - lon1_rad
    
    # Haversine formula
    a = math.sin(dlat / 2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    
    # Distance in kilometers
    distance = R * c
    return distance

# Example usage:
lat1, lon1 = 52.5200, 13.4050  # Berlin, Germany
lat2, lon2 = 48.8566, 2.3522   # Paris, France

distance = haversine(lat1, lon1, lat2, lon2)
print(f"Distance between Berlin and Paris: {distance:.2f} km")