from device import Light, Thermostat, SecuritySystem, AirConditioner, DoorLock

class DeviceFactory:
    """
    Fábrica para criar instâncias de dispositivos.
    """
    def create_device(self, device_type):
        """
        Cria um dispositivo com base no tipo fornecido.

        :param device_type: Tipo do dispositivo.
        :return: Instância do dispositivo especificado.
        :raises ValueError: Se o tipo de dispositivo for desconhecido.
        """
        if device_type == 'light':
            return Light()
        elif device_type == 'thermostat':
            return Thermostat()
        elif device_type == 'security':
            return SecuritySystem()
        elif device_type == 'air_conditioner':
            return AirConditioner()
        elif device_type == 'door_lock':
            return DoorLock()
        else:
            raise ValueError(f'Unknown device type: {device_type}')
