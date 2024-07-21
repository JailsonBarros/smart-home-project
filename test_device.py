from device import Light, Thermostat, SecuritySystem, AirConditioner, DoorLock

def test_device(device):
    """
    Função para testar um dispositivo, alterando seus estados e exibindo o status.

    :param device: Instância do dispositivo a ser testado.
    """
    print(device.get_status())  # Mostra o status inicial

    # Testando transições de estado específicas para cada dispositivo
    if isinstance(device, Light):
        device.turn_on()
        print(device.get_status())
        device.turn_off()
        print(device.get_status())
    elif isinstance(device, Thermostat):
        device.heat()
        print(device.get_status())
        device.cool()
        print(device.get_status())
        device.turn_off()
        print(device.get_status())
    elif isinstance(device, SecuritySystem):
        device.arm_home()
        print(device.get_status())
        device.disarm()
        print(device.get_status())
        device.arm_away()
        print(device.get_status())
        device.disarm()
        print(device.get_status())
    elif isinstance(device, AirConditioner):
        device.cool()
        print(device.get_status())
        device.turn_off()
        print(device.get_status())
    elif isinstance(device, DoorLock):
        device.unlock()
        print(device.get_status())
        device.lock()
        print(device.get_status())
        device.unlock()
        print(device.get_status())
        device.lock_with_alarm()
        print(device.get_status())
        device.unlock()
        print(device.get_status())
    else:
        print("Unknown device type")

def main():
    """
    Função principal para executar os testes.
    """
    # Instancia os dispositivos
    light = Light()
    thermostat = Thermostat()
    security_system = SecuritySystem()
    air_conditioner = AirConditioner()
    door_lock = DoorLock()

    # Testa cada dispositivo
    print("Testing Light:")
    test_device(light)

    print("\nTesting Thermostat:")
    test_device(thermostat)

    print("\nTesting SecuritySystem:")
    test_device(security_system)

    print("\nTesting AirConditioner:")
    test_device(air_conditioner)

    print("\nTesting DoorLock:")
    test_device(door_lock)

if __name__ == "__main__":
    main()
