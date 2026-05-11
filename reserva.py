
# ============================================================
# INTEGRANTE 4 — CLASE RESERVA 
# Software FJ - Sistema de Gestión
# Mariana Espinosa Barrios
# ============================================================

import logging
from datetime import datetime

from cliente import cliente
from servicios import Servicio 


# ============================================================
# CONFIGURACIÓN DEL SISTEMA DE LOGS
# ============================================================

logging.basicConfig(
    filename="reservas.log",
    level=logging.ERROR, 
    format="%(asctime)s - %(levelname)s - %(message)s"
)


# ============================================================
# EXCEPCIONES PERSONALIZADAS
# ============================================================

class ReservaError(Exception):
    """Clase base para errores del módulo reserva."""
    pass


class ClienteInvalidoError(ReservaError):
    """Error cuando el cliente no es válido."""
    pass


class ServicioInvalidoError(ReservaError):
    """Error cuando el servicio no es válido."""
    pass


class ReservaYaConfirmadaError(ReservaError):
    """Error cuando la reserva ya fue confirmada."""
    pass


class ReservaYaCanceladaError(ReservaError):
    """Error cuando la reserva ya fue cancelada."""
    pass


class EstadoReservaError(ReservaError):
    """Error cuando el estado no permite la operación."""
    pass


# ============================================================
# CLASE RESERVA
# ============================================================

class Reserva:
    """
    Clase que representa una reserva.

    Relaciona:
        - Cliente
        - Servicio

    Funciones:
        - validar()
        - confirmar()
        - cancelar()
    """

    # Contador automático
    _contador_id = 1

    def __init__(self, cliente_obj, servicio_obj):

        try:

            # ------------------------------------------------
            # VALIDAR CLIENTE
            # ------------------------------------------------
            if cliente_obj is None:
                raise ClienteInvalidoError(
                    "Debe ingresar un cliente."
                )

            if not isinstance(cliente_obj, cliente):
                raise ClienteInvalidoError(
                    "El objeto enviado no es un cliente válido."
                )

            # Validación propia del cliente
            cliente_obj.validar()

            # ------------------------------------------------
            # VALIDAR SERVICIO
            # ------------------------------------------------
            if servicio_obj is None:
                raise ServicioInvalidoError(
                    "Debe ingresar un servicio."
                )

            # Verificar que el servicio tenga
            # Los atributos mínimos necesarios
            if (
                not hasattr(servicio_obj, "fecha")
                or not hasattr(servicio_obj, "horas")
                or not hasattr(servicio_obj, "calcular_costo")
            ): 
                raise ServicioInvalidoError(
                    "El objeto enviado no es un servicio válido"
                )

        except (
            ClienteInvalidoError,
            ServicioInvalidoError,
            ValueError
        ) as e:

            logging.error(
                f"Error creando reserva: {e}"
            )
            raise

        except Exception as e:

            logging.error(
                f"Error inesperado: {e}"
            )

            raise ReservaError(
                "Error inesperado al crear la reserva."
            ) from e

        else:

            # ID automático
            self.__id = Reserva._contador_id
            Reserva._contador_id += 1

            # Relación entre clases
            self.__cliente = cliente_obj
            self.__servicio = servicio_obj

            # Estado inicial
            self.__estado = "Pendiente"

            # Fecha creación
            self.__fecha_creacion = datetime.now()

        finally:

            logging.info(
                "Proceso de creación "
                "de reserva finalizado."
            )

    # ========================================================
    # PROPERTIES (ENCAPSULAMIENTO)
    # ========================================================

    @property
    def id(self):
        return self.__id

    @property
    def cliente(self):
        return self.__cliente

    @property
    def servicio(self):
        return self.__servicio

    @property
    def estado(self):
        return self.__estado

    @property
    def fecha_creacion(self):
        return self.__fecha_creacion

    # ========================================================
    # VALIDAR RESERVA
    # ========================================================

    def validar(self):
        
        try: 
            
            # Validar cliente
            self.__cliente.validar() 
            
            # Validar horas del servicio
            self.__servicio.validar_horas()
            
            # Probar cálculo del servicio
            self.__servicio.calcular_costo() 
            
            return True
        
        except Exception as e: 
            
            logging.error(
                f"Error valido reserva: {e}"
            )
            
            raise ReservaError(
                "La reserva no es válida."
            ) from e 
        
        finally: 
            
            logging.info(
                f"Reserva #{self.__id} validada." 
            )
    # ========================================================
    # CONFIRMAR RESERVA
    # ========================================================

    def confirmar(self):

        try:

            self.validar()

            if self.__estado == "Confirmada":
                raise ReservaYaConfirmadaError(
                    "La reserva ya fue confirmada."
                )

            if self.__estado == "Cancelada":
                raise EstadoReservaError(
                    "No se puede confirmar "
                    "una reserva cancelada."
                )

        except (
            ReservaYaConfirmadaError,
            EstadoReservaError
        ) as e:

            logging.error(
                f"Error confirmando reserva: {e}"
            )

            raise

        except Exception as e:

            logging.error(
                f"Error inesperado: {e}"
            )

            raise ReservaError(
                "No se pudo confirmar "
                "la reserva."
            ) from e

        else:

            self.__estado = "Confirmada"

            return (
                f"Reserva #{self.__id} "
                f"confirmada correctamente."
            )

        finally:

            logging.info(
                f"Reserva #{self.__id} confirmada."
            )

    # ========================================================
    # CANCELAR RESERVA
    # ========================================================

    def cancelar(self):

        try:

            if self.__estado == "Cancelada":
                raise ReservaYaCanceladaError(
                    "La reserva ya fue cancelada."
                )

        except ReservaYaCanceladaError as e:

            logging.error(
                f"Error cancelando reserva: {e}"
            )
            raise

        except Exception as e:

            logging.error(
                f"Error inesperado: {e}"
            )

            raise ReservaError(
                "No se pudo cancelar "
                "la reserva."
            ) from e

        else:

            self.__estado = "Cancelada"

            return (
                f"Reserva #{self.__id} "
                f"cancelada correctamente."
            )

        finally:

            logging.info(
                f"Reserva #{self.__id} cancelada."
            )

    # ========================================================
    # INFORMACIÓN DE LA RESERVA
    # ========================================================

    def informacion_reserva(self):

        fecha = self.__fecha_creacion.strftime(
            "%d/%m/%Y %H:%M"
        )

        return (
            f"\n===== INFORMACIÓN DE RESERVA =====\n"
            f"ID: {self.__id}\n"
            f"Cliente: "
            f"{self.__cliente.get_nombre()}\n"
            f"Documento: "
            f"{self.__cliente.get_documento()}\n"
            f"Email: "
            f"{self.__cliente.get_email()}\n"
            f"Servicio: "
            f"{type(self.__servicio).__name__}\n"
            f"Estado: {self.__estado}\n"
            f"Creada el: {fecha}"
        )

    # ========================================================
    # MÉTODOS ESPECIALES
    # ========================================================

    def __str__(self):

        return (
            f"Reserva("
            f"{self.__cliente.get_nombre()} | "
            f"Estado={self.__estado})"
        )

    def __repr__(self):

        return (
            f"Reserva("
            f"id={self.__id}, "
            f"cliente='{self.__cliente.get_nombre()}', "
            f"estado='{self.__estado}')"
        )