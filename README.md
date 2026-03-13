# Inventario_NataliaRomerin
# README – Sistema simple de registro de inventario

## Descripción

Este programa en Python permite registrar productos en un inventario de forma sencilla desde la consola.
El usuario puede ingresar el **nombre del producto, el precio y la cantidad**, y el sistema calculará automáticamente el **costo total**.

El programa también incluye **validación de datos**, lo que evita que el usuario ingrese valores incorrectos para el precio o la cantidad.

---

## Funcionamiento del programa

El programa sigue estos pasos:

1. Solicita al usuario el **nombre del producto**.
2. Solicita el **precio del producto** y verifica que sea un número válido.
3. Solicita la **cantidad del producto** y verifica que sea un número entero válido.
4. Calcula el **costo total** multiplicando el precio por la cantidad.
5. Muestra en pantalla toda la información ingresada junto con el total calculado.
6. Pregunta al usuario si desea **registrar otro producto**.
7. Si el usuario responde que sí, el proceso se repite.

---

## Fórmula utilizada

El cálculo del costo total se realiza con la siguiente operación:

```
costo_total = precio * cantidad
```

Esto permite saber cuánto cuesta el total de unidades registradas de un producto.

---

## Ejemplo de ejecución

Ejemplo de cómo se ve el programa en la consola:

```
Ingrese el nombre del producto: Lapiz
Ingrese el precio del producto: 500
Ingrese la cantidad del producto: 3

Resultado del registro:
Producto: Lapiz | Precio: 500 | Cantidad: 3 | Total: 1500
```

---

## Validación de datos

El programa verifica que:

* **El precio sea un número decimal o entero válido**
* **La cantidad sea un número entero**

Si el usuario ingresa un dato incorrecto, el programa muestra un mensaje de error y vuelve a solicitar el valor.

Ejemplo:

```
Error: debe ingresar un número válido para el precio.
```

---

## Tecnologías utilizadas

* **Python**
* Uso de funciones básicas como:

  * `input()`
  * `print()`
  * `float()`
  * `int()`
  * estructuras `while` y `try/except`

---

## Objetivo del proyecto

El objetivo de este programa es practicar conceptos básicos de programación en Python como:

* Variables
* Entrada de datos
* Conversión de tipos
* Validación de datos
* Operaciones matemáticas
* Estructuras de repetición
