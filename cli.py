from smart_home import SmartHome
from device_factory import DeviceFactory
from observer import Observer
from device import Light, Thermostat, SecuritySystem, AirConditioner, DoorLock

def main():
    """
    Main function to interact with the smart home system via CLI.
    """
    # Request the maximum number of devices from the user
    max_devices = int(input("Enter the maximum number of devices: "))
    
    # Initialize the smart home system with the provided device limit
    home = SmartHome(max_devices=max_devices)
    factory = DeviceFactory()
    observer = Observer()

    while True:
        # Display the menu options
        print("\nMenu Options:")
        print("1. Add device")
        print("2. Remove device")
        print("3. View status of specific devices")
        print("4. Control a device")
        print("5. Change the state of all lights")
        print("6. List all devices")
        print("7. List active devices")
        print("8. Count active devices")
        print("9. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            # Add a new device
            device_type = input("Enter the device type (light, thermostat, security, air_conditioner, door_lock): ").lower()
            if device_type in ['light', 'thermostat', 'security', 'air_conditioner', 'door_lock']:
                if len(home.devices) < max_devices:
                    try:
                        device = factory.create_device(device_type)
                        device.add_observer(observer)
                        home.device_count += 1
                        device_name = f'device_{home.device_count}'
                        home.add_device(device_name, device)
                        print(f"{device_type.capitalize()} added successfully!")
                    except ValueError as e:
                        print(e)
                    except Exception as e:
                        print(e)
                else:
                    print("Maximum number of devices reached!")
            else:
                print("Unknown device type!")
        elif choice == '2':
            # Remove an existing device
            device_name = input("Enter the name of the device to remove: ")
            try:
                home.remove_device(device_name)
                print("Device removed successfully!")
            except KeyError:
                print("Invalid device name!")
        elif choice == '3':
            # Display status of specific devices
            device_type = input("Enter the device type to show status (light, thermostat, security, air_conditioner, door_lock): ").lower()
            if device_type in ['light', 'thermostat', 'security', 'air_conditioner', 'door_lock']:
                device_class = factory.create_device(device_type).__class__
                statuses = [f"{name}: {device.get_status()}" for name, device in home.devices.items() if isinstance(device, device_class)]
                if statuses:
                    print(f"Status of {device_type.capitalize()} devices:")
                    for status in statuses:
                        print(status)
                else:
                    print(f"There are no {device_type.capitalize()} devices.")
            else:
                print("Unknown device type!")
        elif choice == '4':
            # Control a specific device
            device_name = input("Enter the name of the device to control: ")
            if device_name in home.devices:
                device = home.devices[device_name]
                if isinstance(device, Light):
                    action = input("Enter the action (turn_on, turn_off): ").lower()
                    action_mapping = {'turn_on': 'turn_on', 'turn_off': 'turn_off'}
                elif isinstance(device, Thermostat):
                    action = input("Enter the action (heat, cool, turn_off): ").lower()
                    action_mapping = {'heat': 'heat', 'cool': 'cool', 'turn_off': 'turn_off'}
                elif isinstance(device, SecuritySystem):
                    action = input("Enter the action (arm_home, arm_away, disarm): ").lower()
                    action_mapping = {'arm_home': 'arm_home', 'arm_away': 'arm_away', 'disarm': 'disarm'}
                elif isinstance(device, AirConditioner):
                    action = input("Enter the action (cool, heat, turn_off): ").lower()
                    action_mapping = {'cool': 'cool', 'heat': 'heat', 'turn_off': 'turn_off'}
                elif isinstance(device, DoorLock):
                    action = input("Enter the action (unlock, lock, lock_with_alarm): ").lower()
                    action_mapping = {'unlock': 'unlock', 'lock': 'lock', 'lock_with_alarm': 'lock_with_alarm'}
                else:
                    print("Unsupported device!")
                    continue

                try:
                    # Executes the selected action
                    getattr(device, action_mapping[action])()
                    device.notify_observers()
                    print("Action executed successfully!")
                except (AttributeError, KeyError):
                    print("Invalid action!")
            else:
                print("Invalid device name!")
        elif choice == '5':
            # Change the state of all lights
            action = input("Enter the action for all lights (turn_on, turn_off): ").lower()
            action_mapping = {'turn_on': 'turn_on', 'turn_off': 'turn_off'}
            
            if action in action_mapping:
                try:
                    home.control_lights(action_mapping[action])
                    print(f"Action '{action}' executed for all lights!")
                except ValueError as e:
                    print(e)
            else:
                print("Unknown action!")
        elif choice == '6':
            # List all devices
            devices = home.list_all_devices()
            if devices:
                print("List of all devices:")
                for device_info in devices:
                    print(device_info)
            else:
                print("No devices found.")
        elif choice == '7':
            # List active devices
            active_devices = home.get_active_devices()
            if active_devices:
                print("Active devices:")
                for name, device in home.devices.items():
                    if device in active_devices:
                        print(f"{name}: {device.get_status()}")
            else:
                print("No active devices found.")
        elif choice == '8':
            # Count active devices
            active_count = home.count_active_devices()
            print(f"Number of active devices: {active_count}")
        elif choice == '9':
            # Exit the program
            print("Exiting...")
            break
        else:
            print("Invalid option! Please try again.")

if __name__ == '__main__':
    main()
