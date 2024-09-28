import json
import numpy

from enum import Enum
from shot_sim import Shot
from artillery_sim import ArtillerySim
from artillery_calculator import ArtilleryCalculator
import coordinates

class GunStatus(Enum):
    Moving = 0
    FirePosition = 1
    Loading = 2
    Loaded = 3
    CoveredPosition = 4

class GunType(Enum):
    PZH2000 = 0
    M109 = 1
    M777 = 2


class GunSim:

    def __init__(self) -> None:
        self._location = coordinates.Coordinate_MGRS(1, 1)
        self.position.x = 1
        self._system_time = 0
        self._action_queue = []
        self._shot_queue: list[dict[str, 'Shot']] = []
        self._time_busy = 0
        self._settings
        self._status: 'GunStatus' = GunStatus.Moving
        self._status_until

        return
    
    def load_default_config(self, type: 'GunType') -> None:
        file_path= ""

        match (type):

            case GunType.PZH2000:
                file_path = 'configs/pzh2000.json'

            case _:

                raise ValueError("")
            
        self._type: 'GunType' = type

        with open() as file:
            self._settings = json.load(file_path)

        return                    

    def load_custom_config(self, config: dict) -> None:

        if not isinstance(config, dict):

            raise TypeError("")
        
        if "Loading Time" in config:

            self._loading_time = config["Loading Time"]

        
    
    def invalidate(self, time_ms: int) -> None:

        if not isinstance(time_ms, int):

            raise TypeError("")
        
        if time_ms < 0:

            raise ValueError("time_ms can't be negative!")
        
        self._system_time = time_ms
        self._update()

        return

    def _do_next_action(self) -> None:

        return
        
    
    def _execute_shot(self, shot) -> None:

        for shot in self._shot_queue[:]:

            if shot.time_to_fire <= self._system_time:
                ArtillerySim.simulate_action()

        return

    def _cease_fire(self, fire_mission) -> None:

        return
    
    def _process_fire_order(self, fire_order: dict) -> None:

        if not isinstance(fire_order, dict):

            raise TypeError("")

        if not "Shots" in fire_order:

            raise SyntaxError("")

        target_coordinates = fire_order["Fire Order"]["Distribution"]

        for shot in target_coordinates:
            target_coordinate = coordinates.Coordinate_Decimal(shot["Latitude"], shot["Longitude"], shot["Height MSL"])
            distance_to_target_coordinate = self._location.get_distance_to(target_coordinate)
            direction_to_target_coordinate = self._location.get_direction_to(target_coordinate)
            probable_error_range = ArtilleryCalculator.get_probable_error(self._type, distance_to_target_coordinate)

            #generate a random error
            simulated_scatter = numpy.random.normal(0, probable_error_range, 1)
            
            # make sure its within 4 pe
            simulated_scatter = numpy.clip(simulated_scatter, 0 - (probable_error_range * 4), 0 + (probable_error_range * 4))

            # calculate scattered hit point
            target_coordinate = target_coordinate.polar(direction_to_target_coordinate, simulated_scatter)

            # create a simulated shot
            new_shot: 'Shot' = Shot()
            new_shot._time_of_flight = ArtilleryCalculator.get_time_of_flight(self._type, distance_to_target_coordinate)

            if "Time On Target" in fire_order["Fire Order"]:
                new_shot._time_to_fire =  fire_order["Fire Order"]["Time On Target"] - new_shot._time_of_flight

            else:
                new_shot._time_to_fire = 0

            new_shot.ammunition = fire_order["Fire Order"]["Ammunition"]

        return
    
    def receive_message(self, message: dict) -> None:

        if not isinstance(message, dict):

            raise TypeError("")
        
        if "Fire Order" in message:

            self._process_fire_order(message)

        return


    def _update_status(self) -> None:

        return
    