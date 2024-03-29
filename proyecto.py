# Importando los modulos para el servidor web
import os # Modulo para el uso del sistema operativo
import flask # Modulo principal para el manejo de servidores web
from flask import render_template, request # Librerías dentro de Flask para procesar plantillas HTML y solicitudes hacia el servidor
from werkzeug.utils import secure_filename # Conjunto de herramientas seguras
# Importando el modulo para cargar la red neuronal entrenada
from keras.models import load_model
# Importando el modulo que nos permite cargar y editar imágenes
import numpy as np # Uso de arreglos
import cv2

# Creando el entorno
# Usamos __name__ cuando se ejecuta el documento desde acá, no sin importar librerias
entorno = flask.Flask(__name__, template_folder="plantillas_web")
# Definimos la ruta del folder
UPLOAD_FOLDER = 'static'
# Configuracion del entorno estático
entorno.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Cargando el modelo
modelo = load_model("modelo.h5")        

# Funcion para detectar neumonía usando el modelo entrenado
def detectar(modelo1, ruta_imagen):
    imagen_leida = cv2.imread(ruta_imagen, cv2.IMREAD_GRAYSCALE)
    imagen_redimensionada = cv2.resize(imagen_leida, (250, 250))
    imagen_en_matriz = np.array(imagen_redimensionada).reshape(-1, 250, 250, 1)
    imagen_en_matriz = imagen_en_matriz / 255.
    imagen_en_matriz = np.array(imagen_en_matriz)

    prediccion = modelo1.predict([imagen_en_matriz])
    if prediccion[0][0]>0.5:
      return "Positivo" # Tiene Neumonía
    else: 
      return "Negativo" # No tiene Neumonía

# Creando la ruta del index
@entorno.route("/", methods=['GET','POST'])

def index(nombre_imagen="person1_virus_8.jpeg", pagina_act="index.html"):
    if request.method == 'POST':
        imagen_recibida = request.files['imagen1'] 
        nombre_imagen = secure_filename(imagen_recibida.filename)
        imagen_recibida.save(os.path.join(entorno.config['UPLOAD_FOLDER'], nombre_imagen))
        resultado = detectar(modelo, os.path.join(entorno.config['UPLOAD_FOLDER'], nombre_imagen))
        with open('imagen_analizar.txt', 'w') as f:
                f.write(nombre_imagen)
                return render_template("resultados.html", resultado=resultado, nombre_imagen=nombre_imagen)
    else:
        with open('imagen_analizar.txt', 'r') as f:
            nombre_imagen = f.read()
        return render_template("index.html", nombre_imagen=nombre_imagen, pagina_act=pagina_act)

# Creando la ruta para le saludo al usuario
@entorno.route("/resultados")
def resultado(nombre_imagen="person1_virus_8.jpeg"):
    with open('imagen_analizar.txt', 'r') as f:
        nombre_imagen = f.read()
        resultado = "Negativo"
        return render_template("resultados.html", resultado=resultado, nombre_imagen=nombre_imagen)

# Mostrando el entorno creado
if __name__ == "__main__":
    entorno.run(debug=True, port=8003, host="0.0.0.0")
