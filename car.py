from engine import Engine
from battery import Battery

class Car(Engine, Battery):

    def __init__(self, engine, battery):
        self.engine = engine
        self.battery = battery
    
    def battery_needs_service(self):
        return self.battery_needs_service()
    
    def engine_needs_service(self):
        return self.engine_needs_service()
    
    def needs_service(self):
        return self.battery_needs_service() or self.engine_needs_service()