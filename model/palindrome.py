from car import Car
from engines.sternman_engine import SternmanEngine
from batteries.spindler_battery import SpindlerBattery

class Palindrome(Car):

    def __init__(self,warning_light_on, last_service_date):
        palindrome_engine = SternmanEngine(warning_light_on)
        palindrome_battery = SpindlerBattery(last_service_date)
        
        super().__init__(palindrome_engine, palindrome_battery)
        self.battery = palindrome_battery
        self.engine = palindrome_engine
        
    def needs_service(self):
        return super().needs_service()