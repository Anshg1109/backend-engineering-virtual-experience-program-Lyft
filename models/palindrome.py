from car import Car
from engines.sternman_engine import SternmanEngine
from batteries.spindler_battery import SpindlerBattery
from tires.octoprime_tire import OctoprimeTire

class Palindrome(Car):

    def __init__(self,warning_light_on, last_service_date, tire_sensor_data):
        palindrome_engine = SternmanEngine(warning_light_on)
        palindrome_battery = SpindlerBattery(last_service_date)
        palindrome_tire = OctoprimeTire(tire_sensor_data)
        super().__init__(palindrome_engine, palindrome_battery, palindrome_tire)
        self.battery = palindrome_battery
        self.engine = palindrome_engine
        self.tire = palindrome_tire
        
    def needs_service(self):
        return super().needs_service()