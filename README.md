# Simulación de Arquitectura Kappa en Python

Este proyecto es una práctica académica diseñada para demostrar el funcionamiento de una **Arquitectura Kappa**, donde los datos se procesan en tiempo real como un flujo continuo de eventos (Stream Processing) utilizando un registro inmutable basada en archivos (*Append-Only Log*).

## Estructura del Proyecto

* `productor.py`: Simula la generación periódica de eventos de venta y los registra cronológicamente en un archivo de texto plano (`eventos_ventas.log`).
* `procesador.py`: Lee el flujo de eventos en tiempo real, calcula métricas acumuladas y actualiza un panel de estadísticas (*dashboard*) en la terminal.
* `eventos_ventas.log`: Archivo que actúa como el "Registro de Eventos" (simulando a Apache Kafka).

## Requisitos Previos

* Python 3.8 o superior instalado en el sistema.

## Instrucciones de Instalación y Ejecución

1. **Clonar o abrir la carpeta del proyecto** en tu terminal.

2. **Crear y activar el entorno virtual:**
   ```bash
   # Crear el entorno virtual
   python -m venv venv

   # Activar en Windows (PowerShell/CMD):
   venv\Scripts\activate

   # Activar en Mac / Linux:
   source venv/bin/activate