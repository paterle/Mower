# Mower
👩🏻‍💻 Paula Terleira                                                          
paulaterleira@gmail.com

---

## DESCRIPCIÓN
El siguiente proyecto resuelve el problema propuesto, Mower, el cúal consiste en simular el movimiento de robots de limpieza autónomos en una fábrica, representada por un área rectangular. El programa parte de una información dada respecto a posiciones y movimientos a realizar por los robots, devolviendo la posición final de estos mismos una vez realizadas las instrucciones indicadas.

---

## TECNOLOGÍAS EMPLEADAS
- **Python**
- **PyTest** para la realización de pruebas unitarias.
---  
## ESTRUCTURA DEL PROYECTO
- `input.txt` -> Fichero con los datos de entrada a procesar. Dimensión del tablero, posiciones de los robots e instrucciones a seguir por los mismos.
- `output.txt` -> Fichero donde se mostrarán los resultados finales, la posición y orientación de cada uno de los robots.
- `main.py` -> Script encargado de la lógica principal de la aplicación, obteniendo los datos del fichero de entrada (input.txt) y encargándose del procesamiento de cada uno de los robots, comunicándose adecuadamente con la clase y método correspondiente.
- `robot.py` -> Script encargado de definir la clase Robot, declarando las orientaciones posibles de los mismos, así como las funciones a realizar: *spin_left*, *spin_right*, *move*, *process_instructions*
- `test_robots.py` -> Script encargado de llevar a cabo las pruebas especificadas empleando PyTest.
- `README.md` -> explicación del proyecto, su estructura y las decisiones tomadas durante su realización.
--- 
## FORMATO ENTRADA Y SALIDA
### Ejemplo de `input.txt`
```
55
12 N
LMLMLMLMM
33 E
MMRMMRMRRM
```
- **Primera línea**: dimensiones del área a recorrer.
- **Siguientes líneas**: organizadas en grupos de dos líneas por robot.
  - **Primera línea del grupo**: posición inicial y orientación del robot (XY Orientación, por ejemplo 12 N)
  - **Segunda línea del grupo**: listado de movimientos a seguir por el robot formado exclusivamente por las instrucciones 'L','R' y 'M'.
### Ejemplo de `output.txt`
```
13 N
51 E
```
- Una línea por cada robot indicando su posición y orientación final (XY Orientación, por ejemplo 13 N)
--- 
## ARQUITECTURA
Se ha aplicado una arquitectura por capas, separando claramente:
- **Dominio**
  - La clase `Robot.py` encapsula la lógica de los robots incluyendo todas sus funciones relacionadas con el movimiento y orientación de los mismos.
  - Esta clase se encarga únicamente del comportamiento de los robots.
- **Entrada**
  - El procesamiento de la entrada de datos no se abstrae completamente, ya que se mantiene dentro del fichero `main.py`, sin embargo, se lleva a cabo mediante una función encargada de recoger los datos de entrada y la estructura y el contenido de los datos de entrada
- **Aplicación**
  - Se encarga del procesamiento secuencial de los robots, realiza el flujo principal de la aplicación recibiendo los datos de entrada, instanciando los robots, procesando las instrucciones y escribiendo la salida de datos.
  - Se coordinan las llamadas al dominio y la entrada de datos.
--- 
## DECISIONES TÉCNICAS
- **Clase Robot**: se ha decidido crear esta clase para encapsular la lógica relacionada con todo lo referente al robot (posición ,orientación e instrucciones) así como las condiciones para llevar a cabo estas instrucciones.
  Esta decisión facilita tres principios clave:
  - Modularidad: al separar la lógica del robot y dentro del mismo las lógicas de giro, movimiento e instrucciones.
  - Reutilización: permite instanciar y modificar robots desde cualquier parte del código.
  - Test: facilita la realización de pruebas unitarias al no depender de la entrada.
- **Entrada y validación de datos**: permite separar el código de lectura y validación de datos de la lógica principal facilitando la mantenibilidad en caso de que se modifique el tipo de entrada y la robustez a la hora de controlar errores en los datos.
- **Procesamiento de entrada**: a la hora de procesar las líneas de entrada se ha optado por no usar el método split() debido a que la estructura de datos "12 N" no contiene delimitadores entre las coordenadas x e y, por este motivo se ha optado por acceder a cada dígito por su posición.
- **Limitaciones**: la falta de delimitadores entre coordenadas limita el tamaño del área a trabajar, haciendo que no pueda ser superior a 9, ya que al pasar a dobles dígitos no habría opción a definir que números pertenecen a la coordenada x o y, debido a esa falta de delimitadores entre ellas en el formato dado como entrada. Por ello el formato de entrada debe ser como el especificado.
- **Validaciones**: se ha supuesto el formato de entrada fijo dado en las instrucciones. Llevando a cabo las validaciones oportunas para la comprobación de formato y estructura, manejando las excepciones en los casos que el fichero esté vacío o no contenga 2 líneas de datos por robot. También se han realizado validaciones a la hora de procesar las instrucciones comprobando que recibe las instrucciones aceptadas 'L', 'R' y 'M' exclusivamente.
--- 
## PRUEBAS
Se ha llevado a cabo la realización de las siguientes pruebas unitarias:
-  Prueba del impedimento de realizar movimientos fuera del área marcada.
-  Prueba de realización correcta de los movimientos según la ubicación y de igual forma con los giros.
-  Prueba del correcto procesamiento de las instrucciones de movimiento.
-  Comprobación del manejo de instrucciones inválidas.
Para la realización de las mismas se ejecuta la instrucción `pytest`
--- 
## EJECUCIÓN DEL PROGRAMA
### Requisitos previos:
  - Python.
  - PyTest.
  - Fichero de texto `input.txt` en la carpeta del proyecto.
### Ejecución del proyecto:
  - `python main.py`
### Ejecución de pruebas
  - `pytest`
