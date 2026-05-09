# ============================================================
# SISTEMA DE SERVICIOS
# Integrante Jose Alejandro Reina Nuñez
# ============================================================

from abc import ABC, abstractmethod
from datetime import datetime
import logging


# ============================================================
# CONFIGURACIÓN DEL SISTEMA DE LOGS
# ============================================================

logging.basicConfig(
    filename="servicios.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


# ============================================================
# CLASE ABSTRACTA BASE
# ============================================================

class Servicio(ABC):
    """
    Clase abstracta que representa un servicio general.
    Todas las clases hijas deben implementar:
        - calcular_costo()
        - mostrar_detalle()
    """

    def __init__(self, cliente, fecha, horas):
        self.cliente = cliente
        self.fecha = fecha
        self.horas = horas

    # --------------------------------------------------------
    # Método abstracto para calcular costos
    # --------------------------------------------------------
    @abstractmethod
    def calcular_costo(self):
        pass

    # --------------------------------------------------------
    # Método abstracto para mostrar detalles
    # --------------------------------------------------------
    @abstractmethod
    def mostrar_detalle(self):
        pass

    # --------------------------------------------------------
    # Método común para validar horas
    # --------------------------------------------------------
    def validar_horas(self):
        if self.horas <= 0:

            logging.error(
                f"Horas inválidas para el cliente {self.cliente}: {self.horas}"
            )

            raise ValueError("Las horas deben ser mayores a 0")


# ============================================================
# CLASE: RESERVA DE SALAS
# ============================================================

class ReservaSala(Servicio):

    COSTO_HORA = 50000

    def __init__(self, cliente, fecha, horas, tipo_sala):
        super().__init__(cliente, fecha, horas)
        self.tipo_sala = tipo_sala

    # --------------------------------------------------------
    # Sobrescritura del método calcular_costo
    # --------------------------------------------------------
    def calcular_costo(self):

        self.validar_horas()

        costo = self.horas * self.COSTO_HORA

        # Sala VIP tiene recargo
        if self.tipo_sala.lower() == "vip":
            costo += 100000

        return costo

    # --------------------------------------------------------
    # Sobrescritura del método mostrar_detalle
    # --------------------------------------------------------
    def mostrar_detalle(self):

        print("\n===== RESERVA DE SALA =====")
        print(f"Cliente: {self.cliente}")
        print(f"Fecha: {self.fecha}")
        print(f"Horas: {self.horas}")
        print(f"Tipo de sala: {self.tipo_sala}")
        print(f"Costo total: ${self.calcular_costo():,.0f}")


# ============================================================
# CLASE: ALQUILER DE EQUIPOS
# ============================================================

class AlquilerEquipos(Servicio):

    COSTO_HORA = 30000

    def __init__(self, cliente, fecha, horas, cantidad_equipos):
        super().__init__(cliente, fecha, horas)
        self.cantidad_equipos = cantidad_equipos

    # --------------------------------------------------------
    # Sobrescritura del método calcular_costo
    # --------------------------------------------------------
    def calcular_costo(self):

        self.validar_horas()

        if self.cantidad_equipos <= 0:
               
            logging.error(
            f"Cantidad inválida de equipos para {self.cliente}"
            )
               
            raise ValueError("Debe alquilar mínimo 1 equipo")

        return self.horas * self.COSTO_HORA * self.cantidad_equipos

    # --------------------------------------------------------
    # Sobrescritura del método mostrar_detalle
    # --------------------------------------------------------
    def mostrar_detalle(self):

        print("\n===== ALQUILER DE EQUIPOS =====")
        print(f"Cliente: {self.cliente}")
        print(f"Fecha: {self.fecha}")
        print(f"Horas: {self.horas}")
        print(f"Cantidad de equipos: {self.cantidad_equipos}")
        print(f"Costo total: ${self.calcular_costo():,.0f}")


# ============================================================
# CLASE: ASESORÍAS
# ============================================================

class Asesoria(Servicio):

    COSTO_HORA = 80000

    def __init__(self, cliente, fecha, horas, especialista):
        super().__init__(cliente, fecha, horas)
        self.especialista = especialista

    # --------------------------------------------------------
    # Sobrescritura del método calcular_costo
    # --------------------------------------------------------
    def calcular_costo(self):

        self.validar_horas()

        return self.horas * self.COSTO_HORA

    # --------------------------------------------------------
    # Sobrescritura del método mostrar_detalle
    # --------------------------------------------------------
    def mostrar_detalle(self):

        print("\n===== ASESORÍA =====")
        print(f"Cliente: {self.cliente}")
        print(f"Fecha: {self.fecha}")
        print(f"Horas: {self.horas}")
        print(f"Especialista: {self.especialista}")
        print(f"Costo total: ${self.calcular_costo():,.0f}")