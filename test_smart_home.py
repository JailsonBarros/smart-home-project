from smart_home import SmartHome
from device import Light, Thermostat, SecuritySystem, AirConditioner, DoorLock

def test_smarthome():
    """
    Testa todas as funcionalidades do sistema de casa inteligente.
    """
    # Cria uma instância do sistema de casa inteligente
    smarthome = SmartHome(max_devices=12)  # Limite de dispositivos é 12 para o teste

    # Adiciona dispositivos
    light1 = Light()
    light2 = Light()
    thermostat1 = Thermostat()
    thermostat2 = Thermostat()
    security_system = SecuritySystem()
    air_conditioner = AirConditioner()
    door_lock = DoorLock()

    smarthome.add_device('light1', light1)
    smarthome.add_device('light2', light2)
    smarthome.add_device('thermostat1', thermostat1)
    smarthome.add_device('thermostat2', thermostat2)
    smarthome.add_device('security_system', security_system)
    assert smarthome.get_all_status('air_conditioner') == 'Nenhum dispositivo encontrado.'
    smarthome.add_device('air_conditioner', air_conditioner)
    smarthome.add_device('door_lock', door_lock)

    # Testa status dos dispositivos
    assert smarthome.get_device_status('light1') == 'Light is off'
    assert smarthome.get_device_status('light2') == 'Light is off'
    assert smarthome.get_device_status('thermostat1') == 'Thermostat is off'
    assert smarthome.get_device_status('thermostat2') == 'Thermostat is off'
    assert smarthome.get_device_status('security_system') == 'Security System is disarmed'
    assert smarthome.get_device_status('air_conditioner') == 'Air Conditioner is off'
    assert smarthome.get_device_status('door_lock') == 'Door Lock is locked'

    # Testa transições de estado dos dispositivos
    light1.turn_on()
    light2.turn_on()
    assert smarthome.get_device_status('light1') == 'Light is on'
    assert smarthome.get_device_status('light2') == 'Light is on'
    
    light1.turn_off()
    light2.turn_off()
    assert smarthome.get_device_status('light1') == 'Light is off'
    assert smarthome.get_device_status('light2') == 'Light is off'

    thermostat1.heat()
    thermostat2.cool()
    assert smarthome.get_device_status('thermostat1') == 'Thermostat is heating'
    assert smarthome.get_device_status('thermostat2') == 'Thermostat is cooling'
    thermostat1.turn_off()
    thermostat2.turn_off()
    assert smarthome.get_device_status('thermostat1') == 'Thermostat is off'
    assert smarthome.get_device_status('thermostat2') == 'Thermostat is off'

    # Testa ligar e desligar todas as luzes
    smarthome.control_lights('turn_on')
    assert smarthome.get_all_status('light') == 'light1: Light is on\nlight2: Light is on'
    smarthome.control_lights('turn_off')
    assert smarthome.get_all_status('light') == 'light1: Light is off\nlight2: Light is off'

    # Testa status de todos os dispositivos de um tipo específico
    smarthome.control_lights('turn_on')  # Todas as luzes estão ligadas agora
    

    # Testa limite de dispositivos
    smarthome.add_device('extra_device_1', Light())
    smarthome.add_device('extra_device_2', Thermostat())
    smarthome.add_device('extra_device_3', SecuritySystem())
    smarthome.add_device('extra_device_4', AirConditioner())
    smarthome.add_device('extra_device_5', DoorLock())
    assert len(smarthome.devices) == 12  # O limite é 12 dispositivos

    # Tenta adicionar mais dispositivos além do limite
    try:
        smarthome.add_device('extra_device_6', Light())
    except Exception as e:
        assert str(e) == 'Device limit reached'

    print("All tests passed!")


if __name__ == "__main__":
    test_smarthome()
