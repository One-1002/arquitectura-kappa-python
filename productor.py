import json
import random
import time
from datetime import datetime

# Lista de productos de ejemplo para simular las ventas
PRODUCTOS = [
    {"id": "P01", "nombre": "Café Americano", "precio": 45.0},
    {"id": "P02", "nombre": "Tlayuda Tradicional", "precio": 120.0},
    {"id": "P03", "nombre": "Agua de Horchata", "precio": 30.0},
    {"id": "P04", "nombre": "Pan de Elote", "precio": 35.0},
]

ARCHIVO_LOG = "eventos_ventas.log"


def generar_evento():
    producto = random.choice(PRODUCTOS)
    evento = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "producto_id": producto["id"],
        "producto_nombre": producto["nombre"],
        "monto": producto["precio"],
        "cantidad": random.randint(1, 3),
    }
    return evento


def main():
    print(
        "=== PRODUCTOR DE EVENTOS INICIADO ==="
    )  # Presiona Ctrl+C para detener
    print(f"Escribiendo eventos en '{ARCHIVO_LOG}'...\n")

    try:
        while True:
            # Generar evento
            evento = generar_evento()

            # Escribir en modo 'append' (añadir al final del archivo) - El Registro Kappa
            with open(ARCHIVO_LOG, "a", encoding="utf-8") as f:
                f.write(json.dumps(evento) + "\n")

            print(
                f"[EVENTO ENVIADO] {evento['timestamp']} - Vendido: {evento['cantidad']}x {evento['producto_nombre']} (${evento['monto'] * evento['cantidad']})"
            )

            # Esperar entre 1 y 3 segundos para simular el flujo continuo
            time.sleep(random.uniform(1.0, 3.0))

    except KeyboardInterrupt:
        print("\nProductor detenido por el usuario.")


if __name__ == "__main__":
    main()