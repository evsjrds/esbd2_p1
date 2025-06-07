from .elevator_decorator import ElevatorDecorator

class VoiceDecorator(ElevatorDecorator):
    def move_to_floor(self, floor):
        result = super().move_to_floor(floor)
        print(f"[Voz] Anunciando: Chegando ao andar {floor}")
        return result