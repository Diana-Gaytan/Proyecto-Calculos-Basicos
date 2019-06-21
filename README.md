# Proyecto-Calculos-Basicos
### Cálculo de elementos de trabajo de topografía básica enfocada en planimetría de predios rurales y urbanos a partir de Excel
#### Azimut y coordenadas
###### Facultad de Ingeniería Civil, Carretera Coquimatlán Kilómetro 9, Coquimatlán 28,400, Coquimatlán, Colima, dgaytan0@ucol.mx, mvazquez15@ucol.mx, ricardojavier_montes@ucol.mx 

**Resumen**
Elaboración de un programa en Python para el cálculo de elementos de un trabajo de topografía básica como lo son azimut, las distancias y la representación gráfica de una poligonal; partiendo de un documento de Excel (csv) que contiene las coordenadas; con el fin de facilitar la obtención de los da-tos mencionados anteriormente, mostrando en distintos puntos texto donde se explica qué se hizo para cada ocasión/punto: Resumen, desarrollo experimental, donde se explica con detalles e imágenes el procedimiento y desarrollo, manejo de datos, análisis de resultados y conclusiones generales, además de las fuentes consultadas para la creación total del contenido de este texto y el proyecto. 
Palabras clave: Topografía básica. Azimut.	 Coordenadas. Excel.

 
**Abstract**

The elaboration of a Python’s program for the calculation of elements of a basic topography activity such the azimuth, distances and the graphic representation of the polygon based of an Excel document with the coordinates. In which it will be easy to obtain the data mentioned above, showing through a structured document the next points: summary, experimental development, where the process development are explained in detail by images, data handing, analy-sis of the results and general conclusions, further-more, the information sources are added too.
Keywords: Basic topography. Azimuth. Coordinates. Excel.




**1. 	Introducción**

Topografía: Ciencia que estudia el conjunto de principios y procedimientos para la representación gráfica de la superficie terrestre, con sus formas y detalles.
El proyecto está pensado principalmente para las personas que necesitan hacer este tipo de cálculos grandes en poco tiempo, pues, normalmente, el cálculo para detalles de predios rurales y urbanos de manera manual, llega a ser muy extenso y agotador, lo que hace que se necesiten varias personas para tratar de agilizar la tarea un poco, lo que probablemente genere gastos en la contratación de personal especializado en la tarea y un horario de entrega o tiempo específico. Con el cálculo automático del proyecto, se pueden obtener muchos de estos datos de manera sencilla y rápida, pues al ser tan eficaz el uso de fórmulas, facilita el trabajo de muchas horas en algunos minutos ingresan-do los datos que se tengan para tener como resultado los datos que se requieran.
Python: Programa en código el cual nos ayuda en la automatización de muchos sistemas que puedan ser complicados manualmente, (como se mencionó en el párrafo anterior), utiliza líneas de código para sus sistemas o trabajos “internos”, como diccionarios, tuplas, listas, etc. de manera en la que se puede hacer un código o comando para el cálculo de datos necesarios, se puede facilitar la tarea aún más para todos.
El uso de Python puede ser algo complicado, pues abarca muchas áreas de conocimiento, como las matemáticas y el inglés; ya que es necesario programar en el idioma inglés y de manera ordenada, pues si tenemos mal una fórmula o cálculo, nuestro código puede estropearse.
Normalmente, para este tipo de trabajos es necesario el orden en todo momento, pues para introducir nuestro código se necesita ingresar una línea base donde iniciaremos e iremos avanzando hasta el punto que necesitemos (en este caso, finalizar en la obtención total de da-tos). 
El orden puede llegar a ser muy extenso, pero siempre se llega a un fin común: el resultado total y la finalización de los datos requeridos.

**2. 	Desarrollo Experimental**

