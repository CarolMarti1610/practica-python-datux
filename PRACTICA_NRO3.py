class Conductor:
    def __init__(self, nombre):
        self.nombre = nombre
        self.horarios = []  # Lista de horas en las que el conductor trabaja

    def asignar_horario(self, hora):
        if hora in self.horarios:
            print(f"Error: El conductor {self.nombre} ya tiene asignado el horario {hora}h.")
            return False
        self.horarios.append(hora)
        return True

class Bus:
    def __init__(self, placa):
        self.placa = placa
        self.ruta = None
        self.horarios = []  # Lista de horas en las que el bus opera
        self.conductor = None
    
    def asignar_ruta(self, ruta):
        self.ruta = ruta

    def registrar_horario(self, hora):
        if hora in self.horarios:
            print(f"Error: El bus {self.placa} ya tiene asignado el horario {hora}h.")
            return False
        self.horarios.append(hora)
        return True
    
    def asignar_conductor(self, conductor):
        if self.conductor is not None:
            print(f"Error: El bus {self.placa} ya tiene asignado al conductor {self.conductor.nombre}.")
            return False
        for hora in self.horarios:
            if hora in conductor.horarios:
                print(f"Error: El conductor {conductor.nombre} ya tiene un bus asignado en el horario {hora}h.")
                return False
        self.conductor = conductor
        return True

class Admin:
    def __init__(self):
        self.buses = []
        self.conductores = []
    
    def agregar_bus(self, placa):
        bus = Bus(placa)
        self.buses.append(bus)
        print(f"Bus {placa} agregado correctamente.")

    def agregar_conductor(self, nombre):
        conductor = Conductor(nombre)
        self.conductores.append(conductor)
        print(f"Conductor {nombre} agregado correctamente.")
    
    def asignar_ruta_a_bus(self, placa, ruta):
        bus = self.buscar_bus(placa)
        if bus:
            bus.asignar_ruta(ruta)
            print(f"Ruta {ruta} asignada al bus {placa}.")
    
    def registrar_horario_bus(self, placa, hora):
        bus = self.buscar_bus(placa)
        if bus:
            bus.registrar_horario(hora)
    
    def asignar_horario_conductor(self, nombre, hora):
        conductor = self.buscar_conductor(nombre)
        if conductor:
            conductor.asignar_horario(hora)
    
    def asignar_conductor_a_bus(self, nombre, placa):
        conductor = self.buscar_conductor(nombre)
        bus = self.buscar_bus(placa)
        if conductor and bus:
            bus.asignar_conductor(conductor)
    
    def buscar_bus(self, placa):
        for bus in self.buses:
            if bus.placa == placa:
                return bus
        print(f"Error: No se encontró el bus con placa {placa}.")
        return None
    
    def buscar_conductor(self, nombre):
        for conductor in self.conductores:
            if conductor.nombre == nombre:
                return conductor
        print(f"Error: No se encontró el conductor con nombre {nombre}.")
        return None
    
    def mostrar_buses(self):
        for bus in self.buses:
            print(f"Bus {bus.placa}, Ruta: {bus.ruta}, Horarios: {bus.horarios}, Conductor: {bus.conductor}")

    def mostrar_conductores(self):
        for conductor in self.conductores:
            print(f"Conductor: {conductor.nombre}, Horarios: {conductor.horarios}")


    def menu(self):
        while True:
            print("\n--- Sistema de Gestión de Buses ---")
            print("1. Agregar bus")
            print("2. Agregar conductor")
            print("3. Asignar ruta a bus")
            print("4. Registrar horario a bus")
            print("5. Asignar horario a conductor")
            print("6. Asignar conductor a bus")
            print("7. Mostrar Buses")
            print("8. Mostrar conductores")
            print("9. Salir")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                placa = input("Ingrese la placa del bus: ")
                self.agregar_bus(placa)
            elif opcion == "2":
                nombre = input("Ingrese el nombre del conductor: ")
                self.agregar_conductor(nombre)
            elif opcion == "3":
                placa = input("Ingrese la placa del bus: ")
                ruta = input("Ingrese la ruta: ")
                self.asignar_ruta_a_bus(placa, ruta)
            elif opcion == "4":
                placa = input("Ingrese la placa del bus: ")
                hora = int(input("Ingrese el horario (en formato de 24h, solo la hora): "))
                self.registrar_horario_bus(placa, hora)
            elif opcion == "5":
                nombre = input("Ingrese el nombre del conductor: ")
                hora = int(input("Ingrese el horario (en formato de 24h, solo la hora): "))
                self.asignar_horario_conductor(nombre, hora)
            elif opcion == "6":
                nombre = input("Ingrese el nombre del conductor: ")
                placa = input("Ingrese la placa del bus: ")
                self.asignar_conductor_a_bus(nombre, placa)
            elif opcion == "7":
                self.mostrar_buses()
            elif opcion == "8":
                self.mostrar_conductores()
            elif opcion == "9":
                print("Saliendo del sistema...")
                break
            else:
                print("Opción inválida, intente de nuevo.")

#5. Agregando buses y conductores
admin = Admin()

bus1 = admin.agregar_bus("1")
bus2 = admin.agregar_bus("2")
conductor1 = admin.agregar_conductor("Anderson")
conductor2 = admin.agregar_conductor("Carol")

#6. Asignación de las rutas y horarios
admin.asignar_ruta_a_bus("1" ,"Ruta A")
admin.registrar_horario_bus("1", 8)
admin.registrar_horario_bus("1", 10)

#7. Asignamos los conductores a los buses
admin.asignar_conductor_a_bus("Anderson", "1")


admin.menu()