from abc import ABC, abstractmethod
import math
import re

class Coordinate(ABC):

    def __init__(self, longitude, latitude, height) -> None:
        self.latitude = self.parse_latitude(latitude)
        self.longitude = 0
        self.height = 0
        self.height_above_ground = 0


    def get_distance_to(self, coordinate: 'Coordinate', unit: str = 'Meter') -> float:

        if not isinstance(coordinate, Coordinate):

            raise TypeError("")
        
        if not isinstance(unit, str):

            raise TypeError("")
        
        match unit:
            case 'Meter':
                earth_radius = 6_371_000.0

            case 'Kilometer':
                earth_radius = 6_371.0

            case 'Miles':
                earth_radius = 3_958.7559

            case 'Nautical Miles':
                earth_radius = 3440.0648

            case _:

                raise ValueError("Parameter unit is not valid!")
        
        from_lat = math.radians(self.latitude)
        from_long = math.radians(self.longitude)
        to_lat = math.radians(coordinate.latitude)
        to_long = math.radians(coordinate.longitude)
        diff_lat = to_lat - from_lat
        diff_long = to_long - from_long
        a = math.sin(diff_lat / 2)**2 + math.cos(from_lat) * math.cos(to_lat) * math.sin(diff_long / 2)**2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        distance = earth_radius * c

        return distance
    
    def get_direction_to(self, coordinate: 'Coordinate', unit = 'Mils') -> float:

        from_lat = math.radians(self.latitude)
        from_long = math.radians(self.longitude)
        to_lat = math.radians(coordinate.latitude)
        to_long = math.radians(coordinate.longitude)
        diff_long = to_long - from_long
        x = math.sin(diff_long) * math.cos(to_lat)
        y = math.cos(from_lat) * math.sin(to_lat) - math.sin(from_lat) * math.cos(to_lat) * math.cos(diff_long)
        azimut_rad = math.atan2(x, y)

        return
    
    def polar(self, direction: float, distance: float, elevation: float = 0) -> 'Coordinate':

        return
    
    def to_mgrs(self) -> 'Coordinate_MGRS':

        return
        

class Coordinate_MGRS(Coordinate):

    def __init__(self, coordinate: str) -> None:

        if not isinstance(coordinate, str):

            raise TypeError("")
        
        mgrs_coordinate = coordinate.replace(' ', '')
        pattern = re.compile(r'^[0-9]{1,2}[C-X]{1}[A-Z]{2}[0-9]{4,5}[0-9]{4,5}$')

        if not bool(pattern.match(mgrs_coordinate)):

            raise ValueError("Format of MGRS Grid is not valid")
        
        coordinate

        return
    
    def polar(self, direction, distance) -> 'Coordinate_MGRS':

        return self.to_mgrs(super().polar(direction, distance))
    
    def to_mgrs(coordinate: 'Coordinate') -> 'Coordinate_MGRS':

        return
    
    def __str__(self):
        pass



class Coordinate_Geo(Coordinate):

    def __init__(self) -> None:

        return
        
class Coordinate_UTM(Coordinate):

    def __init__(self) -> None:

        return
        
    def polar(self, direction, distance) -> 'Coordinate_UTM':

        return self.to_utm(super().polar(direction, distance))
    
    def to_utm(coordinate: 'Coordinate') -> 'Coordinate_UTM':

        return
    
class Coordinate_Decimal(Coordinate):

    def __init__(self, longitude: float, latitude: float, height: float = None) -> None:
        longitude = 0
        latitude = 0

        super().__init__(longitude, latitude, height)

    def __str__(self):
        lat_dir = 'N' if self.latitude >= 0 else 'S'
        long_dir = 'E' if self.longitude >= 0 else 'W'

        return f'{abs(self.latitude):.4f}{lat_dir} {abs(self.longitude):.4f}{long_dir}, H{self.height:.2f}m'
    

coord = Coordinate_Decimal('58.1234, -12.6789')
