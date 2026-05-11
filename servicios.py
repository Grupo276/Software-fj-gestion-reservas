
# ============================================================
# SISTEMA DE SERVICIOS
# Integrante Jose Alejandro Reina Nuñez
# ============================================================

from Servicio_baseabstracta import Servicio
import logging 

# ============================================================
# CONFIGURACIÓN DEL SISTEMA DE LOGS
# ============================================================

logging.basicConfig(
    filename="servicios.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8"
)  

# ============================================================
# CLASE: RESERVA DE SALAS
# ============================================================

class ReservaSala(Servicio):

    COSTO_HORA = 50000

    def __init__(self, cliente, fecha, horas, tipo_sala):
        
        # Integración con Servicio_baseabstracta.py 
        super().__init__("Reserva de Sala", self.COSTO_HORA) 
        
        # Mantener lógica original 
        self.cliente = cliente 
        self.fecha = fecha 
        self.horas = horas 
        self.tipo_sala = tipo_sala 
    
     # --------------------------------------------------------
    # Método para validar horas
    # --------------------------------------------------------
    def validar_horas(self):

        if self.horas <= 0:

            logging.error(
                f"Horas inválidas para el cliente "
                f"{self.cliente}: {self.horas}"
            )

            raise ValueError(
                "Las horas deben ser mayores a 0"
            ) 

    # --------------------------------------------------------
    # Sobrescritura del método calcular_costo
    # --------------------------------------------------------
    def calcular_costo(self, impuesto=0, descuento=0): 

        self.validar_horas()

        costo = self.horas * self.COSTO_HORA

        # Sala VIP tiene recargo
        if self.tipo_sala.lower() == "vip":
            costo += 100000
        
        # Aplicar impuesto
        if impuesto > 0: 
            costo += costo * impuesto 
        
        # Aplicar descuento
        if descuento > 0:
            costo -= costo * descuento 

        return costo
    
    # ---------------------------------------------------
    # Método obligatorio de la clase abastracta
    # ---------------------------------------------------
    def describir_servicio(self): 
        
        return (
            f"Reserva de sala {self.tipo_sala} "
            f"por {self.horas} horas" 
        ) 

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
        
        # Integración con Servicio_baseabstracta.py 
        super().__init__("Alquiler de Equipos", self.COSTO_HORA) 
        
        # Mantener lógica original
        self.cliente = cliente
        self.fecha = fecha
        self.horas = horas
        self.cantidad_equipos = cantidad_equipos 
    
    # --------------------------------------------------------
    # Método para validar horas
    # --------------------------------------------------------
    def validar_horas(self):

        if self.horas <= 0:

            logging.error(
                f"Horas inválidas para el cliente "
                f"{self.cliente}: {self.horas}"
            )

            raise ValueError(
                "Las horas deben ser mayores a 0"
            ) 

    # --------------------------------------------------------
    # Sobrescritura del método calcular_costo
    # --------------------------------------------------------
    def calcular_costo(self, impuesto=0, descuento=0): 

        self.validar_horas()

        if self.cantidad_equipos <= 0:
               
            logging.error(
                f"Cantidad inválida de equipos para {self.cliente}"
            )
               
            raise ValueError("Debe alquilar mínimo 1 equipo")
        
        costo = (
            self.horas * self.COSTO_HORA * self.cantidad_equipos
        ) 
        
        # Aplicar impuesto
        if impuesto > 0:
            costo += costo * impuesto 
        
        # Aplicar descuento
        if descuento > 0:
            costo -= costo * descuento 

        return costo 
    
    # --------------------------------------------------------
    # Método obligatorio de la clase abstracta
    # --------------------------------------------------------
    def describir_servicio(self): 
        
        return (
            f"Alquiler de "
            f"{self.cantidad_equipos} equipos "
            f"por {self.horas} horas "
        ) 

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
        
        # Integración con Servicio_baseabstract.py
        super().__init__("Asesoria", self.COSTO_HORA) 
        
        # Mantener lógica original
        self.cliente = cliente
        self.fecha = fecha
        self.horas = horas
        self.especialista = especialista 
    
    # --------------------------------------------------------
    # Método para validar horas
    # --------------------------------------------------------
    def validar_horas(self):

        if self.horas <= 0:

            logging.error(
                f"Horas inválidas para el cliente "
                f"{self.cliente}: {self.horas}"
            )

            raise ValueError(
                "Las horas deben ser mayores a 0"
            ) 

    # --------------------------------------------------------
    # Sobrescritura del método calcular_costo
    # --------------------------------------------------------
    def calcular_costo(self, impuesto=0, descuento=0): 

        self.validar_horas()
        
        costo = self.horas * self.COSTO_HORA 
        
        # Aplicar impuesto 
        if impuesto > 0:
            costo += costo * impuesto 
        
        # Aplicar descuento 
        if descuento > 0:
            costo -= costo * descuento 

        return costo 
    
    # -------------------------------------------------------
    # Método obligatorio de la clase abstracta
    # -------------------------------------------------------
    def describir_servicio(self): 
        
        return (
            f"Asesoria con "
            f"{self.especialista} " 
            f"por {self.horas} horas "
        )  

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