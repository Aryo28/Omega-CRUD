Toda la información incluida dentro del sistema en su versión actual, es información falsa creada con el único propósito de realizar pruebas de funcionamiento y evaluar las características del mismo.

Este proyecto fue realizado como respuesta a la necesidad del personal de Sala de Radio de Tránsito y Vialidad, de migrar su forma de trabajo en hojas de excel a una modalidad más sencilla, estructurando una Base de Datos que favorezca la integridad de la información y permita a los usuarios tener un control mas estricto y seguro de la información capturada.

Características del Sistema:

Sistema tipo CRUD implementado con el Framerowk de desarrollo web de Python, Django. En conjunto con lenguaje de etiquetas HTML, CSS y Javascript e integrando una Base de Datos SQL.

El desarrollo incluye Vistas Basadas en Clases e implementa el Modelo Vista Template propio del mismo Framework, los modelos fueron diseñados acorde a las necesidades del usuario incluyendo los campos esenciales para su llenado así como validaciones específicas para deteminados elementos de cada tabla en la Base de Datos.
Este sistema integra 7 módulos que permiten efectuar Altas y Cabmios, debido a la naturaleza del proyecto en esta versión no es necesario realizar Bajas de los registros, los cuales solamente deben inactivarse modificando su estatus en la Base de Datos.

Dentro de la interfaz del sistema cuenta con una página de inicio simple pero intuitiva para el usuario, el cual le permite acceder a cada uno de los módulos de acuerdo a sus necesidades, además de un menú desplegable para navegar entre los distintas vistas del sistema. 
La información ingresada por los usuarios es observable directamente en una vista que mediante el pluggin 'Datatable' despliega la lista de registros de la tabla en cuestión y permite buscar registros por palabras incluidas y por rango de fechas.
Cada registro permite visualizar al instante su contenido, así como realizar cambios en el mismo si así lo desea. A su vez, se incluye la opción de 'eliminar' dicho registro el cual como se mencionó anteriormente solamente modifica el estatus del mismo a 'Inactivo', de igual manera, cada registro inactivo puede volver a su estatus original si es que así se lo requiere.

