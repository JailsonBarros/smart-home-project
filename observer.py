class Observer:
    """
    Observador para ser notificado sobre mudanças de estado dos dispositivos.
    """
    def __init__(self):
        """
        Inicializa o observador.
        """
        self.notifications = []

    def update(self, device):
        """
        Atualiza o observador com o status do dispositivo.

        :param device: Dispositivo com status alterado.
        """
        self.notifications.append(device.get_status())
        print(f"Observador notificado: {device.get_status()}")
