from abc import ABC, abstractmethod
from transitions import Machine

class Device(ABC):
    """
    Classe base para dispositivos no sistema de casa inteligente.
    """
    def __init__(self):
        """
        Inicializa o dispositivo com uma máquina de estados e uma lista de observadores.
        """
        self.state = None
        self.machine = None
        self._observers = []

    @abstractmethod
    def get_status(self):
        """
        Método abstrato para obter o status do dispositivo.
        """
        pass

    def add_observer(self, observer):
        """
        Adiciona um observador para mudanças de estado.

        :param observer: Instância de Observer para notificação.
        """
        self._observers.append(observer)

    def notify_observers(self):
        """
        Notifica todos os observadores sobre mudanças no estado do dispositivo.
        """
        for observer in self._observers:
            observer.update(self)

class Light(Device):
    """
    Classe para representar um dispositivo de luz.
    """
    states = ['off', 'on']

    def __init__(self):
        """
        Inicializa a luz com seus estados e transições.
        """
        super().__init__()
        self.state = 'off'
        self.machine = Machine(model=self, states=Light.states, initial='off')
        self.machine.add_transition(trigger='turn_on', source='off', dest='on')
        self.machine.add_transition(trigger='turn_off', source='on', dest='off')

    def get_status(self):
        """
        Obtém o status atual da luz.

        :return: Status da luz em formato de string.
        """
        return f'Light is {self.state}'

class Thermostat(Device):
    """
    Classe para representar um dispositivo de termostato.
    """
    states = ['off', 'heating', 'cooling']

    def __init__(self):
        """
        Inicializa o termostato com seus estados e transições.
        """
        super().__init__()
        self.state = 'off'
        self.machine = Machine(model=self, states=Thermostat.states, initial='off')
        self.machine.add_transition(trigger='heat', source=['off', 'cooling'], dest='heating')
        self.machine.add_transition(trigger='cool', source=['off', 'heating'], dest='cooling')
        self.machine.add_transition(trigger='turn_off', source=['heating', 'cooling'], dest='off')

    def get_status(self):
        """
        Obtém o status atual do termostato.

        :return: Status do termostato em formato de string.
        """
        return f'Thermostat is {self.state}'

class SecuritySystem(Device):
    """
    Classe para representar um dispositivo de sistema de segurança.
    """
    states = ['disarmed', 'armed_home', 'armed_away']

    def __init__(self):
        """
        Inicializa o sistema de segurança com seus estados e transições.
        """
        super().__init__()
        self.state = 'disarmed'
        self.machine = Machine(model=self, states=SecuritySystem.states, initial='disarmed')
        self.machine.add_transition(trigger='arm_home', source='disarmed', dest='armed_home')
        self.machine.add_transition(trigger='arm_away', source='disarmed', dest='armed_away')
        self.machine.add_transition(trigger='disarm', source=['armed_home', 'armed_away'], dest='disarmed')

    def get_status(self):
        """
        Obtém o status atual do sistema de segurança.

        :return: Status do sistema de segurança em formato de string.
        """
        return f'Security System is {self.state}'

class AirConditioner(Device):
    """
    Classe para representar um dispositivo de ar condicionado.
    """
    states = ['off', 'cooling']

    def __init__(self):
        """
        Inicializa o ar condicionado com seus estados e transições.
        """
        super().__init__()
        self.state = 'off'
        self.machine = Machine(model=self, states=AirConditioner.states, initial='off')
        self.machine.add_transition(trigger='cool', source='off', dest='cooling')
        self.machine.add_transition(trigger='turn_off', source='cooling', dest='off')

    def get_status(self):
        """
        Obtém o status atual do ar condicionado.

        :return: Status do ar condicionado em formato de string.
        """
        return f'Air Conditioner is {self.state}'

class DoorLock(Device):
    """
    Classe para representar um dispositivo de tranca.
    """
    states = ['locked', 'unlocked', 'locked_with_alarm']

    def __init__(self):
        """
        Inicializa a tranca com seus estados e transições.
        """
        super().__init__()
        self.state = 'locked'
        self.machine = Machine(model=self, states=DoorLock.states, initial='locked')
        self.machine.add_transition(trigger='lock', source='unlocked', dest='locked')
        self.machine.add_transition(trigger='lock_with_alarm', source='unlocked', dest='locked_with_alarm')
        self.machine.add_transition(trigger='unlock', source=['locked', 'locked_with_alarm'], dest='unlocked')

    def get_status(self):
        """
        Obtém o status atual da tranca.

        :return: Status da tranca em formato de string.
        """
        return f'Door Lock is {self.state}'
