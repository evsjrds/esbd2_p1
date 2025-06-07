from .elevator_decorator import ElevatorDecorator

class DecorationDecorator(ElevatorDecorator):
    def __init__(self, elevator, theme):
        super().__init__(elevator)
        self.theme = theme

    def get_current_status(self):
        status = super().get_current_status()
        status['decoration'] = self.theme
        print(f"[Decoração] Elevador decorado para: {self.theme}")
        return status