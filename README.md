# Parte III: Integrador de Reservas

Este archivo explica únicamente qué hace `main.py`, el módulo encargado de unir los clientes, servicios y reservas del sistema **Software FJ**.

## ¿Qué hace `main.py`?

`main.py` es el punto de integración del proyecto. Su responsabilidad es conectar las clases creadas en `nucleo.py` y `modelos.py` para simular reservas reales de servicios.

En concreto, este archivo:

- Importa las excepciones desde `nucleo.py`.
- Importa los clientes y servicios desde `modelos.py`.
- Define la clase `Reserva`.
- Procesa reservas usando manejo robusto de errores.
- Ejecuta una simulación con 10 operaciones.
- Muestra cuántas reservas fueron exitosas y cuántas fueron rechazadas.

## Clase `Reserva`

La clase `Reserva` representa la relación entre un cliente y un servicio contratado.

Cada reserva contiene:

- Un cliente.
- Un servicio.
- Una duración.
- Un descuento opcional.
- Opciones extra según el tipo de servicio.
- El costo total calculado.

Su método principal es `procesar()`, que valida los datos, calcula el costo y controla posibles errores.

## Manejo de errores

`main.py` usa un bloque completo:

```python
try:
    ...
except:
    ...
else:
    ...
finally:
    ...
```

Esto permite que el programa no se detenga si ocurre un error. En lugar de explotar, muestra un mensaje claro y continúa con la siguiente operación.

Errores controlados:

- Duración inválida.
- Servicio no disponible.
- Descuento fuera del rango permitido.
- Errores financieros.
- Errores inesperados.

## Función `ejecutar_simulacion()`

Esta función crea datos de prueba para demostrar que el sistema funciona.

Incluye:

- 3 clientes.
- 3 servicios diferentes.
- 10 reservas simuladas.

Algunas reservas son correctas y otras tienen errores intencionales para demostrar el manejo de excepciones.

## Cómo ejecutar

Desde la carpeta donde están los tres archivos, ejecutar:

```bash
python3 main.py
```

Al final, el programa muestra un resumen como este:

```text
Operaciones ejecutadas: 10
Reservas exitosas: 7
Reservas rechazadas: 3
```

## Punto de entrada

El archivo termina con:

```python
if __name__ == "__main__":
    ejecutar_simulacion()
```

Esto hace que la simulación se ejecute solo cuando `main.py` se corre directamente.
