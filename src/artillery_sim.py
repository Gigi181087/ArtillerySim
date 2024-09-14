from enum import Enum
import threading

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
            

    class FireUnit:

        def __init__(self):
            self._type = ArtillerySim.GunType.Artillery155mm
            self._no_of_guns = 4

    _instance = None
    _lock = threading.Lock()

    def __new__(cls, *args, **kwargs):

        if not cls.__instance:

            with cls._lock:

                if not cls.__instance:

                    cls.__instance = super(ArtillerySim, cls).__new__(cls, *args, **kwargs)

                
            
        return cls.__instance
    
    def create_fire_mission(self)