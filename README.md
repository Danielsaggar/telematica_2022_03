# telematica_2022_03
sistema de gestión para el mundial CATAR 2022

Integrantes:
Guete Marlon
Peñaloza Yesid
Vergara Alejandra

Requisitos:
Los requerimientos son los siguientes:

-	La interfaz de usuario deberá ser un browser.
-	Toda la información debe estar registrada en un motor de base de datos.
-	Todos los módulos debe tener acceso a una única base de datos.

El sistema se compone de los siguientes módulos:

-	Módulo de Configuración. Debe permitir el ingreso de los siguientes datos de:
o	Datos del Equipos de Futbol
	Nombre del Equipo
	Jugadores (Nombre, apellido, Número),
	Entrenador.
	Logo
o	Árbitros (Al menos 4 árbitros)
	Nombre.
	Procedencia.
o	Estadios. (Al menos 4 estadios)
	Nombre.
	Capacidad.
	Ubicación
o	Deben haber al menos 2 grupos con 4 equipos cada uno.
o	Modificación/Eliminación de datos.  Debe permitir modificar los datos ingresados.
	Buscar por algún parámetro.  En caso que hayan varias coincidencias se debe mostrar en forma de listado.
-	Programación. Permite crear los partidos.
o	Crear programación.
	Asociar un estadio y partido con una fecha y hora determinada. Y asignarle unos árbitros que no sean de la procedencia de los equipos.
o	Modificar programación
-	Módulo de partidos on-line.  En una página WEB una persona o narrador podrá ingresar los datos del partido minuto a minuto y todos sus eventos (solo para partidos programados en fecha y hora).  Solo debe estar disponible cuando el partido comienza.
o	Información minuto a minuto. Breve descripción de texto indicando siempre el tiempo de juego en que ocurre.
o	Puede incluir eventos especiales como :
	Tarjetas  amarillas, rojas,
	Tiros de esquila,
	Goles,
	Fin de juego.
o	Llevar la estadística de:
	Tiros al arco, de esquina.
	Goles
	Fueras de juego, etc.
o	Cuando se termina el tiempo del partido (otro evento), el marcador debe registrarse como definitivo.
-	Módulo de Visualización WEB.  Se debe mostrar:
o	Una página donde están todos los partidos programados del día (alguna señal para partidos activos).
o	Los partidos culminados deben mostrar el resultado final y un enlace para obtener la información del minuto a  minuto y las estadísticas finales. (en otra página)
o	Los partidos que no han comenzado deben mostrar un mensaje de “Próximamente”.
o	Cuando el partido ya comenzó, se debe entrar a la página de minuto a minuto respectivo, se deben mostrar las estadísticas parciales.
o	Visualización de La tabla de posiciones ordenada de mejor a peor para cada uno de los grupos y con los resultados actualizados.
-	Módulo Visualización PC (Opcional- Bono adicional de 1.5 solo si el resto está completo).  Se debe crear un programa residente en el PC (o Enviarlo al Whatsapp), el cual vaya enviando la información del minuto a minuto y tenga siempre el marcador. 



