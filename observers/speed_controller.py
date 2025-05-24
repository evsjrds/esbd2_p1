from .observer import Observer

class SpeedController(Observer):
    def __init__(self, elevator_system):
        self.elevator_system = elevator_system
        self.normal_speed = 100
        self.safety_speeds = {
            "maintenance_nearby": 60,    
            "emergency": 40,             
            "overload_compensation": 70, 
            "power_saving": 80           
        }
    
    def update(self, elevator_id, event, data):
        if event == "maintenance":
            self._intelligent_speed_control_for_maintenance(elevator_id)
        elif event == "emergency":
            self._intelligent_emergency_speed_control(elevator_id)
        elif event == "overload":
            self._intelligent_overload_compensation(elevator_id)
        elif event == "power_failure":
            self._intelligent_power_saving_mode(elevator_id)
        elif event in ["moving_up", "moving_down"]:
            self._check_normal_operation_optimization(elevator_id)
    
    def _intelligent_speed_control_for_maintenance(self, maintenance_elevator_id):
        print(f"Analisando impacto da manutenção do elevador {maintenance_elevator_id}")
        
        operational_elevators = [e for e in self.elevator_system.get_all_elevators() 
                               if e.id != maintenance_elevator_id and 
                               e.state.get_state_name() != "Manutenção"]
        
        if len(operational_elevators) <= 2:
            speed = self.safety_speeds["maintenance_nearby"]
            print(f"Velocidade reduzida para {speed}% nos elevadores operacionais")
            print(f"Apenas {len(operational_elevators)} elevadores disponíveis")
        else:
            print(f"Capacidade suficiente - mantendo velocidade normal")
    
    def _intelligent_emergency_speed_control(self, elevator_id):
        print(f"Ativando protocolo de emergência")
        print(f"Todos os elevadores em velocidade de segurança: {self.safety_speeds['emergency']}%")
        print(f"Protocolo de segurança em emergências")
    
    def _intelligent_overload_compensation(self, overload_elevator_id):
        print(f"Detectada sobrecarga no elevador {overload_elevator_id}")
        
        available_elevators = [e for e in self.elevator_system.get_all_elevators() 
                             if e.id != overload_elevator_id]
        
        print(f"Otimizando velocidade dos {len(available_elevators)} elevadores disponíveis")
        print(f"Velocidade ajustada para {self.safety_speeds['overload_compensation']}% para absorver demanda extra")
    
    def _intelligent_power_saving_mode(self, affected_elevator_id):
        print(f"Ativando modo economia de energia")
        print(f"Velocidade reduzida para {self.safety_speeds['power_saving']}% em todos os elevadores")
    
    def _check_normal_operation_optimization(self, elevator_id):
        active_elevators = len([e for e in self.elevator_system.get_all_elevators() 
                               if e.state.get_state_name() in ["Subindo", "Descendo"]])
        
        if active_elevators >= 3:
            print(f"Alto tráfego detectado - {active_elevators} elevadores ativos")
            print(f"Otimizando fluxo - ajuste automático de velocidades")
