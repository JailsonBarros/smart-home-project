from device import Device, Light, Thermostat, SecuritySystem, AirConditioner, DoorLock

class SmartHome:
    """
    Classe para representar a casa inteligente com o padrão Singleton.
    """
    _instance = None
    
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(SmartHome, cls).__new__(cls)
        return cls._instance

    def __init__(self, max_devices=10):
        """
        Inicializa a casa inteligente com um limite de dispositivos.

        :param max_devices: Número máximo de dispositivos permitidos.
        """
        if not hasattr(self, 'initialized'):
            self.devices = {}
            self.device_count = 0
            self.max_devices = max_devices
            self.initialized = True

    def add_device(self, name: str, device: Device):
        """
        Adiciona um dispositivo ao sistema.

        :param name: Nome do dispositivo.
        :param device: Instância do dispositivo a ser adicionado.
        """
        if len(self.devices) >= self.max_devices:
            raise Exception("Device limit reached")
        if name in self.devices:
            raise ValueError(f"Device with name {name} already exists.")
        self.devices[name] = device

    def remove_device(self, name: str):
        """
        Remove um dispositivo do sistema.

        :param name: Nome do dispositivo a ser removido.
        """
        if name in self.devices:
            del self.devices[name]
        else:
            raise KeyError("Device not found.")

    def get_device_status(self, name: str) -> str:
        """
        Obtém o status de um dispositivo específico.

        :param name: Nome do dispositivo.
        :return: Status do dispositivo em formato de string.
        """
        if name in self.devices:
            return self.devices[name].get_status()
        return f'{name} not found'

    def get_statuses(self):
        """
        Obtém o status de todos os dispositivos no sistema.

        :return: Uma lista de strings, onde cada string representa o status de um dispositivo.
        """
        return [f'{name}: {device.get_status()}' for name, device in self.devices.items()]

    def get_all_status(self, device_type: str) -> str:
        """
        Obtém o status de todos os dispositivos de um tipo específico.

        :param device_type: O tipo de dispositivo para filtrar (e.g., 'light', 'thermostat').
        :return: Uma string com o status de todos os dispositivos do tipo especificado.
        :raises ValueError: Se o tipo de dispositivo não for reconhecido.
        """
        device_classes = {
            'light': Light,
            'thermostat': Thermostat,
            'security': SecuritySystem,
            'air_conditioner': AirConditioner,
            'door_lock': DoorLock
        }
        device_class = device_classes.get(device_type)
        if not device_class:
            raise ValueError(f"Tipo de dispositivo desconhecido: {device_type}")
        
        statuses = [f'{name}: {device.get_status()}' for name, device in self.devices.items() if isinstance(device, device_class)]
        return '\n'.join(statuses) if statuses else "Nenhum dispositivo encontrado."

    def get_active_devices(self):
        """
        Retorna uma lista de dispositivos que estão ativos (ou seja, não estão em estado 'off').

        :return: Uma lista de dispositivos que estão em um estado diferente de 'off'.
        """
        return [device for device in self.devices.values() if device.state != 'off']

    def count_active_devices(self):
        """
        Conta o número de dispositivos que estão ativos (ou seja, não estão em estado 'off').

        :return: O número total de dispositivos ativos.
        """
        return sum(1 for device in self.devices.values() if device.state != 'off')

    def control_lights(self, action):
        """
        Aplica uma ação a todas as luzes no sistema.

        :param action: A ação a ser aplicada (e.g., 'turn_on', 'turn_off').
        :raises ValueError: Se a ação não for reconhecida ou se algum dispositivo não for do tipo Light.
        """
        if action not in ['turn_on', 'turn_off']:
            raise ValueError(f"Ação não reconhecida: {action}. Use 'turn_on' ou 'turn_off'.")
        
        for device in self.devices.values():
            if isinstance(device, Light):
                if action == 'turn_on' and device.state == 'on':
                    continue  # Já está ligado, não faz nada
                elif action == 'turn_off' and device.state == 'off':
                    continue  # Já está desligado, não faz nada
                if hasattr(device, action):
                    getattr(device, action)()
                    device.notify_observers()
                else:
                    raise ValueError(f"Ação {action} não encontrada para Light.")
                
    def list_all_devices(self):
        """
        Lista todos os dispositivos na casa inteligente.

        :return: Lista de strings com o nome e o status de todos os dispositivos.
        """
        return [f"{name}: {device.get_status()}" for name, device in self.devices.items()]
