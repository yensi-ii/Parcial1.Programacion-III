from gestor import GestorConsumo

def main():
    print("Sistema de Control de Gasto Eléctrico")
    tarifa = float(input("Ingrese la tarifa por kWh en dólares: "))

    gestor = GestorConsumo(tarifa)

    while True:
        nombre = input("\nNombre del aparato: ")
        potencia = float(input("Potencia del aparato (W): "))
        horas = float(input("Horas de uso al mes: "))

        gestor.agregar_aparato(nombre, potencia, horas)

        opcion = input("¿Desea agregar otro aparato? (s/n): ")
        if opcion.lower() != 's':
            break

    gestor.mostrar_reporte()

if __name__ == "__main__":
    main()
