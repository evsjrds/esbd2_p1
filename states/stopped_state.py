from .elevator_state import ElevatorState

class StoppedState(ElevatorState):
    def handle(self, elevator, target_floor):
        if target_floor > elevator.current_floor:
            print(f"Elevador {elevator.id} iniciando subida")
            from .moving_up_state import MovingUpState
            elevator.set_state(MovingUpState())
            elevator.state.handle(elevator, target_floor)
        elif target_floor < elevator.current_floor:
            print(f"Elevador {elevator.id} iniciando descida")
            from .moving_down_state import MovingDownState
            elevator.set_state(MovingDownState())
            elevator.state.handle(elevator, target_floor)
        else:
            print(f"Elevador {elevator.id} já está no andar {target_floor}")
    
    def get_state_name(self):
        return "Parado"
