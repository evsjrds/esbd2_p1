from core.elevator_component import ElevatorComponent

class ElevatorDecorator(ElevatorComponent):
    def __init__(self, elevator: ElevatorComponent):
        self._elevator = elevator

    def move_to_floor(self, floor):
        return self._elevator.move_to_floor(floor)

    def set_maintenance_mode(self):
        return self._elevator.set_maintenance_mode()

    def get_current_status(self):
        return self._elevator.get_current_status()