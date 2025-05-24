from .elevator_state import ElevatorState

class MovingDownState(ElevatorState):
    def handle(self, elevator, target_floor):
        print(f"Elevador {elevator.id} descendo do andar {elevator.current_floor} para {target_floor}")
        elevator.current_floor = target_floor
        elevator.notify_observers("moving_down", target_floor)
        
        from .stopped_state import StoppedState
        elevator.set_state(StoppedState())
    
    def get_state_name(self):
        return "Descendo"