El uso de las librerías en Python facilita el traba-jo, por eso usamos openpyxl y mathematics . Para iniciar con el proyecto, se comenzó analizando ideas que se tenían acerca de un buen proyecto. Al final, se decidió hacer una especie de “hoja de cálculos” en Excel de topografía básica, la cual calcularía azimut, distancias entre coordenadas y perímetro. 
Para empezar, tuvimos la idea de hacer un código distinto a nuestra finalización, pues teníamos una idea distinta de lo que queríamos hacer. El programa funcionaba correctamente, pero no tenía las funciones “correctas”, pues el cálculo de “N” número de lados no funcionaba de manera adecuada, ya que calculaba única-mente polígonos con 4 lados, pero el usuario debía introducir manualmente la mayoría de los datos que el programa pedía. Además de calcular el azimut una vez se ingresaban los datos, también calculaba la distancia, así que, hasta este punto, el código funcionaba muy bien pero no era lo que nosotros buscábamos como resultados. Si hubiésemos querido calcular el azimut y distancia para polígonos de 4 lados, con eso, habríamos terminado.
 
 
   ![PalabrasdelTextoAlternativo](https://raw.githubusercontent.com/Diana-Gaytan/Proyecto-Calculos-Basicos/master/1%20Azimut.png)

                                          Figura 1. Código para obtener el azimut
                                   
         En la figura anterior se muestra la fórmula adaptada al lenguaje Python y con las variables del programa.





![PalabrasdelTextoAlternativo](https://raw.githubusercontent.com/Diana-Gaytan/Proyecto-Calculos-Basicos/master/2%20Distancia.png)

                                        Figura 2. Código inicial del programa
                                        
Se intentó basarse en conocimientos que habían otorgado los trabajos anteriores a esta entrega, los cuales sirvieron de mucho y fueron de gran ayuda en su mayoría. 
Para comenzar con los cálculos se necesita un archivo Excel en el cual estarán los datos acomodados en distintas columnas, las cuales el usuario editará a su gusto para que posteriormente el archivo de Python haga los cálculos automáticamente.
Comenzamos con el cálculo de distancias entre coordenadas y azimut, los cuales el programa toma de la hoja de cálculos de Excel de manera automática, escribiendo, por ejemplo “Coordenada X1=…, Coordenada Y1=…, y hasta terminar de agregar las coordenadas, muestra la distancia entre las mismas y, para finalizar, el azimut. Para el cálculo del perímetro, el programa va a dar el azimut automáticamente para después asignar una variable a cada distancia para posteriormente sumarlas, dando como resultado el perímetro del polígono realizado.





![PalabrasdelTextoAlternativo](https://raw.githubusercontent.com/Diana-Gaytan/Proyecto-Calculos-Basicos/master/3%20Distancia.png)

                                       Figura 3 Códigos para cálculos del programa
                          
**3.- Manejo de Datos**

El programa maneja datos geográficos (coordenadas en x y y) que se encuentran dentro de archivos csv organizado en 2 columnas, una con el nombre “X” y la otra “Y” (como se muestra en el archivo csv "Caso_real", el cual contiene datos de un levantamiento real realizado por los alumnos de la Facultad de Ineniería Civil de la carrera Ingeniero Topógrafo Geomático en la comunidad "El Poblado", Coquimatlán Colima"). Dichos datos son leídos por el programa automáticamente; primero, el programa te pregunta cómo se llama tu archivo para poder abrirlo, posteriormente se le tiene que insertar el número de puntos que tiene el archivo en csv, para después tomar la información escrita dentro de estos y así calcular lo que se le pide/necesario mediante el uso de las fórmulas ya presentadas en el apartado de Desarrollo Experimental. En este punto, los datos leídos por el programa pasan a ser numéricos para poder utilizarlos en las ecuaciones.
Los sistemas operativos donde el programa trabaja son los derivados de Windows, pues bajo este sistema operativo fue que trabajamos en su totalidad para la creación del código y no hemos intentado hacerlo funcionar en otras “plataformas” o de otras maneras. 
Los datos manejados en el programa son de especial interés para ingenieros topógrafos geomáticos, civiles, arquitectos o cualquier otra carrera relacionada con la topografía debido a que se obtienen resultados eficientes en poco tiempo.

**4. Resultados**
Anteriormente se había hecho un “anticipo” de lo que se esperaba obtener con el final de nuestro proyecto y, para nuestro beneficio, tuvimos éxito en dichos resultados; nuestro programa cumple con las funciones de las que se habla en el inicio del escrito, el usuario sólo debe introducir sus datos en un archivo csv, donde, por orden, estarán el columnas de datos comenzando por la columna X y siguiendo, la columna Y para que nuestro programa le entregue el polígono con N número de lados dibujado en un plano especial, y que, además de todo esto, imprime las coordenadas y distancias entre estos, generando, como un extra, el azimut.
Las siguientes imágenes harán referencia a un caso topográfico real en el cual fue aplicado el programa. Primero se muestra cómo deben insertarse los datos en el archivo csv.







![PalabrasdelTextoAlternativo](https://raw.githubusercontent.com/Diana-Gaytan/Proyecto-Calculos-Basicos/master/4%20Coordenadas.png)


                                           Figura 4 Estructura del archivo csv.














![PalabrasdelTextoAlternativo](https://raw.githubusercontent.com/Diana-Gaytan/Proyecto-Calculos-Basicos/master/5%20L%C3%ADenas.png)

                                             Figura 5 Primera parte del código.
                                     
En esta parte del código se llama a las librerías correspondientes, las columnas se transforman en listas, se pregunta cómo se llama el archivo y cuántos datos tiene.








![PalabrasdelTextoAlternativo](https://raw.githubusercontent.com/Diana-Gaytan/Proyecto-Calculos-Basicos/master/6%20Bandera.png)
 
                                             Figura 6 Segunda parte del código.
                                        
En la imagen anterior se observa la última parte del código; en la que se termina el ciclo bandera, el cual se asegura de que el número de datos insertados manualmente por el usuario sea igual a los contenidos en el archivo. Si el número de datos es correcto se efectúan las operaciones para cada fila y columna y se arrojan los resultados.











![PalabrasdelTextoAlternativo](https://github.com/Diana-Gaytan/Proyecto-Calculos-Basicos/blob/master/7%20Datos.png)

                                              Figura 7 Programa corrido.
                   En la imagen anterior se observa cómo se arrojan los resultados en el Python Shell.


![PalabrasdelTextoAlternativo](https://raw.githubusercontent.com/Diana-Gaytan/Proyecto-Calculos-Basicos/master/8%20Levantamiento.png)

                                             Figura 8 Gráfica del polígono
                                                 
La figura 8 muestra cómo es el polígono real según las coordenadas del archivo csv.
Vimos este proyecto como un trabajo sencillo para nuestra materia, el cual nos facilitaría un poco este tipo de trabajos, pero, viendo el resultado final, pareciera como si el trabajo hiciera todo por ti, pues es capaz de imprimirte hasta el polígono en un plano. En caso de que no puedas adquirir este plano de tu polígono, puedes darte una idea de cómo es, ya que los datos que agregas en el proyecto son reales, haciendo que su facilidad de uso para cualquier usuario sea altísima, facilitando por mucho todo trabajo relacionado con esto. 
Los datos adquiridos en el transcurso del programa fueron variados, desde funciones que no conocíamos hasta funciones sencillas que habíamos visto en trabajos o entregas anteriores. Si bien, todas estas facilitaron por mucho la creación del código, es cierto que recibimos ayuda de otros usuarios, haciendo que nuestra adquisición de conocimiento para este o futuros trabajos aumentara. 
El manejo de datos es algo sencillo, ya que en el trabajo se explica detalladamente los pasos a seguir para una correcta obtención de datos y el manejo de los mismos, además de que en el mismo proyecto se explica lo anteriormente mencionado. 
Para finalizar, estamos de acuerdo y satisfechos con los resultados que nuestro programa arroja, además de los conocimientos adquiridos a lo largo del desarrollo del mismo.

5.	**Conclusiones**

El programa se ejecutó de la mejor manera posible, el código del mismo permitió que fuera fácil de comprender para cualquier usuario, así como la organización de los datos arrojados, los cuales fueron comprobados con procedimientos manuales asegurando su precisión y logrando el objetivo deseado.
Durante el desarrollo del código tuvimos diversos inconvenientes y dudas, las cuales fueron investigadas y comentadas entre los integrantes del equipo, al igual que pidiendo apoyo al profesor de la materia, compañeros de semestres avanzados y al encargado del módulo de cómputo.
El obstáculo más difícil fue encontrar la manera de que el programa funcionara para n número de datos, ya que al inicio sólo lo hacía con 4 coordenadas.
Sin embargo, como ya se había mencionado, dichos obstáculos se superaron.
Finalmente, pensamos que la topografía es de gran utilidad cuando se requiere conocer las formas del terreno, pero utiliza un sinfín de cálculos, por lo tanto, es necesaria la ayuda de la programación para realizarlos y facilitar el trabajo a los ingenieros topógrafos geomáticos, asegurándonos de que los resultados sean correctos debido a la precisión del programa y dejando la satisfacción de un trabajo bien hecho



6.- **Bibliografía**
Downey, Elkner & Meyers, How to think like a computer scientist, 2002, Green Tea Press, Wellesley, MA, USA, http://www.greenteapress.com/thinkpython/thinkCSpy/thinkCSpy.pdf
Python programming, an introduction to computer science, John M. Zelle, EE.UU., Beedle and Associ-ates Incorporated, 2010, Biblioteca de Ciencias Aplicadas

Zamarripa, M. (2016). Apuntes de elementos de topo-grafía. Recuperado de: 
https://www.um.es/documents/378246/2964900/Normas+APA+Sexta+Edici%C3%B3n.pdf/27f8511d-95b6-4096-8d3e-f8492f61c6dc
