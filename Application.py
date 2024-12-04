import psutil
import time

def check_application_status(app_name):
    """
    Revisa si una aplicación está activa.
    :param app_name: Nombre del proceso de la aplicación (por ejemplo, "chrome" o "python").
    :return: True si el proceso está activo, False en caso contrario.
    """
    for process in psutil.process_iter(attrs=['pid', 'name']):
        if app_name.lower() in process.info['name'].lower():
            return True
    return False

def main():
    app_name = input("Ingrese el nombre del proceso de la aplicación que desea monitorear: ")
    print(f"Monitoreando el estado de la aplicación '{app_name}'... Presione Ctrl+C para salir.")
    
    try:
        while True:
            is_running = check_application_status(app_name)
            if is_running:
                print(f"La aplicación '{app_name}' está activa.")
            else:
                print(f"La aplicación '{app_name}' no está activa.")
            time.sleep(5)  # Espera 5 segundos antes de verificar nuevamente
    except KeyboardInterrupt:
        print("\nMonitoreo detenido.")

if __name__ == "__main__":
    main()
