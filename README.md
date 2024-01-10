# IADIRA 🤖 - Inteligencia artificial detectora de infecciones respiratorias agudas.

## 🗞️ Introducción
Este proyecto es un prototipo de inteligencia artificial enfocado a la detección de neumonía mediante radiografías de tórax. Representa una herramienta valiosa en el ámbito médico, ofreciendo precisión y velocidad en el diagnóstico.

## Planteamiento del Problema 💪
En diversas partes del mundo, las bajas temperaturas pueden desencadenar infecciones respiratorias agudas como la neumonía. Las personas, a menudo, evitan <b>acudir a centros médicos</b> por temor a costos, demoras o posibles incomodidades. Este proyecto busca abordar estos problemas al proporcionar una herramienta rápida y precisa para la detección de neumonía para brindar una mejor asistencia al médico profesional, para <b>optimizar</b> los tiempos de demora y una segunda fuente en el que puede guiarse para confirmar sus diagnósticos.

## Investigación Propuesta 🔍
Durante la investigación, se comparó el tiempo y la precisión de la detección de neumonía entre médicos radiólogos y la inteligencia artificial (IA). Algunos resultados incluyen:

<ul>
  <li>⚕️ <b>Comparación de tiempo estimado en la detección de neumonía con radiografías con radiologos certificados:</b></li>
  <p>Durante la investigación, el primer objetivo de investigación fué el tiempo que una radiólogo demora en detectar este tipo de patologías, y cuánto tiempo demora en hacerlo una IA, y los resultados fueron los siguientes:<p>
  <table>
    <tr>
      <td>Entorno de prueba</td>
      <td>Médico radiólogo</td>
      <td>Inteligencia Artificial</td>
      <td>Resultado comparativo</td>
    </tr>
    <tr>
      <td>Clínica privada</td>
      <td>1,5 horas</td>
      <td>30 segundos</td>
      <td>La IA es más rápida</td>
    </tr>
    <tr>
      <td>Centro de seguros</td>
      <td>15 minutos</td>
      <td>30 segundos</td>
      <td>La IA es más rápida</td>
    </tr>
    <tr>
      <td>Entrevista de Técnico Radiólogo</td>
      <td>1 hora</td>
      <td>30 egundos</td>
      <td>La IA es más rápida</td>
    </tr>
  </table>
  <li><b>🥇 Comparación de precisión en el momento del análisis en radiografías:</b></li>
  <p>Durante la investigación, una de las mayores prioridades es aumentar el nivel de precisión en la IA, para así tener un alto grado de confiabilidad, para lo cual, se obtuvo los siguientes resultados:<p>
  <table>
    <tr>
      <td>Etapa del proyecto</td>
      <td>Médico radiólogo</td>
      <td>Inteligencia Artificial</td>
      <td>Resultado comparativo</td>
    </tr>
    <tr>
      <td>1ra Etapa</td>
      <td>99,70% de confiabilidad</td>
      <td>68% de confiabilidad</td>
      <td>El médico radiologo es más preciso</td>
    </tr>
    <tr>
      <td>2da Etapa</td>
      <td>99,70% de confiabilidad</td>
      <td>88% de confiabilidad</td>
      <td>El médico radiologo es más preciso</td>
    </tr>
    <tr>
      <td>3ra Etapa</td>
      <td>99,70% de confiabilidad</td>
      <td>94% de confiabilidad</td>
      <td>El médico radiologo es más preciso</td>
    </tr>
  </table>
  <li><b>✅ Estudio de resultados en entornos reales con radiografías reales:</b></li>
  <p>Gracias a la ayuda de una clínica privada, nos proporcionaron 5 radiografías de torax, 2 con <b>NEUMONÍA</b> y 3 <b>SIN NEUMONÍA</b>, por lo que, logramos obtener los resultados:</p>
  <ul>
    <li>Comparación de resultados de predicciones de la IA con radiografías de tórax con la IA en su primer etapa:</li>
    <table>
      <tr>
        <td>N° de Paciente</td>
        <td>Diagnóstico médico</td>
        <td>Predicción de la IA</td>
        <td>Resultado comparativo</td>
      </tr>
      <tr>
        <td>1</td>
        <td>No tiene Neumonía</td>
        <td>Si tiene neumonía</td>
        <td>Fallido</td>
      </tr>
      <tr>
        <td>2</td>
        <td>No tiene Neumonía</td>
        <td>Si tiene neumonía</td>
        <td>Fallido</td>
      </tr>
      <tr>
        <td>3</td>
        <td>Si tiene Neumonía</td>
        <td>Si tiene neumonía</td>
        <td>Acertado</td>
      </tr>
      <tr>
        <td>4</td>
        <td>Si tiene Neumonía</td>
        <td>Si tiene neumonía</td>
        <td>Acertado</td>
      </tr>
      <tr>
        <td>5</td>
        <td>No tiene Neumonía</td>
        <td>Si tiene neumonía</td>
        <td>Fallido</td>
      </tr>
    </table>
