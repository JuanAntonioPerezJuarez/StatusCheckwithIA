# StatusCheckwithIA
Tarea para la clase de Computación Tolerante a Fallas del profesor Michel Lopez Franco

# Application Status Monitor

## Description

This Python script allows you to monitor the status of a specific application process. It continuously checks whether the specified application is running and provides real-time status updates.

## Features

- Monitor any application process by its name
- Real-time status checking every 5 seconds
- Easy-to-use command-line interface
- Graceful exit with Ctrl+C

## Requirements

- Python 3.x
- `psutil` library

## Installation

1. Ensure you have Python installed on your system
2. Install the required `psutil` library:
   ```
   pip install psutil
   ```

## Usage

Run the script and follow the prompts:

```bash
python Application.py
```

When prompted, enter the name of the application process you want to monitor (e.g., "chrome", "python", "notepad").

### Example

```
Ingrese el nombre del proceso de la aplicación que desea monitorear: chrome
Monitoreando el estado de la aplicación 'chrome'... Presione Ctrl+C para salir.
La aplicación 'chrome' está activa.
La aplicación 'chrome' está activa.
La aplicación 'chrome' no está activa.
```

## How It Works

1. The script uses `psutil` to list and check running processes
2. It compares the input application name against process names
3. Checks the application status every 5 seconds
4. Allows stopping the monitoring with a keyboard interrupt (Ctrl+C)

## Notes

- Process names are case-insensitive
- The script checks for partial matches in process names

## License

[Add your license information here]

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
