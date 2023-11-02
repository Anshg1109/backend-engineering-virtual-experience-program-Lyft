from abc import ABC, abstractmethod

class Engine(ABC):

    def __int__(self,current_mileage, last_service_mileage,warning_light_on = False):
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage
        self.warning_light_on = warning_light_on

    @abstractmethod
    def engine_needs_service(self):
        pass         