## Test Funcionales con Selenium y Behave ##
El objetivo de esta práctica es realizar una serie de test con selenium y behave a una página web, en mi caso al supermercado **DIA**: [www.dia.es](https://www.dia.es/)

### Estructura de los archivos: ###

- **./** Encontramos 3 archivos creados por el gestor de paquetes **Poetry**:
  - .log
  - .lock
  - .toml

- **/features** En el feature encontramos los escenarios de los test y en el environment la carga de la página web
  - .feature
  - .py

- **/steps** Encontramos el archivo steps que contiene todos los test: 
  - .py

### Contenido de los archivos: ###

- **environment.py**

Con este archivo se abre el navegador **Firefox** y se entra a la página web del supermercado **DIA** (quitando las cookies)

- **fetures.feature**

Este archivo contiene 3 escenarios:
En el primer escenario se compruba si el título de la página **https://www.dia.es** es **Supermercado online | ¡Recibe tu compra hoy mismo! | Día**.
En el segundo escenario se comprueba si hay 5 articulos ccuando se busca la palabra ACUAREL.
En el tercer escenario se comprueba si se añade correcramente el producto al carrito

- **steps.py**

En el último when he tenido que cargar la página https:/www.dia.es/cart/ en vez de darle click al carrito ya que no me dejaba interactuar con el de ninguna forma
