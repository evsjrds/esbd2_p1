from decorators.elevator_decorator import ElevatorDecorator

class MonitorDecorator(ElevatorDecorator):
    def move_to_floor(self, floor):
        result = super().move_to_floor(floor)
        print(f"[Monitor] Mostrando no display: Andar {floor}")
        return result