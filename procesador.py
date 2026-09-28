import json
import os
import time

ARCHIVO_LOG = "eventos_ventas.log"


def main():
    print("=== PROCESADOR DE FLUJOS (STREAM PROCESSOR) INICIADO ===")
    print("Esperando eventos...\n")

    # Esperar a que el archivo de log exista
    while not os.path.exists(ARCHIVO_LOG):
        time.sleep(1)

    # Variables de estado (Estadísticas continuas)
    total_transacciones = 0
    ingreso_total = 0.0
    productos_vendidos = {}

    # Abrir el archivo y posicionarse al final (para leer solo lo nuevo en tiempo real)
    with open(ARCHIVO_LOG, "r", encoding="utf-8") as f:
        # Ir al final del archivo
        f.seek(0, os.SEEK_END)

        try:
            while True:
                linea = f.readline()
                if not linea:
                    # Si no hay nueva línea, esperamos un momento antes de volver a leer
                    time.sleep(0.5)
                    continue

                # Procesar el evento recibido
                evento = json.loads(linea.strip())

                # Actualizar estadísticas en tiempo real
                total_transacciones += 1
                subtotal = evento["monto"] * evento["cantidad"]
                ingreso_total += subtotal

                nombre = evento["producto_nombre"]
                productos_vendidos[nombre] = (
                    productos_vendidos.get(nombre, 0) + evento["cantidad"]
                )

                # Mostrar el panel de estadísticas actualizado
                print("\n" + "=" * 40)
                print(" 📊 ESTADÍSTICAS EN TIEMPO REAL (DASHBOARD)")
                print("=" * 40)
                print(f"Total de transacciones: {total_transacciones}")
                print(f"Ingreso total acumulado: ${ingreso_total:.2f}")
                print("Desglose por productos:")
                for prod, cant in productos_vendidos.items():
                    print(f"   - {prod}: {cant} unidades")
                print("=" * 40)

        except KeyboardInterrupt:
            print("\nProcesador detenido por el usuario.")


if __name__ == "__main__":
    main()