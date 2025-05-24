from .elevator_state import ElevatorState

class MaintenanceState(ElevatorState):
    def handle(self, elevator, target_floor):
        print(f"Elevador {elevator.id} em manutenção - movimento não permitido")
        elevator.notify_observers("maintenance", elevator.current_floor)
    
    def get_state_name(self):
        return "Manutenção"
