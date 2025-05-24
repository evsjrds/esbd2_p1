from core.elevator import Elevator

class ElevatorFactory:
    @staticmethod
    def create_elevator(elevator_id, elevator_type="standard"):
        if elevator_type == "standard":
            elevator = Elevator(elevator_id)
            print(f"Factory: Elevador padrão {elevator_id} criado")
            return elevator
        else:
            raise ValueError(f"Tipo de elevador '{elevator_type}' não suportado")
