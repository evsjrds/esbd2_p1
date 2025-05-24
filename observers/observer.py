from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self, elevator_id, event, data):
        pass
