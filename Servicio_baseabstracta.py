# ============================================================
# INTEGRANTE 2 — CLASE ABSTRACTA SERVICIO
# Software FJ - Sistema de Gestión
# ============================================================

from abc import ABC, abstractmethod   # para hacer clases abstractas
import logging                         # para guardar errores en archivo
import datetime                        # para registrar fechas


# ──────────────────────────────────────────────────────────
# PASO 1: Configurar el sistema de LOGS
# Esto hace que todos los errores se guarden en un archivo
# ──────────────────────────────────────────────────────────

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s | %(levelname)-8s | %(message)s",
    handlers=[
        logging.FileHandler("softwarefj_log.txt", encoding="utf-8"),
    ]
)


# ──────────────────────────────────────────────────────────
# PASO 2: Excepciones personalizadas
# Son errores "propios" que nosotros inventamos para el sistema
# ──────────────────────────────────────────────────────────

class ServicioError(Exception):
    """Error general del módulo Servicio."""
    pass


class NombreInvalidoError(ServicioError):
    """Se lanza cuando el nombre del servicio está vacío o es inválido."""
    pass


class PrecioInvalidoError(ServicioError):
    """Se lanza cuando el precio no es un número positivo."""
    pass


class ServicioNoDisponibleError(ServicioError):
    """Se lanza cuando se intenta usar un servicio desactivado."""
    pass


class ParametroFaltanteError(ServicioError):
    """Se lanza cuando falta un parámetro obligatorio."""
    pass


class CalculoInconsistenteError(ServicioError):
    """Se lanza cuando el resultado de un cálculo no tiene sentido."""
    pass


# ──────────────────────────────────────────────────────────
# PASO 3: Clase abstracta Servicio
# Esta es la PLANTILLA que deben seguir todos los servicios
# ──────────────────────────────────────────────────────────

