from car import Car
from engines.capulet_engine import CapuletEngine
from batteries.nubbin_battery import NUBBIN_BATTERY


class Thovex(Car):
    def __init__(self,current_mileage, last_service_mileage, last_service_date):
        Thovex_engine = CapuletEngine(current_mileage, last_service_mileage)
        Thovex_battery = NUBBIN_BATTERY(last_service_date)
        
        super().__init__(Thovex_engine, Thovex_battery)
        self.battery = Thovex_battery
        self.engine = Thovex_engine
        
    def needs_service(self):
        return super().needs_service()