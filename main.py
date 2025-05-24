from core.elevator_system import ElevatorSystem
from factory.elevator_factory import ElevatorFactory
from observers.music_controller import MusicController
from observers.speed_controller import SpeedController

print("=== DEMONSTRAÇÃO DA INTELIGÊNCIA DO SISTEMA ===\n")

# Setup do sistema
system = ElevatorSystem()
elevators = [
    ElevatorFactory.create_elevator("E001"),
    ElevatorFactory.create_elevator("E002"), 
    ElevatorFactory.create_elevator("E003")
]

music_controller = MusicController()
speed_controller = SpeedController(system)

for elevator in elevators:
    system.add_elevator(elevator)
    elevator.add_observer(music_controller)
    elevator.add_observer(speed_controller)

print("1. OPERAÇÃO NORMAL - SEM MÚSICA")
elevators[0].move_to_floor(5)
elevators[1].move_to_floor(3)
print()

print("2. SITUAÇÃO DE PANE/MANUTENÇÃO - INTELIGÊNCIA ATIVADA")
elevators[1].set_maintenance_mode()
print()

print("3. SITUAÇÃO DE SOBRECARGA - DECISÕES INTELIGENTES")
elevators[0].simulate_overload(1200)  # Acima da capacidade
print()

print("4. SITUAÇÃO DE EMERGÊNCIA - PROTOCOLOS AUTOMÁTICOS")
elevators[2].simulate_emergency("incêndio")
print()

print("5. FALHA DE ENERGIA - MODO ECONOMIA AUTOMÁTICO")
elevators[0].simulate_power_failure()
print()

print("6. RETORNO AO NORMAL - SISTEMA SE ADAPTA")
elevators[2].move_to_floor(2)  # Operação normal volta
print()
