# Smart Home System 🏠✨

Welcome to the Smart Home System repository! 🎉 This project is a complete implementation of a smart home system that allows you to control various smart devices via a command-line interface (CLI). Below, you'll find a detailed overview of the project, setup instructions, usage examples, and more.

## Overview 🌟

The Smart Home System lets you manage multiple smart devices in your home, including lights 💡, thermostats 🌡️, security systems 🚨, air conditioners ❄️, and door locks 🔒. The system uses state machines to handle device states and provides a user-friendly CLI for easy interaction.

## Features 🚀

- **Device Management**: Add, remove, and control devices. 🛠️
- **Device Status**: Check the status of specific devices or all devices. 📊
- **Device Filtering**: Filter and view devices by type. 🔍
- **Light Control**: Control all lights at once. 🌟
- **Device Counting**: Count and list active devices. 🔢

## Components & Design Patterns 🛠️

### Components

- **Device**: Abstract base class for all devices. 🏗️
- **Light**: Represents a light device. 💡
- **Thermostat**: Represents a thermostat device. 🌡️
- **SecuritySystem**: Represents a security system device. 🚨
- **AirConditioner**: Represents an air conditioner device. ❄️
- **DoorLock**: Represents a door lock device. 🔒
- **SmartHome**: Manages all devices in the system. 🏠
- **DeviceFactory**: Creates devices based on type. 🏭
- **Observer**: Notifies about device state changes. 📩

### Design Patterns

- **State Pattern**: Manages device states with transitions. 🔄
- **Factory Pattern**: Creates devices dynamically. 🏭
- **Observer Pattern**: Notifies changes in device states. 👀

## Setup Instructions 🛠️

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/JailsonBarros/smart-home-project.git
   cd smart-home-system
   ```

2. **Install Dependencies**:

    Ensure you have Python installed, then install the required packages:

    ```bash
    pip install transitions
    ```

3. **Run the System**:

    Execute the CLI script to start interacting with the system:

    ```bash
    python cli.py
    ```

## CLI Usage Examples 💻

1. **Add a Device** ➕

    To add a new device, you will be prompted to enter the device type:

    ```text
    Enter the maximum number of devices: 5
    Menu Options:
    1. Add Device
    2. Remove Device
    3. View Status of Specific Devices
    4. Control Device
    5. Filter Devices and Show Status
    6. Change State of All Lights
    7. List All Devices
    8. Exit
    Choose an option: 1
    Enter the device type (light, thermostat, security, air_conditioner, door_lock): light
    Light added successfully!
    ```

2. **Remove a Device** ➖

    To remove an existing device, enter the device name:

    ```text
    Menu Options:
    1. Add Device
    2. Remove Device
    3. View Status of Specific Devices
    4. Control Device
    5. Filter Devices and Show Status
    6. Change State of All Lights
    7. List All Devices
    8. Exit
    Choose an option: 2
    Enter the name of the device to remove: device_1
    Device removed successfully!
    ```

3. **View Status of Specific Devices** 📋

    To view the status of specific devices, enter the device type:

    ```text
    Menu Options:
    1. Add Device
    2. Remove Device
    3. View Status of Specific Devices
    4. Control Device
    5. Filter Devices and Show Status
    6. Change State of All Lights
    7. List All Devices
    8. Exit
    Choose an option: 3
    Enter the device type to show status (light, thermostat, security, air_conditioner, door_lock): light
    Status of Light devices:
    device_1: Light is on
    ```

4. **Control a Device** 🎛️

    To control a specific device, enter the device name and the desired action:

    ```text
    Menu Options:
    1. Add Device
    2. Remove Device
    3. View Status of Specific Devices
    4. Control Device
    5. Filter Devices and Show Status
    6. Change State of All Lights
    7. List All Devices
    8. Exit
    Choose an option: 4
    Enter the name of the device to control: device_1
    Enter the action (turn_on, turn_off): turn_on
    Action executed successfully!
    ```

5. **Filter Devices and Show Status** 🔍

    To filter and display devices of a specific type:

    ```text
    Menu Options:
    1. Add Device
    2. Remove Device
    3. View Status of Specific Devices
    4. Control Device
    5. Filter Devices and Show Status
    6. Change State of All Lights
    7. List All Devices
    8. Exit
    Choose an option: 5
    Enter the device type to filter (light, thermostat, security, air_conditioner, door_lock): air_conditioner
    Air Conditioner devices:
    device_2: Air Conditioner is off
    ```

6. **Change State of All Lights** 💡

    To change the state of all lights:

    ```text
    Menu Options:
    1. Add Device
    2. Remove Device
    3. View Status of Specific Devices
    4. Control Device
    5. Filter Devices and Show Status
    6. Change State of All Lights
    7. List All Devices
    8. Exit
    Choose an option: 6
    Enter the action for all lights (turn_on, turn_off): turn_off
    Action 'turn_off' executed for all lights!
    ```

7. **List All Devices** 📋

    To list all devices and their statuses:

    ```text
    Menu Options:
    1. Add Device
    2. Remove Device
    3. View Status of Specific Devices
    4. Control Device
    5. Filter Devices and Show Status
    6. Change State of All Lights
    7. List All Devices
    8. Exit
    Choose an option: 7
    List of all devices:
    device_1: Light is off
    device_2: Air Conditioner is on
    device_3: Door Lock is locked
    ```

8. **Exit** ➕

    To exit the CLI:

    ```text
    Menu Options:
    1. Add Device
    2. Remove Device
    3. View Status of Specific Devices
    4. Control Device
    5. Filter Devices and Show Status
    6. Change State of All Lights
    7. List All Devices
    8. Exit
    Choose an option: 8
    Exiting...
    ```

## Conclusion 🎉

Thank you for exploring the Smart Home System! We hope you find it useful and easy to use. If you have any questions or feedback, feel free to reach out. Enjoy managing your smart home!
