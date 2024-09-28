"""Standard Modules"""
from enum import Enum
import json
from typing import Callable

"""Internal Modules"""
import fire_unit_sim

"""Submodules"""
#import variable_message_format as vmf

"""Code"""

class ArtillerySim:

    class GunType(Enum):
        Mortar60mm = 1
        Mortar81mm = 2
        Mortar120mm = 3
        Rockets110mm = 4
        Artillery155mm = 5
        Artillery203mm = 6

    class Ammunition(Enum):
        HighExplosive = 1
        Smoke = 2
        Illumination = 3

    class Gun:

        def __init__(self) -> None:
            pass
            

    class FireUnit:

        def __init__(self):
            self._type = ArtillerySim.GunType.Artillery155mm
            self._no_of_guns = 4

        def create_gun(self) -> None:
            pass



    _instance = None
    _send_message_callback: Callable = None
    _simulation_callback: Callable = None
    _fire_units: list['fire_unit_sim.FireUnitSim'] = []
    _system_time: int = 0

    def __new__(cls, *args, **kwargs):

        if not cls._instance:

            cls._instance = super(ArtillerySim, cls).__new__(cls, *args, **kwargs)
            
        return cls._instance
    
    def create_fire_unit(self, id: int = None) -> None:

        return
    
    def receive_message(self, message: dict) -> None:

        try:
            message = vmf.parse_to_json(message)

        except Exception as e:
            print(e)

    def invalidate(self, time_ms: int) -> None:

        if not isinstance(time_ms, int):

            raise TypeError("")
        
        if time_ms < 0:

            raise ValueError("time_ms can't be negative!")
        
        for fire_unit in self._fire_units:
            fire_unit.invalidate(time_ms)

        self._system_time = time_ms

        return

    def send_message(self, message: dict) -> None:

        if not isinstance(message, dict):

            raise TypeError(f'Parameter message must be of type \'dict\'. Provided type: {type(message)}')
        
        if self._send_message_callback is None:

            raise NotImplementedError(f'Couldn\'t sent message. Please setup callback to sending mechanism!')

        try:
            raw_message = vmf.parse_to_string(message)
            self._send_message_callback(raw_message)

            return
        
        except Exception as e:
            print (e)

    def simulate_action(self, action) -> None:

        return

        