class Servicio(ABC):
    """
    Clase abstracta base para todos los servicios de Software FJ.

    ¿Qué significa abstracta?
    → No se puede usar directamente.
    → Obliga a las clases hijas a implementar ciertos métodos.
    → Es como un contrato: "si heredas de mí, debes tener estos métodos".
    """

    # Contador automático de IDs
    _contador_id = 1

    def __init__(self, nombre: str, precio_base: float, disponible: bool = True):
        """
        Constructor: se ejecuta cada vez que se crea un servicio.

        nombre      → nombre del servicio (texto)
        precio_base → precio por hora o unidad (número)
        disponible  → True si está activo, False si no
        """

        # ── try/except/else/finally completo ──
        # Validamos los datos antes de guardarlos
        try:
            # Validar nombre
            if nombre is None:
                raise ParametroFaltanteError("El parámetro 'nombre' es obligatorio y no fue enviado.")
            if not isinstance(nombre, str) or nombre.strip() == "":
                raise NombreInvalidoError(f"El nombre '{nombre}' no es válido. Debe ser texto no vacío.")

            # Validar precio
            if precio_base is None:
                raise ParametroFaltanteError("El parámetro 'precio_base' es obligatorio y no fue enviado.")
            if not isinstance(precio_base, (int, float)):
                raise PrecioInvalidoError(f"El precio debe ser un número. Se recibió: {type(precio_base).__name__}")
            if precio_base <= 0:
                raise PrecioInvalidoError(f"El precio debe ser mayor a 0. Se recibió: {precio_base}")

            # Validar disponible
            if not isinstance(disponible, bool):
                raise ServicioError(f"'disponible' debe ser True o False. Se recibió: {disponible}")

        except (ParametroFaltanteError, NombreInvalidoError, PrecioInvalidoError) as e:
            # Registramos el error en el log
            logging.error(f"[SERVICIO] Error al crear servicio: {e}")
            raise  # volvemos a lanzar el error para que el sistema lo sepa

        except ServicioError as e:
            logging.error(f"[SERVICIO] Error de configuración: {e}")
            raise

        except Exception as e:
            # Encadenamiento de excepción: atrapamos lo inesperado
            logging.critical(f"[SERVICIO] Error inesperado al crear servicio: {e}")
            raise ServicioError("Error inesperado al inicializar el servicio.") from e

        else:
            # Este bloque SOLO se ejecuta si NO hubo ningún error
            # Aquí guardamos los datos porque ya sabemos que son válidos
            self.__id           = Servicio._contador_id
            Servicio._contador_id += 1
            self.__nombre       = nombre.strip()
            self.__precio_base  = float(precio_base)
            self.__disponible   = disponible
            self.__fecha_creacion = datetime.datetime.now()

            logging.info(f"[SERVICIO] Creado exitosamente: '{self.__nombre}' | Precio: ${self.__precio_base:,.0f}")

        finally:
            # Este bloque SIEMPRE se ejecuta, haya error o no
            logging.debug(f"[SERVICIO] Intento de creación de servicio con nombre='{nombre}' finalizado.")


    # ──────────────────────────────────────────────────────
    # PASO 4: Propiedades
    # Forma segura de leer los atributos privados (con __)
    # ──────────────────────────────────────────────────────

    @property
    def id(self):
        return self.__id

    @property
    def nombre(self):
        return self.__nombre

    @property
    def precio_base(self):
        return self.__precio_base

    @property
    def disponible(self):
        return self.__disponible

    @disponible.setter
    def disponible(self, valor: bool):
        """Permite activar o desactivar el servicio."""
        try:
            if not isinstance(valor, bool):
                raise ServicioError(f"'disponible' debe ser True o False. Se recibió: {valor}")
            self.__disponible = valor
            estado = "ACTIVADO" if valor else "DESACTIVADO"
            logging.info(f"[SERVICIO] '{self.__nombre}' → {estado}")

        except ServicioError as e:
            logging.error(f"[SERVICIO] No se pudo cambiar disponibilidad: {e}")
            raise

    @property
    def fecha_creacion(self):
        return self.__fecha_creacion


    # ──────────────────────────────────────────────────────
    # PASO 5: Métodos abstractos
    # Estas funciones NO tienen lógica aquí (solo "pass")
    # Las clases hijas ESTÁN OBLIGADAS a implementarlas
    # ──────────────────────────────────────────────────────

    @abstractmethod
    def calcular_costo(self, horas: float = 1) -> float:
        """
        Calcula el costo del servicio según las horas.
        Cada servicio lo calcula diferente (polimorfismo).
        """
        pass

    @abstractmethod
    def describir_servicio(self) -> str:
        """
        Retorna una descripción completa del servicio.
        Cada servicio la escribe diferente (polimorfismo).
        """
        pass


    # ──────────────────────────────────────────────────────
    # PASO 6: Métodos concretos
    # Estos SÍ tienen lógica y los heredan todas las clases hijas
    # sin necesidad de reescribirlos
    # ──────────────────────────────────────────────────────

    def verificar_disponibilidad(self):
        """
        Revisa si el servicio está activo.
        Lanza excepción si no lo está.
        Uso: try/except simple
        """
        try:
            if not self.__disponible:
                raise ServicioNoDisponibleError(
                    f"El servicio '{self.__nombre}' (ID {self.__id}) no está disponible."
                )
        except ServicioNoDisponibleError as e:
            logging.warning(f"[SERVICIO] Intento de uso de servicio inactivo: {e}")
            raise

    def calcular_costo_con_impuesto(self, horas: float = 1, impuesto: float = 0.19) -> float:
        """
        Calcula el costo total incluyendo impuesto (IVA).
        Por defecto aplica 19%.
        Uso: try/except/else/finally
        """
        resultado = 0.0
        try:
            self.verificar_disponibilidad()

            if not isinstance(horas, (int, float)) or horas <= 0:
                raise ParametroFaltanteError(f"Horas inválidas: {horas}. Deben ser mayor a 0.")
            if not isinstance(impuesto, (int, float)) or not (0 <= impuesto <= 1):
                raise CalculoInconsistenteError(f"Impuesto inválido: {impuesto}. Debe estar entre 0 y 1.")

            costo_base = self.calcular_costo(horas)

            if costo_base < 0:
                raise CalculoInconsistenteError(f"El costo base no puede ser negativo: {costo_base}")

            resultado = round(costo_base * (1 + impuesto), 2)

        except (ServicioNoDisponibleError, ParametroFaltanteError, CalculoInconsistenteError) as e:
            logging.error(f"[SERVICIO] Error en cálculo con impuesto: {e}")
            raise

        except Exception as e:
            logging.critical(f"[SERVICIO] Error inesperado en cálculo con impuesto: {e}")
            raise CalculoInconsistenteError("Error inesperado calculando costo con impuesto.") from e

        else:
            logging.info(f"[SERVICIO] Costo con impuesto calculado: ${resultado:,.2f} ({horas}h, IVA {impuesto*100:.0f}%)")
            return resultado

        finally:
            logging.debug(f"[SERVICIO] Cálculo con impuesto finalizado para '{self.__nombre}'.")

    def calcular_costo_con_descuento(self, horas: float = 1, descuento: float = 0.0) -> float:
        """
        Calcula el costo aplicando un descuento.
        descuento=0.10 significa 10% menos.
        Uso: try/except/finally
        """
        try:
            self.verificar_disponibilidad()

            if not isinstance(horas, (int, float)) or horas <= 0:
                raise ParametroFaltanteError(f"Horas inválidas: {horas}")
            if not isinstance(descuento, (int, float)) or not (0 <= descuento < 1):
                raise CalculoInconsistenteError(f"Descuento inválido: {descuento}. Debe estar entre 0 y 0.99.")

            costo_base = self.calcular_costo(horas)
            resultado  = round(costo_base * (1 - descuento), 2)

            logging.info(f"[SERVICIO] Costo con descuento: ${resultado:,.2f} ({descuento*100:.0f}% desc.)")
            return resultado

        except (ServicioNoDisponibleError, ParametroFaltanteError, CalculoInconsistenteError) as e:
            logging.error(f"[SERVICIO] Error en cálculo con descuento: {e}")
            raise

        except Exception as e:
            logging.critical(f"[SERVICIO] Error inesperado en cálculo con descuento: {e}")
            raise CalculoInconsistenteError("Error inesperado calculando costo con descuento.") from e

        finally:
            logging.debug(f"[SERVICIO] Cálculo con descuento finalizado para '{self.__nombre}'.")

    def informacion_general(self) -> str:
        """Retorna información básica del servicio (compartida por todos)."""
        estado = "✓ Disponible" if self.__disponible else "✗ No disponible"
        fecha  = self.__fecha_creacion.strftime("%Y-%m-%d %H:%M")
        return (
            f"ID: {self.__id} | Nombre: {self.__nombre} | "
            f"Precio base: ${self.__precio_base:,.0f} | {estado} | Creado: {fecha}"
        )

    def __str__(self):
        estado = "Disponible" if self.__disponible else "No disponible"
        return f"[Servicio #{self.__id}] {self.__nombre} | ${self.__precio_base:,.0f}/hora | {estado}"

    def __repr__(self):
        return f"Servicio(id={self.__id}, nombre='{self.__nombre}', precio={self.__precio_base})"