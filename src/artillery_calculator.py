from pandas import DataFrame

class ArtilleryCalculator:

    _ballistics: dict['DataFrame'] = {}

    def get_probable_error(weapon_system, distance) -> float:

        return 0