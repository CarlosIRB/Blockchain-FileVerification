File Hashing Service
Descripción
Este repositorio contiene una implementación sencilla de un servicio de hashing de archivos utilizando Python (Flask) y una interfaz web básica. El propósito principal de este proyecto es permitir la carga de archivos de cualquier tipo (como PDF, ZIP, DOCX, CSV, etc.) y calcular sus hashes SHA-256 para verificar su integridad. Los hashes generados se pueden utilizar en aplicaciones como contratos inteligentes en blockchain para garantizar que los archivos no hayan sido modificados.

Características
- Soporte para múltiples tipos de archivos: El enfoque de utilizar la estructura binaria de los archivos para calcular el hash permite ampliar el rango de tipos de archivos que se pueden procesar, ya que todos los archivos, independientemente de su formato (PDF, DOCX, CSV, ZIP, etc.), pueden ser tratados como secuencias de bytes. Al leer el contenido del archivo directamente como datos binarios y aplicar el algoritmo de hashing sobre estos datos, se asegura que el cálculo del hash sea independiente del tipo de archivo. Esto garantiza que cualquier archivo, sin importar su extensión o contenido, pueda ser procesado uniformemente, permitiendo así la validación de integridad para una amplia variedad de archivos.
- Buffer dinámico: La implementación ajusta dinámicamente el tamaño del buffer utilizado para leer los archivos en función de su tamaño, optimizando el proceso de hashing.
- Interfaz web sencilla: Se proporciona una página HTML con Bootstrap que permite la carga de archivos y la interacción directa con el servicio de hashing.

Limitaciones del Hashing
- Metadatos Volátiles: Algunos archivos contienen metadatos que cambian con cada edición o incluso al ser simplemente abiertos, lo que puede causar que el hash cambie aunque el contenido esencial del archivo no haya sido modificado. Esto es común en archivos PDF, DOCX, y otros formatos que almacenan información como la fecha de modificación.
- Desempeño con Archivos Grandes: Aunque se implementó un buffer dinámico para optimizar la lectura de archivos grandes, el cálculo del hash puede ser intensivo en recursos para archivos muy grandes, especialmente en entornos con recursos limitados.