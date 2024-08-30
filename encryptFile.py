from flask import Flask, request, jsonify
from flask_cors import CORS
import hashlib

app = Flask(__name__)
CORS(app)  # Permitir todos los CORS

def calcular_tamano_buffer(tamano_archivo):
    """Determina el tamaño del buffer en función del tamaño del archivo."""
    if tamano_archivo < 1 * 1024 * 1024:  # Menor de 1 MB
        return 4096  # 4 KB
    elif tamano_archivo < 100 * 1024 * 1024:  # Entre 1 MB y 100 MB
        return 8192  # 8 KB
    else:  # Mayor de 100 MB
        return 16384  # 16 KB

def calcular_hash(archivo):
    """Calcula el hash SHA-256 de un archivo tomando en cuenta la estructura binaria."""
    archivo.seek(0, 2)  # Mover al final del archivo para obtener el tamaño
    tamano_archivo = archivo.tell()
    archivo.seek(0)  # Volver al inicio del archivo

    buffer_size = calcular_tamano_buffer(tamano_archivo)
    
    hasher = hashlib.sha256()
    for bloque in iter(lambda: archivo.read(buffer_size), b""):
        hasher.update(bloque)
    return hasher.hexdigest()

@app.route('/upload', methods=['POST'])
def upload_file():
    archivos = request.files.getlist('files')
    resultados = {}
    for archivo in archivos:
        archivo.seek(0)
        try:
            hash_resultado = calcular_hash(archivo)
        except Exception as e:
            hash_resultado = f"Error procesando {archivo.filename}: {e}"
        resultados[archivo.filename] = hash_resultado
    return jsonify(resultados)

if __name__ == '__main__':
    
    app.run(debug=True)
