from abc import ABC, abstractmethod

class ElevatorComponent(ABC):
    @abstractmethod
    def move_to_floor(self, floor):
        pass
    @abstractmethod    
    def set_maintenance_mode(self):
        pass
    @abstractmethod
    def get_current_status(self):
        pass