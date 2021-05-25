import numpy as np

class Minkowski():
    def __init__(self):
        pass
        
    def minkowski_distance(self, x1, x2, y1, y2, p):
        delta_x = x1 - x2
        delta_y = y1 - y2
        return ((abs(delta_x) ** p) + (abs(delta_y)) ** p) ** (1 / p)
        
    # in a GPS coordinates system, the Minkowksi distance should be implented as follows:
    # convert degrees to radians
    def deg2rad(self, coordinate):
        return coordinate * np.pi / 180

    # convert radians into distance
    def rad2dist(self, coordinate):
        earth_radius = 6371 # km
        return earth_radius * coordinate

    # correct the longitude distance regarding the latitude (https://jonisalonen.com/2014/computing-distance-between-coordinates-can-be-simple-and-fast/)
    def lng_dist_corrected(self, lng_dist, lat):
        return lng_dist * np.cos(lat)

    def minkowski_distance_gps(self, lat1, lat2, lon1, lon2, p):
        """
        Cartesian system of 2-dims, minkowski distance can be implemented as follows:
        p=1 for Manhattan distance, p=2 for Euclidean distance
        """
        lat1, lat2, lon1, lon2 = [self.deg2rad(coordinate) for coordinate in [lat1, lat2, lon1, lon2]]
        y1, y2, x1, x2 = [self.rad2dist(angle) for angle in [lat1, lat2, lon1, lon2]]
        x1, x2 = [self.lng_dist_corrected(elt['x'], elt['lat']) for elt in [{'x': x1, 'lat': lat1}, {'x': x2, 'lat': lat2}]]
        return self.minkowski_distance(x1, x2, y1, y2, p)
