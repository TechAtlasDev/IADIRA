<h1>🤖 IADIRA</h1><br>


<h2>Introducción</h2>
<p>Este es un prototipo de una inteligencia artificial, que radica en la detección de neumonía usando radiografías de torax, lo cual representa ser una herramienta con muchas ventajas en el ámbito médico para una detección con mucha calidad de precisión, pero tambien con mucha velocidad.<p>

<h2>Planteamiento del problema</h2>
<p>Uno de los mayores problemas en este tipo de situación, es que en diferentes partes del mundo, las muy bajas temperaturas afectan de manera muy peligrosa a las personas, algo que puede ser causante de infecciones respiratorias agudas, como la neumonía, por lo que, en cadena de ello, las personas con bajos recursos, optan por automedicarse, y tomar la decisión de no ir a algún centro médico para no gastar recursos económicos, el temor de demorar demasiado tiempo para la detección de estas patologías, o la suposición de que se sentirá un gran dolor al momento de detectar síntomas de infecciones respiratorias agudas y adquirir un mal tratamiento.</p>

<h1>Investigación propuesta</h1>
<p>Durante la elaboración del proyecto, estuve investigando sobre la importancia del proyecto, por lo que, llegué a recopilar los siguientes datos:<p>
<ul>
  <li>Comparación de tiempo estimado en la detección de neumonía con radiografías con radiologos certificados:</li>
  <p>Durante la investigación, el primer objetivo de investigación fué el tiempo que una radiólogo demora en detectar este tipo de patologías, y cuánto tiempo demora en hacerlo una IA, y los resultados fueron los siguientes:<p>
  <table>
    <tr>
      <td>Sujeto de prueba</td>
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
  <li>Comparación de precisión en el momento del análisis en radiografías:</li>
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
  <li>Estudio de resultados en entornos reales con radiografías reales:</li>
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
<h2>Estructura de la IA</h2>
  <p>Para llevar a cabo el entrenamiento de este proyecto, usamos <b>REDES NEURONALES CONVOLUCIONALES</b>, que nos permite usar diferentes tipos de filtros en imágenes para encontrar características en los datos.</p>
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

<h2>Fuente de radiografías para el análisis</h2>
<p>Para elaborar el proyecto, he entrenado a la IA usando un set de datos de la plataforma <a href="https://kaggle.com/">Kaggle</a> que me permitió tener a mi disposición una gran cantidad de radiografías para el análisis y segmentación de datos importantes.</p>

<h2>Conceptos a tener en cuenta</h2>
<p>Durante el desarrollo del proyecto, se tuvo la preliminar idea de que, este proyecto será enteramente experimental, y que de ninguna manera se podría reemplazar el puesto de un médico certificado y con experiencia, ya que, esta IA tiende a aveces fallar, y, a pesar de que su precisión puede ser aumentada a más de un 99.3%, no garantiza los mejores resultados con lujos de datalle, por lo que, se recomienda usarlo como un asistente o una herramienta secundaria.</p>

<h2>Requisitos para usarla</h2>
<p>Durante su entrenamiento, el modelo fué entrenado con las capas indicadas anteriormente usando una GPU de Google (Tesla T4) por medio de <a href="https://colab.research.google.com">Google Colab</a>, pero el modelo puede ser ejecutado en una máquina cuya memoria RAM sea mayor a la de 4 GB, y una CPU estable.</p>

<h2>Agradecimientos</h2>
<p>Quiero dar las gracias a los médicos radiólogos que apoyaron al análisis del proyecto, y tambien a mi anterior equipo <i>Valletta</i> por darme la motivación de cada vez ser mejor.</p>