</ul>

## 🔨 Estructura de la IA
Para llevar a cabo el entrenamiento de este proyecto, usamos <b>REDES NEURONALES CONVOLUCIONALES</b>, que nos permite usar diferentes tipos de filtros en imágenes para encontrar características en los datos.
    <table>
      <tr>
        <td>N° de capa</td>
        <td>Tipo de capa</td>
        <td>Función de la capa</td>
        <td>N° de unidades</td>
      </tr>
      <tr>
        <td>1</td>
        <td>Convolución</td>
        <td>Usa diferentes filtros para encontrar características</td>
        <td>32 mapas</td>
      </tr>
      <tr>
        <td>2</td>
        <td>MaxPooling</td>
        <td>Saca un valor máximo en una matriz de 2x2</td>
        <td>1 vez</td>
      </tr>
      <tr>
        <td>3</td>
        <td>Convolución</td>
        <td>Usa diferentes filtros para encontrar características</td>
        <td>64 mapas</td>
      </tr>
      <tr>
        <td>4</td>
        <td>MaxPooling</td>
        <td>Saca un valor máximo en una matriz de 2x2</td>
        <td>1 vez</td>
      </tr>
      <tr>
        <td>5</td>
        <td>Convolución</td>
        <td>Usa diferentes filtros para encontrar características</td>
        <td>128 mapas</td>
      </tr>
      <tr>
        <td>6</td>
        <td>MaxPooling</td>
        <td>Saca un valor máximo en una matriz de 2x2</td>
        <td>1 vez</td>
      </tr>
      <tr>
        <td>7</td>
        <td>Dropout</td>
        <td>Se usa solo un porcentaje de cantidad de neuronas existentes</td>
        <td>50%</td>
      </tr>
      <tr>
        <td>8</td>
        <td>Flatten</td>
        <td>Se realiza un aplanamiento de los datos luego de la convolución</td>
        <td>1 vez</td>
      </tr>
      <tr>
        <td>9</td>
        <td>Densa</td>
        <td>La parte principal que la IA para realizar el cálculo con la función de activación Relu</td>
        <td>64 neuronas</td>
      </tr>
      <tr>
        <td>10</td>
        <td>Densa</td>
        <td>La parte principal que la IA para realizar el cálculo con la función de activación Relu</td>
        <td>128 neuronas</td>
      </tr>
      <tr>
        <td>11</td>
        <td>Densa</td>
        <td>La parte principal que la IA para realizar el cálculo con la función de activación Relu</td>
        <td>64 neuronas</td>
      </tr>
      <tr>
        <td>12</td>
        <td>Densa</td>
        <td>La parte principal que la IA para realizar el cálculo con la función de activación Sigmoidal</td>
        <td>1 neurona</td>
      </tr>
    </table>

## 📓 Fuente de radiografías para el análisis
Para elaborar el proyecto, he entrenado a la IA usando un set de datos de la plataforma <a href="https://kaggle.com/">Kaggle</a> que me permitió tener a mi disposición una gran cantidad de <b>radiografías para el análisis</b> y segmentación de datos importantes.

## Conceptos a tener en cuenta ⚠️
Durante el desarrollo del proyecto, se tuvo la idea de que, este proyecto es puramente experimental, y que, de ninguna manera se podría <b>reemplazar</b> el puesto de un médico certificado y con experiencia, ya que, esta IA tiende a fallar aveces, y, a pesar de que su precisión puede ser aumentada a más de un 99.3%, no garantiza los mejores resultados con lujos de datalle, por lo que, se recomienda usarlo <b>como un asistente o una herramienta secundaria.</b>

## Requisitos para usarla 🔨
Durante su entrenamiento, el modelo fué entrenado con las capas indicadas anteriormente usando una GPU de Google (Tesla T4) por medio de <a href="https://colab.research.google.com">Google Colab</a>, pero el modelo puede ser ejecutado en una máquina cuya memoria RAM sea mayor a la de 4 GB, y una CPU estable.

## :handshake: Agradecimientos
Quiero dar las gracias en especial a mi amigo <b>Andre Rafael Apaza Chura</b> por apoyarme a desarrollar el proyecto, a la clínica <b>Monte Sinaí</b>, <i>Juliaca</i> por brindarme las radiografías físicas sin ánimos de lucro para llevar a cabo mi investigación, a la clínica <b>Americana</b>, <i>Juliaca</i> por darme asistencia en el análisis de las placas radiográficas, y a la clínica del <b>Dr. Willy Pari</b> especializada en el diagnóstico por imágenes, por darnos asistencia en el análisis de las placas radiográficas.