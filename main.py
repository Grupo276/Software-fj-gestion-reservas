
# ============================================================
# MAIN - SISTEMA SOFTWARE FJ
# ============================================================

from cliente import cliente
from servicios import (
    ReservaSala,
    AlquilerEquipos,
    Asesoria
)
from reserva import Reserva


print("\n===== SOFTWARE FJ =====")


# ============================================================
# LISTAS INTERNAS DEL SISTEMA
# (Ayudan a cumplir el requisito del proyecto)
# ============================================================

clientes = []
servicios = []
reservas = []


# ============================================================
# 1. CLIENTE VÁLIDO
# ============================================================

try:

    cliente1 = cliente(
        "Mariana Espinosa",
        123456789,
        "mariana@gmail.com"
    )

    clientes.append(cliente1)

    print("\nCliente creado correctamente:")
    print(cliente1)

except Exception as e:
    print(f"Error: {e}")


# ============================================================
# 2. SERVICIO VÁLIDO - RESERVA DE SALA
# ============================================================

try:

    servicio1 = ReservaSala(
        cliente1,
        "2026-05-15",
        2,
        "VIP"
    )

    servicios.append(servicio1)

    servicio1.mostrar_detalle()

except Exception as e:
    print(f"Error: {e}")


# ============================================================
# 3. SERVICIO VÁLIDO - ALQUILER DE EQUIPOS
# ============================================================

try:

    servicio2 = AlquilerEquipos(
        cliente1,
        "2026-05-16",
        3,
        2
    )

    servicios.append(servicio2)

    servicio2.mostrar_detalle()

except Exception as e:
    print(f"Error: {e}")


# ============================================================
# 4. SERVICIO VÁLIDO - ASESORÍA
# ============================================================

try:

    servicio3 = Asesoria(
        cliente1,
        "2026-05-17",
        1,
        "Ingeniero de Sistemas"
    )

    servicios.append(servicio3)

    servicio3.mostrar_detalle()

except Exception as e:
    print(f"Error: {e}")


# ============================================================
# 5. RESERVA EXITOSA
# ============================================================

try:

    print("\n===== CREANDO RESERVA =====")

    reserva1 = Reserva(
        cliente1,
        servicio1
    )

    reservas.append(reserva1)

    print(
        reserva1.informacion_reserva()
    )

except Exception as e:
    print(f"Error: {e}")


# ============================================================
# 6. CONFIRMAR RESERVA
# ============================================================

try:

    print("\n===== CONFIRMANDO RESERVA =====")

    mensaje = reserva1.confirmar()

    print(mensaje)

    print(
        reserva1.informacion_reserva()
    )

except Exception as e:
    print(f"Error: {e}")


# ============================================================
# 7. CANCELAR RESERVA
# ============================================================

try:

    print("\n===== CANCELANDO RESERVA =====")

    mensaje = reserva1.cancelar()

    print(mensaje)

    print(
        reserva1.informacion_reserva()
    )

except Exception as e:
    print(f"Error: {e}")


# ============================================================
# 8. CLIENTE INVÁLIDO
# ============================================================

try:

    print("\n===== CLIENTE INVÁLIDO =====")

    cliente_malo = cliente(
        "Juan Perez",
        123456,
        "correo_invalido"
    )

except Exception as e:
    print(f"Error capturado: {e}")


# ============================================================
# 9. SERVICIO INVÁLIDO
# ============================================================

try:

    print("\n===== SERVICIO INVÁLIDO =====")

    servicio_malo = ReservaSala(
        cliente1,
        "2026-05-20",
        -2,   # horas inválidas
        "VIP"
    )

    servicio_malo.mostrar_detalle()

except Exception as e:
    print(f"Error capturado: {e}")


# ============================================================
# 10. RESERVA FALLIDA
# ============================================================

try:

    print("\n===== RESERVA FALLIDA =====")

    reserva_mala = Reserva(
        cliente1,
        "esto no es un servicio valido"
    )

except Exception as e:
    print(f"Error capturado: {e}")

# ============================================================
# 11. CÁLCULO CON IMPUESTO
# ============================================================

try:

    print("\n===== COSTO CON IMPUESTO =====")

    total_impuesto = servicio1.calcular_costo_con_impuesto(
        horas=2,
        impuesto=0.19
    )

    print(f"Costo con IVA: ${total_impuesto:,.0f}")

except Exception as e:
    print(f"Error capturado: {e}")


# ============================================================
# 12. CÁLCULO CON DESCUENTO
# ============================================================

try:

    print("\n===== COSTO CON DESCUENTO =====")

    total_descuento = servicio2.calcular_costo_con_descuento(
        horas=3,
        descuento=0.10
    )

    print(f"Costo con descuento: ${total_descuento:,.0f}")

except Exception as e:
    print(f"Error capturado: {e}")


# ============================================================
# 13. SERVICIO NO DISPONIBLE
# ============================================================

try:

    print("\n===== SERVICIO NO DISPONIBLE =====")

    servicio3.disponible = False

    servicio3.verificar_disponibilidad()

except Exception as e:
    print(f"Error capturado: {e}")

# ============================================================
# 14. INFORMACIÓN GENERAL DEL SERVICIO
# ============================================================

try:

    print("\n===== INFORMACIÓN GENERAL =====")

    print(
        servicio1.informacion_general()
    )

except Exception as e:
    print(f"Error capturado: {e}") 


# ============================================================
# FINAL DEL SISTEMA
# ============================================================

finally:

    print("\n===== RESUMEN DEL SISTEMA =====")
    print(f"Clientes registrados: {len(clientes)}")
    print(f"Servicios registrados: {len(servicios)}")
    print(f"Reservas registradas: {len(reservas)}")

    print("\nSistema finalizado.")