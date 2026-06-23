# Sistema de Gestión de Restaurante

## Información del Estudiante
* **Nombre Completo:** Jorge Adrián Santamaría Muñoz
* **Carrera:** Tecnologías de la Información 

---

## Descripción del Sistema
Este proyecto consiste en un Sistema Básico de Gestión de Restaurante desarrollado bajo el paradigma de **Programación Orientada a Objetos** en Python. 
El sistema permite:
1. Definir **Productos** (platos o bebidas) con sus respectivos precios y disponibilidad.
2. Registrar **Clientes** y llevar el control individual de sus datos en el sistema.
3. Contar con un servicio llamado **Restaurante** que administra de forma centralizada el menú disponible y los clientes registrados.

El objetivo principal de este proyecto es demostrar la correcta aplicación de conceptos de arquitectura de software como la modularización, la separación de responsabilidades, el uso de tipos de datos anotados y la comunicación entre archivos mediante importaciones.

---

## Estructura del Proyecto

El proyecto respeta estrictamente la siguiente estructura modular:

```text
restaurante_app/
├── modelos/
│   ├── producto.py      # Clase Producto: Define la estructura de los platos.
│   └── cliente.py       # Clase Cliente: Gestiona los datos del cliente y sus pedidos.
├── servicios/
│   └── restaurante.py   # Clase Restaurante: Coordina el negocio.
└── main.py              # Punto de entrada: Ejecuta y simula el flujo.