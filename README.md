# Mower
👩🏻‍💻 Paula Terleira                                                          
paulaterleira@gmail.com
---
## DESCRIPCIÓN
El siguiente proyecto resuelve el problema propuesto, Mower, el cúal consiste en simular el movimiento de robots de limpieza autónomos en una fábrica, representada por un área rectangular. Se parte de una información dada respecto a posiciones y movimientos a realizar por los robots, devolviendo la posición final de estos mismos una vez realizadas las instrucciones indicadas.
## TECNOLOGÍAS EMPLEADAS
- Python con el uso de la librería PyTest para la realización de pruebas.
## ESTRUCTURA DEL PROYECTO
- input.txt -> Fichero con los datos de entrada a procesar. Dimensión del tablero, posiciones de los robots e instrucciones a seguir por los mismos.
- output.txt -> Fichero donde se mostrarán los resultados finales, la posición y orientación de cada uno de los robots.
- main.py -> Script encargado de la lógica principal de la aplicación, obteniendo los datos del fichero de entrada (input.txt) y encargándose del procesamiento de cada uno de los robots, comunicandose adecuadamente con la clase y método correspondiente.
- robot.py -> Script encargado de definir la clase Robot, declarando las orientaciones posibles de los mismos, así como las funciones a realizar: *spin_left*, *spin_right*, *move*, *process_instructions*
- test_robots.py -> Script encargado de llevar a cabo las pruebas especificadas empleando PyTest.
- README.md -> explicación del proyecto, estructura y toma de decisiones durante su realización.
## EJECUCIÓN DEL PROGRAMA
- Requisitos previos:
  - Python
  - PyTest
