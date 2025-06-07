from core.elevator import Elevator
from decorators.monitor_decorator import MonitorDecorator
from decorators.voice_decorator import VoiceDecorator
from decorators.decoration_decorator import DecorationDecorator

# Criação do elevador
elevador = Elevator("E004")

# Adicionando monitor e voz
elevador = MonitorDecorator(elevador)
elevador = VoiceDecorator(elevador)
elevador = DecorationDecorator(elevador, "Natal")

# Testando
elevador.move_to_floor(7)
status = elevador.get_current_status()
print(status)