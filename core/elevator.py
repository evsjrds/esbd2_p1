from states.stopped_state import StoppedState

class Elevator:   
    def __init__(self, elevator_id):
        self.id = elevator_id
        self.current_floor = 1
        self.state = StoppedState()
        self.observers = []
        self.weight_capacity = 1000 
        self.current_weight = 0     
        print(f"Elevador {self.id} criado no andar {self.current_floor}")
    
    def add_observer(self, observer):
        self.observers.append(observer)
        print(f"Observer {observer.__class__.__name__} adicionado ao elevador {self.id}")
    
    def remove_observer(self, observer):
        if observer in self.observers:
            self.observers.remove(observer)
    
    def notify_observers(self, event, data):
        for observer in self.observers:
            observer.update(self.id, event, data)
    
    def set_state(self, new_state):
        old_state_name = self.state.get_state_name()
        self.state = new_state
        new_state_name = self.state.get_state_name()
        print(f"Elevador {self.id}: Estado alterado de '{old_state_name}' para '{new_state_name}'")
    
    def move_to_floor(self, target_floor):
        print(f"Elevador {self.id} recebeu solicitação para andar {target_floor}")
        self.state.handle(self, target_floor)
    
    def set_maintenance_mode(self):
        from states.maintenance_state import MaintenanceState
        self.set_state(MaintenanceState())
        self.notify_observers("maintenance", self.current_floor)
    
    def get_current_status(self):
        return {
            "id": self.id,
            "current_floor": self.current_floor,
            "state": self.state.get_state_name()
        }
    def simulate_overload(self, weight):
        self.current_weight = weight
        if weight > self.weight_capacity:
            print(f"SOBRECARGA detectada no elevador {self.id}: {weight}kg > {self.weight_capacity}kg")
            self.notify_observers("overload", {"weight": weight, "capacity": self.weight_capacity})
    
    def simulate_power_failure(self):
        print(f"FALHA DE ENERGIA detectada no elevador {self.id}")
        self.notify_observers("power_failure", {"floor": self.current_floor})
    
    def simulate_emergency(self, emergency_type):
        print(f"EMERGÊNCIA detectada no elevador {self.id}: {emergency_type}")
        self.notify_observers("emergency", {"type": emergency_type, "floor": self.current_floor})