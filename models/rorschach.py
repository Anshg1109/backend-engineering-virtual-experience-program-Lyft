from car import Car
from engines.willoughby_engine import WilloughbyEngine
from batteries.nubbin_battery import NUBBIN_BATTERY

class Rorschach(Car):

    def __init__(self,current_mileage, last_service_mileage, last_service_date):
        rorschach_engine = WilloughbyEngine(current_mileage, last_service_mileage)
        rorschach_battery = NUBBIN_BATTERY(last_service_date)
        
        super().__init__(rorschach_engine, rorschach_battery)
        self.battery = rorschach_engine
        self.engine = rorschach_battery
        
    def needs_service(self):
        return super().needs_service()