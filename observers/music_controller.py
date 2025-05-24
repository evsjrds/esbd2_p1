from .observer import Observer

class MusicController(Observer):
    def __init__(self):
        self.emergency_playlists = {
            "maintenance": ["Música relaxante tocando.. - Aguarde, voltaremos em breve"],
            "emergency": ["Anúncio: Mantenha a calma - Socorro a caminho"],
            "overload": ["Anúncio: Por favor, redistribuam o peso"],
            "power_failure": ["Anúncio: Energia sendo restaurada"]
        }
        self.active_music = {}  # Controla qual elevador está tocando música
    
    def update(self, elevator_id, event, data):
        if event == "maintenance":
            self._handle_maintenance_situation(elevator_id)
        elif event == "emergency":
            self._handle_emergency_situation(elevator_id)
        elif event == "overload":
            self._handle_overload_situation(elevator_id)
        elif event == "power_failure":
            self._handle_power_failure(elevator_id)
        elif event in ["moving_up", "moving_down", "stopped"]:
            self._stop_music_if_playing(elevator_id)
    
    def _handle_maintenance_situation(self, elevator_id):
        """Situação de pane/manutenção - música para acalmar usuários"""
        if elevator_id not in self.active_music:
            music = self.emergency_playlists["maintenance"][0]
            self.active_music[elevator_id] = music
            print(f"Reproduzindo música de manutenção {music} no elevador {elevator_id}")
            print(f"Motivo: Elevador em pane - tranquilizando usuários")
    
    def _handle_emergency_situation(self, elevator_id):
        """Situação de emergência - orientações por áudio"""
        music = self.emergency_playlists["emergency"][0]
        self.active_music[elevator_id] = music
        print(f"Reproduzindo {music} no elevador {elevator_id}")
    
    def _handle_overload_situation(self, elevator_id):
        """Situação de sobrecarga - música + orientação"""
        music = self.emergency_playlists["overload"][0]
        self.active_music[elevator_id] = music
        print(f"Reproduzindo {music} no elevador {elevator_id}")
    
    def _handle_power_failure(self, elevator_id):
        """Situação de falha de energia - música tranquilizante"""
        music = self.emergency_playlists["power_failure"][0]
        self.active_music[elevator_id] = music
        print(f"Reproduzindo {music} no elevador {elevator_id}")
    
    def _stop_music_if_playing(self, elevator_id):
        """Para a música quando volta ao normal"""
        if elevator_id in self.active_music:
            del self.active_music[elevator_id]
            print(f"Música interrompida no elevador {elevator_id} - operação normalizada")
