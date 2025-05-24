class ElevatorSystem:
    _instance = None
    _initialized = False
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ElevatorSystem, cls).__new__(cls)
        return cls._instance
    
    def __init__(self):
        if not ElevatorSystem._initialized:
            self.elevators = {}
            ElevatorSystem._initialized = True
            print("Sistema de Elevadores inicializado (Singleton)")
    
    def add_elevator(self, elevator):
        self.elevators[elevator.id] = elevator
        print(f"Elevador {elevator.id} adicionado ao sistema")
    
    def get_elevator(self, elevator_id):
        return self.elevators.get(elevator_id)
    
    def get_all_elevators(self):
        return list(self.elevators.values())
