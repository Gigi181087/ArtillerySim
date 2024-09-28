import gun_sim
import artillery_sim

class FireUnitSim:

    def __init__(self, parameters: dict = None) -> None:
        self._systemn_time = 0
        self._guns: dict[str, 'gun_sim.GunSim'] = {}

        return
    
    def invalidate(self, time_ms) -> None:

        if not isinstance(time_ms, int):

            raise TypeError("")
        
        if time_ms < 0:

            raise ValueError("time_ms can't be negative!")
        
        for key, gun in self._guns.items():
            gun.update_time(time_ms)

        self._systemn_time = time_ms

        return
    
    def receive_message(self, message: dict) -> None:
        
        if "Fire Mission" in message:

            self._calculate_fire_mission(message["Fire Mission"])

        return

        
    
    def fire_mission(self, fire_mission: dict) -> None:
        
        return

