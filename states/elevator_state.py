from abc import ABC, abstractmethod

class ElevatorState(ABC):
    @abstractmethod
    def handle(self, elevator, target_floor):
        pass
    
    @abstractmethod
    def get_state_name(self):
        pass
