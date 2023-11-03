from car import Car
from engines.capulet_engine import CapuletEngine
from batteries.nubbin_battery import NUBBIN_BATTERY
from tires.carrigan_tire import CarriganTire

class Thovex(Car):
    def __init__(self,current_mileage, last_service_mileage, last_service_date, tire_sensor_data):
        Thovex_engine = CapuletEngine(current_mileage, last_service_mileage)
        Thovex_battery = NUBBIN_BATTERY(last_service_date)
        Thovex_tire = CarriganTire(tire_sensor_data)
        super().__init__(Thovex_engine, Thovex_battery, Thovex_tire)
        self.battery = Thovex_battery
        self.engine = Thovex_engine
        self.tire = Thovex_tire
    def needs_service(self):
        return super().needs_service()