from aparato import Aparato

class GestorConsumo:
    def __init__(self, tarifa):
        """
        Inicializa el gestor de consumo con una tarifa por kWh
        :param tarifa: Tarifa en dólares por kWh
        """
        self.tarifa = tarifa
        self.aparatos = []

    def agregar_aparato(self, nombre, potencia, horas):
        """
        Agrega un aparato a la lista de aparatos
        """
        aparato = Aparato(nombre, potencia, horas)
        self.aparatos.append(aparato)

    def mostrar_reporte(self):
        """
        Muestra un reporte de consumo y costo por cada aparato y totales
        """
        print("\nReporte de Consumo Eléctrico\n")
        total_kwh = 0
        total_costo = 0

        for aparato in self.aparatos:
            consumo = aparato.consumo_kwh()
            costo = aparato.costo(self.tarifa)
            total_kwh += consumo
            total_costo += costo

            print(f"Aparato: {aparato.nombre}")
            print(f"  Potencia: {aparato.potencia} W")
            print(f"  Horas de uso: {aparato.horas} h")
            print(f"  Consumo: {consumo:.2f} kWh")
            print(f"  Costo: ${costo:.2f}\n")

        print("Resumen General:")
        print(f"  Consumo total: {total_kwh:.2f} kWh")
        print(f"  Gasto mensual: ${total_costo:.2f}")
