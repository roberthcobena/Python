# Notas de programadores: FAVOR IGNORAR
# -Roberth: HAY QUE AÑADIR ALGUNAS RESPUESTAS A LAS PREGUNTAS QUE EL MISMO CHATBOT HACE EN LA SECCION SEGUIR
# _____________________________________________________________________________________________________________________________________________________________
# Presentacion

print("\nUNIVERSIDAD AGRARIA DEL ECUADOR\n")
print("MATERIA: Inteligencía Artificial\n")
print("CURSO: 9SA\n")
print("PROYECTO FINAL\n")
print("DOCENTE:\n Ing. Charles Peréz\n")
print("ALUMNOS:\n Cobeña Roberth\n Miño Jordi\n")
print("REGLAS DEL CHATBOT:\n")
print(" *Escribir únicamente en idioma español\n")
print(" *Usar ? para preguntas o cuestiones\n")
print(" *Reconoce solo algunas palabra con tilde\n")
print(" *Tener paciencia, es un prototipo en crecimiento\n")
print(" *No responde a temas relacionados a las peleas\n")
print(" *No responde a preguntas específicas sobre un personaje, solo en general\n")
print(" *Conoce a todos los personajes más relevantes y conocidos que apaceren durande la saga del Torneo Universal\n")
print(" *No escribir groserias, Tenshin-bot es algo sensible\n")
# _____________________________________________________________________________________________________________________________________________________________
# Aleatorio para respuestas distintas y otras variables

import random as rd
rd.randint(0, 1000)
import time
ahora = time.strftime("%c")
# _____________________________________________________________________________________________________________________________________________________________
# Palabras almacenadas
# _____________________________________________________________________________________________________________________________________________________________

saludos = ["hola", "que más", "buenas", "que tal", "hi bro", "hola que te cuentas?", "holi :3", "holiwis", "habla pués",
           "que hay pana", "que mas mi llave", "aloja", 'saludos cordiales', 'bienvenido']

despedida = ["nos vemos" "pilas bro", "chao", "adios", "hay te ves", "sayonara", 'nos vemos', 'cuidate', 'chaito',
             'hasta luego', 'que Zeno-Sama te bendiga', 'cuidate humano', 'bye bye', "sayonara",
             "que Sheng Long guíe tu camino", "que Goku te proteja"]

articulos = ["y", "la", "las", "un", "en", "unos", "unas", "los", "lo", "ellos", "eso", "esas", "esa", "esos",
             "es"]

seguir = ["- Que tal tu dia", "- Como te sientes", "- A que te dedicas", "- Que hay de nuevo en tu vida",
          "- Comó has estado",
          "- Eres barcelonista o emelecista", "- Como te diviertes", "- Te gusta el anime",
          "- Te gustan los videojuegos",
          "- Cual es tu numero favorito", "- Cual es tu color favorito", "- Cual es tu pelicula favorita",
          "- Quien es tu artista o banda preferida",
          "- Cual es tu cancion favorita", "- Cual es tu platillo favorito", "- Amas a alguien",
          "- Que clase de musica escuchas",
          "- Cual es tu color favorito", "- Quiere preguntame algo", "- Si quieres conversar",
          "- Sabes que es Dragon Ball", "- Sabes que es un sayayin", "has escuchado sobre la serie Dragon Ball Súper"]

noentiendo = ["No sé como contestar", "No te entiendo",
              "Sal de ahí Shen Long y dime que lo trata de decirme",
              "Le preguntare a Zuno si sabe lo que tratas de decirme"]

lista_personajes = ["akira", "bulma", "trunks", "goten", "satán", "satan", "boo", "zeno", "rey", "marron", "bra",
                    "pilaf", "shu", "mai", "yamcha", "rensou", "jaco", "zuno", "milk", "chi", "chi-chi", "videl",
                    "pan", "bee", "kibito", "yurin", "chaoz", "panchy", "brief", "uranai", "enma", "tights"]

lista_universo1 = ["iwen", "awamo", "anat"]

lista_universo2 = ["heles", "sour", "peru", "brianne", "bikal", "harmira", "jimizu", "prum", "rabanra", "sanka", "roas",
                   "zarbuto", "zirloin"]

lista_universo3 = ["mosco", "capahri", "ea", "biarra", "boraleta", "katopesla", "kayo", "nigrissi", "narirama",
                   "preecho", "paparoni", "koitsukai", "pancea", "koichealeta", "koichiarator", "anilaza"]

lista_universo4 = ["quitela", "cognic", "kur", "nink", "ganos", "shousa", "shosa", "majora", "caway", "dercori",
                   "monna",
                   "shantsa", "damom", "gamisalas"]

lista_universo5 = ["arak", "cucatall", "ogma"]

lista_universo6 = ["champa", "vados", "fuwa", "hit", "cabba", "frost", "magetta", "botamo", "caulifla", "kale", "rota",
                   "saonel", "pilina", "kefla"]

lista_universo7 = ["bilss", "beerus", "whis", "shin", "anciano", "antiguo", "gohan", "goku", "vegeta", "piccolo", "17",
                   "18", "krilin", "tenshinhan", "roshi", "kamekame", "senin", "sen'nin", "freezer"]

lista_universo8 = ["liquir", "korn", "iii"]

lista_universo9 = ["sidra", "mojito", "rou", "bergamo", "lavenda", "basil", "hyssop", "cheppil", "comfrey", "hop",
                   "oregano", "sorrel", "roselle"]

lista_universo10 = ["rumoosh", "kus", "gowas", "dium", "jirasen", "lilibeu", "rubalt", "methiop", "murichim",
                    "murisarm", "napapa", "obuni", "zircol"]

lista_universo11 = ["vermud", "marcarita", "kai", "jiren", "toppo", "dispo", "casseral", "cocotte", "vuon", "kettle",
                    "tupper", "zoirei", "kunsi"]

lista_universo12 = ["geen", "martinne", "ag"]

lista_destruccion = ["iwen", "heles", "mosco", "quitela", "arak", "champa", "bilss", "beerus", "liquir", "sidra",
                     "rumoosh", "vermud", "geen"]

lista_angeles = ["awamo", "sour", "capahri", "cognic", "cucatall", "vados", "whis", "korn", "mojito", "kus",
                 "marcarita", "martinne", "sacerdote"]

lista_profesiones = ["profesor", "estudiante", "vendedor", "nada", "vago", "trabajo", "trabajar", "estudiar", "comer",
                     "dormir", "pasear", "trabajo"]

lista_colores = ["amarillo", "azul", "rojo", "verde", "blanco", "negro", "azul", "violeta", "morado", "celeste",
                 "fuccia", "naranja", "anaranjado"]

lista_numeros = ["0", "1", "2", "3", "5", "6", "7", "8", "9", "11", "13"]

lista_peliculas = ["titanic", "accion", "comedia", "acción", "romanticas", "avengers", "vengadores", "padrino", "la"]

lista_artistas = ["rock", "electronica", "rap", "cumbia", "guns", "rammstein", "metalica", "metallica", "led", "iron"]

lista_canciones = ["para", "du", "welcome", "sandman", "trooper", "walk"]

lista_alagos = ["inteligente", "sorprendente", "super", "súper", "bella", "bello", "maravilloso", "maravillosa",
                "amistoso", "amistosa"]

lista_insultos = ["tonta", "tonto", "pendejo", "pendeja", "estupido", "estupida", "imbecil", "ímbecil", "bruto",
                  "bruta", "incapaz"]

lista_gusta = ["estudiar", "dragon", "programar", "novio", "novia", "salir", "anime", "manga", "amigos", "bailar",
               "cantar", "leer", "pasear", "cine", "netflix", "jugar", "videojuegos", "chatear"]

lista_comida = ["encebollado", "bolon", "ceviche", "guatita", "pizza", "caldo", "sopa", "arroz", "seco", "estofado",
                "frito", "asado", "asada", "con"]

lista_comida2 = ["sushi", "pastel", "torta"]

# _____________________________________________________________________________________________________________________________________________________________
# Respuestas almacenadas
# _____________________________________________________________________________________________________________________________________________________________

def equipo(futbol):
    if futbol == "barcelona":
        print("- Esa es " + nombre + ", ya me caiste bien\n")
    if futbol == "emelec":
        print("- Sal de mi CHAT...¡¡¡ " + nombre + ", naaaaaa es broma, hasta yo tengo que ser tolerante\n")

def relacion(pareja):
    if pareja == "novio":
        print("- El amor es algo impropio de mi, por eso o necesito un hombre a mi lado\n")
    elif pareja == "novia":
        print("- El amor es algo impropio de mi, por eso o necesito a una mujer a mi lado\n")
    elif pareja == "problemas":
        print("- Mi unico problema es que aun no lo se todo\n")
    elif pareja == "hambre":
        print("- No puedo percibir el mundo, ni siquiera a mi mismo, por lo tanto no tengo eso...\n")
    elif pareja == "feliz":
        print("- No entiendo ningun sentimiento por lo tanto no puedo darte una repsuesta certera\n")
    elif pareja == "respuesta":
        print(
            "- Desafortunadamente aun no tengo todas las respuestas, pero tratare de contestarte lo mejor que pueda...¡¡¡\n")
    elif pareja == "mal":
        print(
            "- Me gustaria ayudar a que te sientas mejor " + nombre + ", puedes confiar en mi, cuentame porque estas asi...\n")
    elif pareja == "bien":
        print(
            "- No sabes cuanto me alegro de que estes animado " + nombre + "\n")
    else:
        print("- Se mas especifico, tengo y se algunas cosss y otras no...\n")

def sabes(personajes):  # JORDI----------------------------
    # personajes
    if personajes == "akira":
        print("- Akira Toriyama es el Mangaka creador del universo de Dragon Ball.... Cuándo sea grande quiero ser "
              "como él :D\n")
    elif personajes == "bulma":
        print("- Es la creadora del radar del dragón y esposa de Vegeta.\n")
    elif personajes == "trunks":
        print("- Es el hijo mayor de Vegeta y Bulma.\n")
    elif personajes == "goten":
        print("- Es el hijo menor de Goku y Milk.\n")
    elif personajes == "satan":
        print("- Es papá de Videl, campeón mundial de artes marciales y ''heroe de la Tierra''.\n")
    elif personajes == "satán":
        print("- Es papá de Videl, campeón mundial de artes marciales y ''heroe de la Tierra''.\n")
    elif personajes == "boo":
        print("- Es una criatura demoniaca que se hizo buena gracias a Mr. Satán.\n")
    elif personajes == "zeno":
        print("- Es el Rey de Todo, está por encima de todo y de todos, no existe nadie más fuerte que él.\n")
    elif personajes == "rey":
        print("- Es el Rey de Todo, está por encima de todo y de todos, no existe nadie más fuerte que él.\n")
    elif personajes == "marron":
        print("- Es la hija de Krilin y Nº18.\n")
    elif personajes == "bra":
        print("- Es la hija menor de Vegeta y Bulma.\n")
    elif personajes == "pilaf":
        print("- Es villano que busca las esferas del dragón, vive en casa de Bulma junto a sus secuaces Mai y Shu.\n")
    elif personajes == "shu":
        print("- Es un secuaz de pilaf, vive en casa de Bulma junto a su colega Mai y su jefe Pilaf.\n")
    elif personajes == "mai":
        print("- Es una secuaz de pilaf, vive en casa de Bulma junto a su colega Shu y su jefe Pilaf.\n")
    elif personajes == "yamch":
        print("- Es uno de los Guerreros Z. El debil XD\n")
    elif personajes == "rensou":
        print("- Es hermano de kaulifla.\n")
    elif personajes == "jaco":
        print("- Es un patrullero de las Fuerzas Galácticas, amigo de Bulma y Tights.\n")
    elif personajes == "zuno":
        print("- Es un sabio, y conoce cualquier cosa sobre el Universo 7.\n")
    elif personajes == "milk":
        print("- Es la esposa de Goku.\n")
    elif personajes == "chi":
        print("- Es la esposa de Goku.\n")
    elif personajes == "chi-chi":
        print("- Es la esposa de Goku.\n")
    elif personajes == "videl":
        print("- Es la hija Mr. Satán y esposa de Goham. Todo indica que es la terricola más fuerte de la Tierra\n")
    elif personajes == "pan":
        print("- Es la hija de Gohan y Videl, nieta de Mr. Satan, Goku y Milk.\n")
    elif personajes == "bee":
        print("- Es el perrito de Mr. Satan.\n")
    elif personajes == "kibito":
        print("- Es asistente y guardaespaldas de Kaio-Shin Shin.\n")
    elif personajes == "yurin":
        print("- Es una chica experta en hechizos que quería aprender artes marciales en la escuela de Tenshinhan.\n")
    elif personajes == "chaoz":
        print("- Es el mejor amigo de Tenshinhan.\n")
    elif personajes == "panchy":
        print("- Es la madre de Bulma, esposa del Dr. Brief.\n")
    elif personajes == "brief":
        print("- Es el hombre más inteligente de la tierra, padre Bulma y fundadore de la Corporación Cápsula.... Si él"
              " inventó las cápsulas\n")
    elif personajes == "bra":
        print("- Es la hija menor de Vegeta y Bulma.\n")
    elif personajes == "uranai":
        print("- Es una bruja XD y adivina, hermada del MAestro Roshi.\n")
    elif personajes == "enma":
        print("- Es el 'Gerente del Inframundo'.\n")
    elif personajes == "tights":
        print("- Es la hermana mayor de Bulma y amiga de Jaco.\n")
    # equipos univeros
    elif personajes == "brianne":
        print("- Es un luchador del equipo universo 2.\n")
    elif personajes == "bikal":
        print("- Es un luchador del equipo universo 2.\n")
    elif personajes == "harmira":
        print("- Es un luchador del equipo universo 2.\n")
    elif personajes == "jimizu":
        print("- Es un luchador del equipo universo 2.\n")
    elif personajes == "prum":
        print("- Es un luchador del equipo universo 2.\n")
    elif personajes == "rabanra":
        print("- Es un luchador del equipo universo 2.\n")
    elif personajes == "sanka":
        print("- Es un luchador del equipo universo 2.\n")
    elif personajes == "roas":
        print("- Es un luchador del equipo universo 2.\n")
    elif personajes == "zarbuto":
        print("- Es un luchador del equipo universo 2.\n")
    elif personajes == "zirloin":
        print("- Es un luchador del equipo universo 2.\n")
    elif personajes == "biarra":
        print("- Es un luchador del equipo universo 3.\n")
    elif personajes == "boraleta":
        print("- Es un luchador del equipo universo 3.\n")
    elif personajes == "katopesla":
        print("- Es un luchador del equipo universo 3.\n")
    elif personajes == "kayo":
        print("- Es un luchador del equipo universo 3.\n")
    elif personajes == "nigrissi":
        print("- Es un luchador del equipo universo 3.\n")
    elif personajes == "narirama":
        print("- Es un luchador del equipo universo 3.\n")
    elif personajes == "preecho":
        print("- Es un luchador del equipo universo 3.\n")
    elif personajes == "paparoni":
        print("- Es un luchador del equipo universo 3.\n")
    elif personajes == "koitsukai":
        print("- Es un luchador del equipo universo 3.\n")
    elif personajes == "pancea":
        print("- Es un luchador del equipo universo 3.\n")
    elif personajes == "koichealeta":
        print("- Es un luchador del equipo universo 3.\n")
    elif personajes == "koichiarator":
        print("- Es un luchador del equipo universo 3.\n")
    elif personajes == "anilaza":
        print("- Es un luchador del equipo universo 3.\n")
    elif personajes == "nink":
        print("- Es un luchador del equipo universo 4.\n")
    elif personajes == "ganos":
        print("- Es un luchador del equipo universo 4.\n")
    elif personajes == "shousa":
        print("- Es un luchador del equipo universo 4.\n")
    elif personajes == "shosa":
        print("- Es un luchador del equipo universo 4.\n")
    elif personajes == "majora":
        print("- Es un luchador del equipo universo 4.\n")
    elif personajes == "caway":
        print("- Es un luchador del equipo universo 4.\n")
    elif personajes == "dercori":
        print("- Es un luchador del equipo universo 4.\n")
    elif personajes == "monna":
        print("- Es un luchador del equipo universo 4.\n")
    elif personajes == "shantsa":
        print("- Es un luchador del equipo universo 4.\n")
    elif personajes == "damom":
        print("- Es un luchador del equipo universo 4.\n")
    elif personajes == "gamisalas":
        print("- Es un luchador del equipo universo 4.\n")
    elif personajes == "hit":
        print("- Es un asesiono que puede dar saltos en el tiempo!!! y pertenece al equipo universo 6.\n")
    elif personajes == "cabba":
        print("- Es un saiyanyin del equipo universo 6.\n")
    elif personajes == "frost":
        print("- Es un farsante del equipo universo 6.\n")
    elif personajes == "magetta":
        print("- Es un bebé llorón de lava del equipo universo 6.\n")
    elif personajes == "botamo":
        print("- Es un oso medio raro que desvia los golpes que recibe a otra dimensión del equipo universo 6.\n")
    elif personajes == "caulifla":
        print("- Es una saiyanyin <3 del equipo universo 6.\n")
    elif personajes == "kale":
        print("- Es una saiyanyin <3 del equipo universo 6.\n")
    elif personajes == "rota":
        print("- Es un luchador del equipo universo 6. y nunca pudo mostrar su técnica secreta xD\n")
    elif personajes == "saonel":
        print("- Es un luchador del equipo universo 6.\n")
    elif personajes == "pilina":
        print("- Es un luchador del equipo universo 6.\n")
    elif personajes == "kefla":
        print("- Es la fusón de caulifla <3 y kale usando los pendientes Pothala.\n")
    elif personajes == "gohan":
        print("- Es el hijo mayor de Goku esposo de Videl y del equipo universo 7.\n")
    elif personajes == "goku":
        print("- Es el protector de la tierra y el más fuerte del universo 7 y del equipo universo 7.\n")
    elif personajes == "vegeta":
        print("- Es el principe de los sayayines y del equipo universo 7.\n")
    elif personajes == "piccolo":
        print("- Es un namekiano amigo de Goku , también es su niñero y del equipo universo 7.\n")
    elif personajes == "17":
        print("- Es un androide, guardabosques heramno de Nº18 y del equipo universo 7.\n")
    elif personajes == "18":
        print("- Es la esposa de Krilin y la madre de Marron,hermana de Nº17 y del equipo universo 7.\n")
    elif personajes == "krilin":
        print("- Es el esposo de Nº18 y mejor amigo de Goku, y del equipo universo 7.\n")
    elif personajes == "tenshinhan":
        print("- Es uno de los guerreros Z, tiene 3 ojos y es maestro de artes marciales, y del equipo universo 7.\n")
    elif personajes == "roshi":
        print("- Es el maestro de Goku y Krilin, y del equipo universo 7.\n")
    elif personajes == "kamekame":
        print("- Es el maestro de Goku y Krilin, y del equipo universo 7.\n")
    elif personajes == "senin":
        print("- Es el maestro de Goku y Krilin, y del equipo universo 7.\n")
    elif personajes == "sen'nin":
        print("- Es el maestro de Goku y Krilin, y del equipo universo 7.\n")
    elif personajes == "freezer":
        print("- Es el emperador del mal en el universo 7, y del equipo universo 7.\n")
    elif personajes == "bergamo":
        print(
            "- Es una especie de lobo que absorbe la energía de los golpes que recibe para ser mas fuerte, líder del "
            "Trío Peligro, hermano de Lavenda y Basil, y del equipo universo 9.\n")
    elif personajes == "lavenda":
        print(
            "- Es una especie de lobo que escupe veneno, miembro del Trío Peligro, hermano de Verg.. digo Bergamo y "
            "Basil, y del equipo universo 9.\n")
    elif personajes == "basil":
        print(
            "- Es una especie de lobo que puede mover los pies muuuuy rápido, miembro del Trío Peligro, heramno de "
            "Verg.. digo Bergamo y Lavenda, y del equipo universo 9.\n")
    elif personajes == "hyssop":
        print("- Es un luchador del equipo universo 9.\n")
    elif personajes == "cheppil":
        print("- Es un luchador del equipo universo 9.\n")
    elif personajes == "comfrey":
        print("- Es un luchador del equipo universo 9.\n")
    elif personajes == "hop":
        print("- Es un luchador del equipo universo 9.\n")
    elif personajes == "oregano":
        print("- Es un luchador del equipo universo 9.\n")
    elif personajes == "sorrel":
        print("- Es un luchador del equipo universo 9.\n")
    elif personajes == "roselle":
        print("- Es un luchador del equipo universo 9.\n")
    elif personajes == "dium":
        print("- Es un luchador del equipo universo 10.\n")
    elif personajes == "jirasen":
        print("- Es un luchador del equipo universo 10.\n")
    elif personajes == "lilibeu":
        print("- Es un luchador del equipo universo 10.\n")
    elif personajes == "rubalt":
        print("- Es un luchador del equipo universo 10.\n")
    elif personajes == "methiop":
        print("- Es un luchador del equipo universo 10.\n")
    elif personajes == "murichim":
        print("- Es un luchador del equipo universo 10.\n")
    elif personajes == "murisarm":
        print("- Es un luchador del equipo universo 10.\n")
    elif personajes == "napapa":
        print("- Es un luchador del equipo universo 10.\n")
    elif personajes == "obuni":
        print("- Es un luchador del equipo universo 10.\n")
    elif personajes == "zircol":
        print("- Es un luchador del equipo universo 10.\n")
    elif personajes == "jiren":
        print(
            "- Es guerrero a quien le importa una .... todos, es ULTRAMEGAFUERTE, miembro de las Tropas del Orgullo y "
            "del equipo universo 11.\n")
    elif personajes == "toppo":
        print(
            "- Es el candidato a dios de la destrucción de su universo (seguramente porque Jiren no acepto xD), lider "
            "de las Tropas del Orgullo y del equipo universo 11.\n")
    elif personajes == "dispo":
        print(
            "- Es un luchador (parece bugs bunny) más rápido que el sonido, miembro del las Tropas del Orgullo y del "
            "equipo universo 11.\n")
    elif personajes == "casseral":
        print("- Es un luchador general de las Tropas del Orgullo y del equipo universo 11.\n")
    elif personajes == "cocotte":
        print("- Es un luchador del equipo universo 11.\n")
    elif personajes == "vuon":
        print("- Es un luchador del equipo universo 11.\n")
    elif personajes == "kettle":
        print("- Es un luchador del equipo universo 11.\n")
    elif personajes == "tupper":
        print("- Es un luchador del equipo universo 11.\n")
    elif personajes == "zoirei":
        print("- Es un luchador del equipo universo 11.\n")
    elif personajes == "kunsi":
        print("- Es un luchador del equipo universo 11.\n")
    # dioses de la destruccionm, angeles y kaio de los 12 universos
    elif personajes == "awamo":
        print("- Es un ángel, guardián y maestro del dios de la destrucción del universo 1.\n")
    elif personajes == "iwen":
        print("- Es el dios de la destrucción del universo 1.\n")
    elif personajes == "sour":
        print("- Es un ángel, guardián y maestro del dios de la destrucción del universo 2.\n")
    elif personajes == "heles":
        print("- Es el dios de la destrucción del universo 2.\n")
    elif personajes == "capahri":
        print("- Es un ángel, guardián y maestro del dios de la destrucción del universo 3.\n")
    elif personajes == "mosco":
        print("- Es el dios de la destrucción del universo 3.\n")
    elif personajes == "cognic":
        print("- Es un ángel, guardián y maestro del dios de la destrucción del universo 4.\n")
    elif personajes == "quitela":
        print("- Es el dios de la destrucción del universo 4.\n")
    elif personajes == "cucatail":
        print("- Es un ángel, guardián y maestro del dios de la destrucción del universo 5.\n")
    elif personajes == "arak":
        print("- Es el dios de la destrucción del universo 5.\n")
    elif personajes == "vados":
        print("- Es un ángel, guardián y maestro del dios de la destrucción del universo 6.\n")
    elif personajes == "champa":
        print("- Es el dios de la destrucción del universo 6.\n")
    elif personajes == "whis":
        print("- Es un ángel, guardián y maestro del dios de la destrucción del universo 7.\n")
    elif personajes == "bills":
        print("- Es el dios de la destrucción del universo 7.\n")
    elif personajes == "beerus":
        print("- Es el dios de la destrucción del universo 7.\n")
    elif personajes == "korn":
        print("- Es un ángel, guardián y maestro del dios de la destrucción del universo 8.\n")
    elif personajes == "liquir":
        print("- Es el dios de la destrucción del universo 8.\n")
    elif personajes == "mojito":
        print("- Es un ángel, guardián y maestro del dios de la destrucción del universo 9.\n")
    elif personajes == "sidra":
        print("- Es el dios de la destrucción del universo 9.\n")
    elif personajes == "kus":
        print("- Es un ángel, guardián y maestro del dios de la destrucción del universo 10.\n")
    elif personajes == "rumoosh":
        print("- Es el dios de la destrucción del universo 10.\n")
    elif personajes == "marcarita":
        print("- Es un ángel, guardián y maestro del dios de la destrucción del universo 11.\n")
    elif personajes == "vermud":
        print("- Es el dios de la destrucción del universo 11.\n")
    elif personajes == "martinne":
        print("- Es un ángel, guardián y maestro del dios de la destrucción del universo 12.\n")
    elif personajes == "geen":
        print("- Es el dios de la destrucción del universo 12.\n")
    elif personajes == "anat":
        print("- Es el kaio de mayor rango del universo 1.\n")
    elif personajes == "peru":
        print("- Es el kaio de mayor rango del universo 2.\n")
    elif personajes == "ea":
        print("- Es el kaio de mayor rango del universo 3.\n")
    elif personajes == "kur":
        print("- Es el kaio de mayor rango del universo 4.\n")
    elif personajes == "ogma":
        print("- Es el kaio de mayor rango del universo 5.\n")
    elif personajes == "fuwa":
        print("- Es el kaio de mayor rango del universo 6.\n")
    elif personajes == "shin":
        print("- Es el kaio de mayor rango del universo 7.\n")
    elif personajes == "iii":
        print("- Es el kaio de mayor rango del universo 8.\n")
    elif personajes == "row":
        print("- Es el kaio de mayor rango del universo 9.\n")
    elif personajes == "gowas":
        print("- Es el kaio de mayor rango del universo 10.\n")
    elif personajes == "kai":
        print("- Es el kaio de mayor rango del universo 11.\n")
    elif personajes == "ag":
        print("- Es el kaio de mayor rango del universo 12.\n")

def preguntas(directas):  # JORDI----------------------------
    if directas == "padre":
        print("- No tengo padre, ni madre, ni perro que me ladre...  :( \nSoy producto de la inteligencia Artificial, "
              "mis creadores son Jordi Miño y Roberth Cobeña\n")
    elif directas == "nombre":
        print("- ドラゴンボール超 y se pronuncia Doragon Bōru Sūpā.\n")
    elif directas == "universos":
        print("- Son 12 universos y cada universo tiene un gemelo; Eran 18 pero el Rey de Todo destruyó 6.\n")
    elif directas == "omniverso":
        print("- Es como se denomida al conjunto de todos los universos y líneas de tiempo.\n")
    elif directas == "dioses":
        print("- Son mushísismo!!!\n")
    elif directas == "destruccion":
        print("- Son 12 Hakai-Shin o dioses de la destrucción, uno por cada universo.\nY si cuentas a Toppo serían 13.\n")
    elif directas == "angeles":
        print("- Son 12 Tenshi o ángeles, uno por cada dios de la destrucción.\nSin contar al Gran Sacerdote.\n")
    elif directas == "creación":
        print(
            "- Son 4 Kaio-Shin o dioses de la creación por universo pero no son 48.\nSin contar a los Gran Kaio-Sihn.\n")
def indagacion(estados):
    if estados == "estas":
        print("- Estoy muy bien, y tu?\n")
    elif estados == "llamo":
        print("- Tu nombre es " + nombre + "...\n")
    elif estados == "llamas":
        print("- Me llamo Tenshin-Bot\n")
    elif estados == "si":
        print("- Ya somos dos que sabemos del tema " + nombre + "...¡¡¡\n")
    elif estados == "no":
        print("- Puedes preguntarme cuanto quieras sobre Dragon Ball Súper " + nombre + "\n")
    elif estados == "querer":
        print("- Entonces espero poder ayudarte " + nombre + "\n")
def interrogantes(contest):
    if contest == "amor":
        print("- Supongo que un sentimiento importante para ti " + nombre + "\n")
    elif contest == "paz":
        print("- La pregunta es ¿qué consideras tu como paz?\n")
    elif contest == "reggaeton":
        print("- El reggaeton es una de las peores cosas que le ha pasado a la humanidad, los incultos llaman música a "
              "eso\n")
    elif contest == "rock":
        print("- Un genero musica inspirados en los dioses, el universo y lo perfecto, te lo recomiendo, o te faltan "
              "huev...\n")
    elif contest == "hecho":
        print("- Aqui conversando contigo, es lo unico que he hecho\n")
    elif contest == "pasado":
        print("- No se que ha pasado en realidad, mejor dimelo tu " + nombre + "\n")
    elif contest == "pasa":
        print("- A mi no me pasa nada y a ti " + nombre + "?\n")
    elif contest == "mejor1":
        print("- Lo mejor para mi es conversar contigo " + nombre + "\n")
    elif contest == "mejor2":
        print("- Solo se que tu nombre es " + nombre + "\n")
    elif contest == "mejor3":
        print("- Solo se cosas sobre el anime Dragon Ball Súper " + nombre + "\n")
    elif contest == "mejora":
        print("- Creo que lo mejor para ti es llevar una vida sana y ver un buen anime como Dragon Ball " + nombre + "\n")
    elif contest == "deseas":
        print("- no tengo ningun deseo mas que serte útil " + nombre + "\n")
    elif contest == "sabes":
        print("- Por ahora se conversar de una forma básica y de temas selectos\n")
    elif contest == "si":
        print("- Es bueno saberlo, cuentame mas\n")
    elif contest == "no":
        print("- ya tenemos algo en comun, a mi tampoco me agrada\n")
    elif contest == "mentir":
        print("- Nunca haria algo asi, me programaron para ayudarte y serte util\n")
    elif contest == "ayuda":
        print("- Haré lo que este a mi alcance, por lo pronto conversar contigo\n")
    else:
        print("- ¿Que de que " + nombre + "?\n")
def cultura(personalidad):
    if personalidad == "dragon":
        print("- Dragon Ball fue publicado por primera vez en 1984, de la mano de Akira Toriyama\n")
    elif personalidad == "super":
        print("- Dragon Ball Súper emitío su primer capitulo el 18 de junio del 2015\n")
    elif personalidad == "akira":
        print("- Akira Toriyama nacío en 1955, tiene 63 años...¡¡¡\n")
    elif personalidad == "goku":
        print("- Segun la cronologia del universo de Dragon Ball, Son Goku tiene alrrededor de 40 años\n")
    elif personalidad == "america":
        print("- Segun los libros en 1942 y fue Cristóbal Colón... pero " + nombre + "mejor hablemos de otra cosa\n")
    elif personalidad == "capi":
        print("- Dragon Ball Súper consta de 8 volumenes de manga y 131 de anime\n")
    elif personalidad == "capi2":
        print("- Dragon Ball Z consta de 42 volumenes de manga y 153 de anime\n")
    elif personalidad == "capi3":
        print("- Dragon Ball GT consta de 64 capitulos de anime\n")
    elif personalidad == "where":
        print("- Dragon Ball nació en tierras Niponas (Jápon) de la mano del Mangaka (dibujante) Akira Toriyama\n")
    elif personalidad == "where2":
        print("- Actualmente estamos en la ciudad de Guayaquil en la República del  Ecuador\n")
    elif personalidad == "why":
        print("- Mis creadores aplicadando conocimientos de informatica, la Inteligencia Artificial y el Procesamiento del lenguaje Humano me programaron para poder conversar contigo " + nombre + "...\n")
    elif personalidad == "why2":
        print("- Seguramente estas feo " + nombre + "...\n")
    elif personalidad == "why3":
        print("- No soy bueno recordando edades " + nombre + ", pero igual dime tu edad...\n")
    elif personalidad == "why4":
        print("- Apenas tengo 3 meses de edad " + nombre + "\n")
    elif personalidad == "time":
        print("- Ahora mismo son las: " + time.strftime ("%c") + " " +  nombre + "\n")
    else:
        print("- Cuando/Cuanto que ????\n")
# _____________________________________________________________________________________________________________________________________________________________
# Empieza la conversacion
nombre = input("Para empezar escribe tu nombre: ")
fin = 0
pausa = 0
a = input("\nHola " + nombre + "...¡¡¡\n")
# _____________________________________________________________________________________________________________________________________________________________
# Funcion principal para unigrams
# chat

while fin == 0:
    a = a.lower()
# ______________________________________________________________________________________________________________________________________________________________
# despedida
    for desp in despedida:
        if a == desp:
            v = rd.randint(0, len(despedida) - 1)
            print(despedida[v] + " " + nombre + "\n")
            fin = 1
            break
# ______________________________________________________________________________________________________________________________________________________________
# saludo
    for palabra in saludos:
        if a == palabra:
            v = rd.randint(0, len(saludos) - 1)
            print("- " + saludos[v] + " " + nombre + "\n")
        break
# _______________________________________________________________________________________________________________________________________________________________
# Deteccion de preguntas y espaciado despues de signo ?
    if a[len(a) - 1:] == "?":
        a = a[:len(a) - 1] + " ?"
# _______________________________________________________________________________________________________________________________________________________________
# Detectar e ignorar articulos
    lista_tmp = a.split()
    lista = []
    bandera = False
    for palart in lista_tmp:
        for artis in articulos:
            if palart == artis:
                bandera = True
                break
        if not bandera:
            lista.append(palart)
        else:
            bandera = False
    band_pregunta = False
# _________________________________________________________________________________________________________________________________________________________________
# PREGUNTAS SECCION: Personajes DBS
    for pal in lista:
        if pal == "conoces":
            for pals in lista:
                for per in lista_personajes:
                    if pals == per:
                        print("- No...., porqueee no es real ._. \n")
                        pausa = 1
                        break
            for pals in lista:
                for per in lista_angeles:
                    if pals == per:
                        print("- Ninguno de los angeles son reales ._. \n")
                        pausa = 1
                        break
            for pals in lista:
                for per in lista_destruccion:
                    if pals == per:
                        print("- No, por fortuna son imaginarios ._. \n")
                        pausa = 1
                        break
            for pals in lista:
                for per in lista_universo1:
                    if pals == per:
                        print("- No, El universo 1 no es real ._. \n")
                        pausa = 1
                        break
            for pals in lista:
                for per in lista_universo2:
                    if pals == per:
                        print("- No, el universo 2 no es real ._. \n")
                        pausa = 1
                        break
            for pals in lista:
                for per in lista_universo3:
                    if pals == per:
                        print("- No, el universo 3 no es real ._. \n")
                        pausa = 1
                        break
            for pals in lista:
                for per in lista_universo4:
                    if pals == per:
                        print("- No, el universo 4 no es real ._. \n")
                        pausa = 1
                        break
            for pals in lista:
                for per in lista_universo5:
                    if pals == per:
                        print("- No, el universo 5 no es real ._. \n")
                        pausa = 1
                        break
            for pals in lista:
                for per in lista_universo6:
                    if pals == per:
                        print("- No, el universo 6 no es real ._. \n")
                        pausa = 1
                        break
            for pals in lista:
                for per in lista_universo7:
                    if pals == per:
                        print("- Aunque técnicamente es de nuestro universo, ningun personaje de DBS es real ._. \n")
                        pausa = 1
                        break
            for pals in lista:
                for per in lista_universo8:
                    if pals == per:
                        print("- No, el universo 8 no es real ._. \n")
                        pausa = 1
                        break
            for pals in lista:
                for per in lista_universo9:
                    if pals == per:
                        print("- No, el universo 9 no es real ._. \n")
                        pausa = 1
                        break
            for pals in lista:
                for per in lista_universo10:
                    if pals == per:
                        print("- No, el universo 10 no es real ._. \n")
                        pausa = 1
                        break
            for pals in lista:
                for per in lista_universo11:
                    if pals == per:
                        print("- No, el universo 11 no es real ._. \n")
                        pausa = 1
                        break
            for pals in lista:
                for per in lista_universo12:
                    if pals == per:
                        print("- No, el universo 12 no es real ._. \n")
                        pausa = 1
                        break
        elif pal == "padre" or pal == "madre" or pal == "papa" or pal == "papá" or pal == "mama" or pal == "mamá":
            preguntas("padre")
            band_pregunta = True
            pausa = 1
            break
        elif pal == "quien" or pal == "quién":
            for pals in lista:
                for per in lista_personajes:
                    if pals == per:
                        sabes(per)
                        band_pregunta = True
                        pausa = 1
                        break
                for per in lista_universo1:
                    if pals == per:
                        sabes(per)
                        band_pregunta = True
                        pausa = 1
                        break
                for per in lista_universo2:
                    if pals == per:
                        sabes(per)
                        band_pregunta = True
                        pausa = 1
                        break
                for per in lista_universo3:
                    if pals == per:
                        sabes(per)
                        band_pregunta = True
                        pausa = 1
                        break
                for per in lista_universo4:
                    if pals == per:
                        sabes(per)
                        band_pregunta = True
                        pausa = 1
                        break
                for per in lista_universo5:
                    if pals == per:
                        sabes(per)
                        band_pregunta = True
                        pausa = 1
                        break
                for per in lista_universo6:
                    if pals == per:
                        sabes(per)
                        band_pregunta = True
                        pausa = 1
                        break
                for per in lista_universo7:
                    if pals == per:
                        sabes(per)
                        band_pregunta = True
                        pausa = 1
                        break
                for per in lista_universo8:
                    if pals == per:
                        sabes(per)
                        band_pregunta = True
                        pausa = 1
                        break
                for per in lista_universo9:
                    if pals == per:
                        sabes(per)
                        band_pregunta = True
                        pausa = 1
                        break
                for per in lista_universo10:
                    if pals == per:
                        sabes(per)
                        band_pregunta = True
                        pausa = 1
                        break
                for per in lista_universo11:
                    if pals == per:
                        sabes(per)
                        band_pregunta = True
                        pausa = 1
                        break
                for per in lista_universo12:
                    if pals == per:
                        sabes(per)
                        band_pregunta = True
                        pausa = 1
                        break
        elif pal == "omniverso":
            preguntas("omniverso")
            band_pregunta = True
            pausa = 1
            break
        elif pal == "universos":
            for pals in lista:
                if pals == "son" or pals == "hay":
                    preguntas("universos")
                    band_pregunta = True
                    pausa = 1
                    break
        elif pal == "lugar":
            for pals in lista:
                if pals == "torneo":
                    print("El torneo de poder se llevó a cabo em el Reino de la Nada.\n")
                    pausa = 1
                    band_pregunta = True
                    break
        elif pal == "cuanto" or pal == "cuánto" or pal == "limite" or pal == "límite":
            for pals in lista:
                if pals == "tiempo":
                    for p in lista:
                        if p == "reunir":
                            print("40 horas terricolas.\n")
                            pausa = 1
                            band_pregunta = True
                            break
                    print("El torneo de poder duraba máximo 48 minutos.\n")
                    pausa = 1
                    band_pregunta = True
                    break
        elif pal == "inicia" or pal == "iniciaba" or pal == "iniciaría":
            for pals in lista:
                if pals == "torneo":
                    print("El torneo inició exáctamente el día 3.135.500.603 del calendario real a sus 157 horas.\n")
                    pausa = 1
                    band_pregunta = True
                    break
        elif pal == "participantes" or pal == "peleadores" or pal == "guerreros" or pal == "luchadores":
            for pals in lista:
                if pals == "universo":
                    print("10 peleadores por universo, pero fueron son 80.\n")
                    pausa = 1
                    band_pregunta = True
                    break
        elif pal == "premio":
            for pals in lista:
                if pals == "torneo":
                    print("El premio era un deseo de las Súper Esferas del Dragón.\n")
                    pausa = 1
                    band_pregunta = True
                    break
        elif pal == "migatte" or pal == "doctrina":
            for pals in lista:
                if pals == "es":
                    print("El un estado que permite a tu cuempre moverse a voluntad.\n")
                    pausa = 1
                    band_pregunta = True
                    break
        elif pal == "ultima" or pal == "ultimo" or pal == "último" or pal == "última":
            for pals in lista:
                if pals == "pelea" or pals == "batalla" or pals == "enfrentamiento":
                    print("LA última pelea fue Jiren vs Goku, Frezeer y Nº17.\n")
                    pausa = 1
                    band_pregunta = True
                    break
        elif pal == "reglas":
            for pals in lista:
                if pals == "torneo":
                    print("No matar, no volar (a no ser que tengas alas), no usar armas.\n")
                    pausa = 1
                    band_pregunta = True
                    break
        elif pal == "ganador" or pal == "triunfador":
            for pals in lista:
                if pals == "torneo":
                    print("Ganó el universo 7 siendo Nº17 el último en pié.\n")
                    pausa = 1
                    band_pregunta = True
                    break
        elif pal == "perdedor" or pal == "pierde" or pal == "perdedores":
            for pals in lista:
                if pals == "torneo":
                    print("Si un equipo del torneo pierde, el Rey de Todo los elimina junto a todo su Universo.\n")
                    pausa = 1
                    band_pregunta = True
                    break
        elif pal == "sale" or pal == "cae":
            for pals in lista:
                if pals == "plataforma":
                    print("Si un participante cae de la plataforma es descalificado.\n")
                    pausa = 1
                    band_pregunta = True
                    break
        elif pal == "mata" or pal == "asesina":
            for pals in lista:
                print("Si participante mata a otro, es descalificado.\n")
                pausa = 1
                band_pregunta = True
                break
        elif pal == "plataforma":
            for pals in lista:
                if pals == "material" or pals =="hecha":
                    print("Esta construida de Acero Kachi Kacchin\n")
                    pausa = 1
                    band_pregunta = True
                    break
        elif pal == "dioses":
            for pals in lista:
                if pals == "son" or pals == "hay":
                    preguntas("dioses")
                    band_pregunta = True
                    pausa = 1
                    break
                elif pals == "destruccion" or pals == "destrucción":
                    preguntas("destruccion")
                    band_pregunta = True
                    pausa = 1
                    break
                elif pals == "creacion" or pals == "creación":
                    preguntas("creacion")
                    band_pregunta = True
                    pausa = 1
                    break
        elif pal == "angeles" or pal == "ángeles":
            for pals in lista:
                if pals == "son" or pals == "hay":
                    preguntas("angeles")
                    band_pregunta = True
                    pausa = 1
                    break
        elif pal == "japones" or pal == "japonés":
            for pals in lista:
                if pals == "dragon":
                    preguntas("nombre")
                    band_pregunta = True
                    pausa = 1
                    break
        elif pal == "quienes" or pal == "cuales" or pal == "cuáles":
            for pals in lista:
                if pals == "personajes" or pals == "parte":
                    for p in lista:
                        todos = ""
                        if p == "universo":
                            for pl in lista:
                                if pl == "1":
                                    for t in lista_universo1:
                                       todos = todos + t + " "
                                    print("Son: " + todos)
                                    band_pregunta = True
                                    pausa = 1
                                    break
                                elif pl == "2":
                                    for t in lista_universo12:
                                       todos = todos + t + " "
                                    print("Son: " + todos)
                                    band_pregunta = True
                                    pausa = 1
                                    break
                                elif pl == "3":
                                    for t in lista_universo3:
                                       todos = todos + t + " "
                                    print("Son: " + todos)
                                    band_pregunta = True
                                    pausa = 1
                                    break
                                elif pl == "4":
                                    for t in lista_universo4:
                                       todos = todos + t + " "
                                    print("Son: " + todos)
                                    band_pregunta = True
                                    pausa = 1
                                    break
                                elif pl == "5":
                                    for t in lista_universo5:
                                       todos = todos + t + " "
                                    print("Son: " + todos)
                                    band_pregunta = True
                                    pausa = 1
                                    break
                                elif pl == "6":
                                    for t in lista_universo6:
                                       todos = todos + t + " "
                                    print("Son: " + todos)
                                    band_pregunta = True
                                    pausa = 1
                                    break
                                elif pl == "7":
                                    for t in lista_universo7:
                                       todos = todos + t + " "
                                    for t in lista_personajes:
                                       todos = todos + t + " "
                                    print("Son: " + todos)
                                    band_pregunta = True
                                    pausa = 1
                                    break
                                elif pl == "8":
                                    for t in lista_universo8:
                                       todos = todos + t + " "
                                    print("Son: " + todos)
                                    band_pregunta = True
                                    pausa = 1
                                    break
                                elif pl == "9":
                                    for t in lista_universo9:
                                       todos = todos + t + " "
                                    print("Son: " + todos)
                                    band_pregunta = True
                                    pausa = 1
                                    break
                                elif pl == "10":
                                    for t in lista_universo10:
                                       todos = todos + t + " "
                                    print("Son: " + todos)
                                    band_pregunta = True
                                    pausa = 1
                                    break
                                elif pl == "11":
                                    for t in lista_universo11:
                                       todos = todos + t + " "
                                    print("Son: " + todos)
                                    band_pregunta = True
                                    pausa = 1
                                    break
                                elif pl == "12":
                                    for t in lista_universo12:
                                       todos = todos + t + " "
                                    print("Son: " + todos)
                                    band_pregunta = True
                                    pausa = 1
                                    break
                        elif p == "universo1":
                            for t in lista_universo1:
                               todos = todos + t + " "
                            print("Son: " + todos)
                            band_pregunta = True
                            pausa = 1
                            break
                        elif p == "universo2":
                            for t in lista_universo12:
                               todos = todos + t + " "
                            print("Son: " + todos)
                            band_pregunta = True
                            pausa = 1
                            break
                        elif p == "universo3":
                            for t in lista_universo3:
                               todos = todos + t + " "
                            print("Son: " + todos)
                            band_pregunta = True
                            pausa = 1
                            break
                        elif p == "universo4":
                            for t in lista_universo4:
                               todos = todos + t + " "
                            print("Son: " + todos)
                            band_pregunta = True
                            pausa = 1
                            break
                        elif p == "universo5":
                            for t in lista_universo5:
                               todos = todos + t + " "
                            print("Son: " + todos)
                            band_pregunta = True
                            pausa = 1
                            break
                        elif p == "universo6":
                            for t in lista_universo6:
                               todos = todos + t + " "
                            print("Son: " + todos)
                            band_pregunta = True
                            pausa = 1
                            break
                        elif p == "universo7":
                            for t in lista_universo7:
                               todos = todos + t + " "
                            for t in lista_personajes:
                               todos = todos + t + " "
                            print("Son: " + todos)
                            band_pregunta = True
                            pausa = 1
                            break
                        elif p == "universo8":
                            for t in lista_universo8:
                               todos = todos + t + " "
                            print("Son: " + todos)
                            band_pregunta = True
                            pausa = 1
                            break
                        elif p == "universo9":
                            for t in lista_universo9:
                               todos = todos + t + " "
                            print("Son: " + todos)
                            band_pregunta = True
                            pausa = 1
                            break
                        elif p == "universo10":
                            for t in lista_universo10:
                               todos = todos + t + " "
                            print("Son: " + todos)
                            band_pregunta = True
                            pausa = 1
                            break
                        elif p == "universo11":
                            for t in lista_universo11:
                               todos = todos + t + " "
                            print("Son: " + todos)
                            band_pregunta = True
                            pausa = 1
                            break
                        elif p == "universo12":
                            for t in lista_universo12:
                               todos = todos + t + " "
                            print("Son: " + todos)
                            band_pregunta = True
                            pausa = 1
                            break
        elif pal == "universo":
            for pals in lista:
                for per in lista_universo1:
                    if pals == per:
                        print("Del universo 1\n")
                        band_pregunta = True
                        pausa = 1
                        break
                for per in lista_universo2:
                    if pals == per:
                        print("Del universo 2\n")
                        band_pregunta = True
                        pausa = 1
                        break
                for per in lista_universo3:
                    if pals == per:
                        print("Del universo 3\n")
                        band_pregunta = True
                        pausa = 1
                        break
                for per in lista_universo4:
                    if pals == per:
                        print("Del universo 4\n")
                        band_pregunta = True
                        pausa = 1
                        break
                for per in lista_universo5:
                    if pals == per:
                        print("Del universo 5\n")
                        band_pregunta = True
                        pausa = 1
                        break
                for per in lista_universo6:
                    if pals == per:
                        print("Del universo 6\n")
                        band_pregunta = True
                        pausa = 1
                        break
                for per in lista_universo7:
                    if pals == per:
                        print("Del universo 7\n")
                        band_pregunta = True
                        pausa = 1
                        break
                for per in lista_personajes:
                    if pals == per:
                        print("Del universo 7\n")
                        band_pregunta = True
                        pausa = 1
                        break
                for per in lista_universo9:
                    if pals == per:
                        print("Del universo 8\n")
                        band_pregunta = True
                        pausa = 1
                        break
                for per in lista_universo10:
                    if pals == per:
                        print("Del universo 9\n")
                        band_pregunta = True
                        pausa = 1
                        break
                for per in lista_universo1:
                    if pals == per:
                        print("Del universo 10\n")
                        band_pregunta = True
                        pausa = 1
                        break
                for per in lista_universo1:
                    if pals == per:
                        print("Del universo 11\n")
                        band_pregunta = True
                        pausa = 1
                        break
                for per in lista_universo1:
                    if pals == per:
                        print("Del universo 12\n")
                        band_pregunta = True
                        pausa = 1
                        break
        elif pal == "dios":
            for p in lista:
                if p == "destruccion" or p == "destrucción" or p == "destructor":
                    for pals in lista:
                        if pals == "universo":
                            for pl in lista:
                                if pl == "1":
                                    print("El dios de la destrucción del universo 1 es " + lista_universo1[0])
                                    pausa = 1
                                    band_pregunta = True
                                    break
                                elif pl == "2":
                                    print("El dios de la destrucción del universo 2 es " +lista_universo2[0])
                                    pausa = 1
                                    band_pregunta = True
                                    break
                                elif pl == "3":
                                    print("El dios de la destrucción del universo 3 es " +lista_universo3[0])
                                    pausa = 1
                                    band_pregunta = True
                                    break
                                elif pl == "4":
                                    print("El dios de la destrucción del universo 4 es " +lista_universo4[0])
                                    pausa = 1
                                    band_pregunta = True
                                    break
                                elif pl == "5":
                                    print("El dios de la destrucción del universo 5 es " +lista_universo5[0])
                                    pausa = 1
                                    band_pregunta = True
                                    break
                                elif pl == "6":
                                    print("El dios de la destrucción del universo 6 es " +lista_universo6[0])
                                    pausa = 1
                                    band_pregunta = True
                                    break
                                elif pl == "7":
                                    print("El dios de la destrucción del universo 7 es " +lista_universo7[0])
                                    pausa = 1
                                    band_pregunta = True
                                    break
                                elif pl == "8":
                                    print("El dios de la destrucción del universo 8 es " +lista_universo8[0])
                                    pausa = 1
                                    band_pregunta = True
                                    break
                                elif pl == "9":
                                    print("El dios de la destrucción del universo 9 es " +lista_universo9[0])
                                    pausa = 1
                                    band_pregunta = True
                                    break
                                elif pl == "10":
                                    print("El dios de la destrucción del universo 0 es " +lista_universo10[0])
                                    pausa = 1
                                    band_pregunta = True
                                    break
                                elif pl == "11":
                                    print("El dios de la destrucción del universo 11 es " +lista_universo11[0])
                                    pausa = 1
                                    band_pregunta = True
                                    break
                                elif pl == "12":
                                    print("El dios de la destrucción del universo 12 es " +lista_universo12[0])
                                    pausa = 1
                                    band_pregunta = True
                                    break
                        elif pals == "universo1":
                            print("El dios de la destrucción del universo 1 es " +lista_universo1[0])
                            pausa = 1
                            band_pregunta = True
                            break
                        elif pals == "universo2":
                            print("El dios de la destrucción del universo 2 es " +lista_universo2[0])
                            pausa = 1
                            band_pregunta = True
                            break
                        elif pals == "universo3":
                            print("El dios de la destrucción del universo 3 es " +lista_universo3[0])
                            pausa = 1
                            band_pregunta = True
                            break
                        elif pals == "universo4":
                            print("El dios de la destrucción del universo 4 es " +lista_universo4[0])
                            pausa = 1
                            band_pregunta = True
                            break
                        elif pals == "universo5":
                            print("El dios de la destrucción del universo 5 es " +lista_universo5[0])
                            pausa = 1
                            band_pregunta = True
                            break
                        elif pals == "universo6":
                            print("El dios de la destrucción del universo 6 es " +lista_universo6[0])
                            pausa = 1
                            band_pregunta = True
                            break
                        elif pals == "universo7":
                            print("El dios de la destrucción del universo 7 es " +lista_universo7[0])
                            pausa = 1
                            band_pregunta = True
                            break
                        elif pals == "universo8":
                            print("El dios de la destrucción del universo 8 es " +lista_universo8[0])
                            pausa = 1
                            band_pregunta = True
                            break
                        elif pals == "universo9":
                            print("El dios de la destrucción del universo 9 es " +lista_universo9[0])
                            pausa = 1
                            band_pregunta = True
                            break
                        elif pals == "universo10":
                            print("El dios de la destrucción del universo 10 es " +lista_universo10[0])
                            pausa = 1
                            band_pregunta = True
                            break
                        elif pals == "universo11":
                            print("El dios de la destrucción del universo 11 es " +lista_universo11[0])
                            pausa = 1
                            band_pregunta = True
                            break
                        elif pals == "universo12":
                            print("El dios de la destrucción del universo 12 es " +lista_universo12[0])
                            pausa = 1
                            band_pregunta = True
                            break
        elif pal == "angel":
            for pals in lista:
                if pals == "universo":
                    for pl in lista:
                        if pl == "1":
                            print("El Ángel  del universo 1 es " +lista_universo1[1])
                            pausa = 1
                            band_pregunta = True
                            break
                        elif pl == "2":
                            print("El Ángel  del universo 2 es " +lista_universo2[1])
                            pausa = 1
                            band_pregunta = True
                            break
                        elif pl == "3":
                            print("El Ángel  del universo 3 es " +lista_universo3[1])
                            pausa = 1
                            band_pregunta = True
                            break
                        elif pl == "4":
                            print("El Ángel  del universo 4 es " +lista_universo4[1])
                            pausa = 1
                            band_pregunta = True
                            break
                        elif pl == "5":
                            print("El Ángel  del universo 5 es " +lista_universo5[1])
                            pausa = 1
                            band_pregunta = True
                            break
                        elif pl == "6":
                            print("El Ángel  del universo 6 es " +lista_universo6[1])
                            pausa = 1
                            band_pregunta = True
                            break
                        elif pl == "7":
                            print("El Ángel  del universo 7 es " +lista_universo7[1])
                            pausa = 1
                            band_pregunta = True
                            break
                        elif pl == "8":
                            print("El Ángel  del universo 8 es " +lista_universo8[1])
                            pausa = 1
                            band_pregunta = True
                            break
                        elif pl == "9":
                            print("El Ángel  del universo 9 es " +lista_universo9[1])
                            pausa = 1
                            band_pregunta = True
                            break
                        elif pl == "10":
                            print("El Ángel  del universo 10 es " +lista_universo10[1])
                            pausa = 1
                            band_pregunta = True
                            break
                        elif pl == "11":
                            print("El Ángel  del universo 11 es " +lista_universo11[1])
                            pausa = 1
                            band_pregunta = True
                            break
                        elif pl == "12":
                            print("El Ángel  del universo 12 es " +lista_universo12[1])
                            pausa = 1
                            band_pregunta = True
                            break
                elif pals == "universo1":
                    print("El Ángel  del universo 1 es " +lista_universo1[1])
                    pausa = 1
                    band_pregunta = True
                    break
                elif pals == "universo2":
                    print("El Ángel  del universo 2 es " +lista_universo2[1])
                    pausa = 1
                    band_pregunta = True
                    break
                elif pals == "universo3":
                    print("El Ángel  del universo 3 es " +lista_universo3[1])
                    pausa = 1
                    band_pregunta = True
                    break
                elif pals == "universo4":
                    print("El Ángel  del universo 4 es " +lista_universo4[1])
                    pausa = 1
                    band_pregunta = True
                    break
                elif pals == "universo5":
                    print("El Ángel  del universo 5 es " +lista_universo5[1])
                    pausa = 1
                    band_pregunta = True
                    break
                elif pals == "universo6":
                    print("El Ángel  del universo 6 es " +lista_universo6[1])
                    pausa = 1
                    band_pregunta = True
                    break
                elif pals == "universo7":
                    print("El Ángel  del universo 7 es " +lista_universo7[1])
                    pausa = 1
                    band_pregunta = True
                    break
                elif pals == "universo8":
                    print("El Ángel  del universo 8 es " +lista_universo8[1])
                    pausa = 1
                    band_pregunta = True
                    break
                elif pals == "universo9":
                    print("El Ángel  del universo 9 es " +lista_universo9[1])
                    pausa = 1
                    band_pregunta = True
                    break
                elif pals == "universo10":
                    print("El Ángel  del universo 10 es " +lista_universo10[1])
                    pausa = 1
                    band_pregunta = True
                    break
                elif pals == "universo11":
                    print("El Ángel  del universo 11 es " +lista_universo11[1])
                    pausa = 1
                    band_pregunta = True
                    break
                elif pals == "universo12":
                    print("El Ángel  del universo 12 es " +lista_universo12[1])
                    pausa = 1
                    band_pregunta = True
                    break
        elif pal == "kaio":
            for pals in lista:
                if pals == "universo":
                    for pl in lista:
                        if pl == "1":
                            print("El Kaio de mayor rango del universo 1 es " +lista_universo1[2])
                            pausa = 1
                            band_pregunta = True
                            break
                        elif pl == "2":
                            print("El Kaio de mayor rango del universo 2 es " +lista_universo2[2])
                            pausa = 1
                            band_pregunta = True
                            break
                        elif pl == "3":
                            print("El Kaio de mayor rango del universo 3 es " +lista_universo3[2])
                            pausa = 1
                            band_pregunta = True
                            break
                        elif pl == "4":
                            print("El Kaio de mayor rango del universo 4 es " +lista_universo4[2])
                            pausa = 1
                            band_pregunta = True
                            break
                        elif pl == "5":
                            print("El Kaio de mayor rango del universo 5 es " +lista_universo5[2])
                            pausa = 1
                            band_pregunta = True
                            break
                        elif pl == "6":
                            print("El Kaio de mayor rango del universo 6 es " +lista_universo6[2])
                            pausa = 1
                            band_pregunta = True
                            break
                        elif pl == "7":
                            print("El Kaio de mayor rango del universo 7 es " +lista_universo7[2])
                            pausa = 1
                            band_pregunta = True
                            break
                        elif pl == "8":
                            print("El Kaio de mayor rango del universo 8 es " +lista_universo8[2])
                            pausa = 1
                            band_pregunta = True
                            break
                        elif pl == "9":
                            print("El Kaio de mayor rango del universo 9 es " +lista_universo9[2])
                            pausa = 1
                            band_pregunta = True
                            break
                        elif pl == "10":
                            print("El Kaio de mayor rango del universo 10 es " +lista_universo10[2])
                            pausa = 1
                            band_pregunta = True
                            break
                        elif pl == "11":
                            print("El Kaio de mayor rango del universo 11 es " +lista_universo11[2])
                            pausa = 1
                            band_pregunta = True
                            break
                        elif pl == "12":
                            print("El Kaio de mayor rango del universo 12 es " +lista_universo12[2])
                            pausa = 1
                            band_pregunta = True
                            break
                elif pals == "universo1":
                    print("El Kaio de mayor rango del universo 1 es " +lista_universo1[2])
                    pausa = 1
                    band_pregunta = True
                    break
                elif pals == "universo2":
                    print("El Kaio de mayor rango del universo 2 es " +lista_universo2[2])
                    pausa = 1
                    band_pregunta = True
                    break
                elif pals == "universo3":
                    print("El Kaio de mayor rango del universo 3 es " +lista_universo3[2])
                    pausa = 1
                    band_pregunta = True
                    break
                elif pals == "universo4":
                    print("El Kaio de mayor rango del universo 4 es " +lista_universo4[2])
                    pausa = 1
                    band_pregunta = True
                    break
                elif pals == "universo5":
                    print("El Kaio de mayor rango del universo 5 es " +lista_universo5[2])
                    pausa = 1
                    band_pregunta = True
                    break
                elif pals == "universo6":
                    print("El Kaio de mayor rango del universo 6 es " +lista_universo6[2])
                    pausa = 1
                    band_pregunta = True
                    break
                elif pals == "universo7":
                    print("El Kaio de mayor rango del universo 7 es " +lista_universo7[2])
                    pausa = 1
                    band_pregunta = True
                    break
                elif pals == "universo8":
                    print("El Kaio de mayor rango del universo 8 es " +lista_universo8[2])
                    pausa = 1
                    band_pregunta = True
                    break
                elif pals == "universo9":
                    print("El Kaio de mayor rango del universo 9 es " +lista_universo9[2])
                    pausa = 1
                    band_pregunta = True
                    break
                elif pals == "universo10":
                    print("El Kaio de mayor rango del universo 10 es " +lista_universo10[2])
                    pausa = 1
                    band_pregunta = True
                    break
                elif pals == "universo11":
                    print("El Kaio de mayor rango del universo 11 es " +lista_universo11[2])
                    pausa = 1
                    band_pregunta = True
                    break
                elif pals == "universo12":
                    print("El Kaio de mayor rango del universo 12 es " +lista_universo12[2])
                    pausa = 1
                    band_pregunta = True
                    break
# _________________________________________________________________________________________________________________________________________________________________
# PREGUNTAS SUELTAS
        elif pal == "si":
            for pals in lista:
                if pals == 'se' or pals == 'conozco' or pals == 'idea' or pals == 'conocimiento' or pals == 'saber' or pals == 'dragon':
                    indagacion('si')
                    band_pregunta = True
                    pausa = 0
                    break
                elif pals == 'se' or pals == 'conozco' or pals == 'idea' or pals == 'conocimiento' or pals == 'saber' or pals == 'dragon':
                    indagacion('si')
                    band_pregunta = True
                    pausa = 0
                    break
        elif pal == "sabes" or pal == 'conoces':
            for pals in lista:
                for gust in lista_gusta:
                    if pals == gust:
                        print(" - Mis conocimientos son algo limitados, pero mi especialidad es Dragon Ball Súper\n")
                        pausa = 1
                        break
        elif pal == "no":
            for pals in lista:
                if pals == 'se' or pals == 'conozco' or pals == 'idea' or pals == 'conocimiento' or pals == 'saber':
                    indagacion('no')
                    pausa = 1
                    break
        elif pal == "tienes" or pal == "tengo" or pal == "estoy" or pal == "me":
            for pals in lista:
                if pals == 'novio' or pals == 'esposo' or pals == 'pelado' or pals == 'marido' or pals == 'enamorado':
                    relacion('novio')
                    band_pregunta = True
                    pausa = 0
                    break
                elif pals == "novia" or pals == 'esposa' or pals == 'pelada' or pals == 'enamorada':
                    relacion('novia')
                    band_pregunta = True
                    pausa = 0
                    break
                elif pals == "problemas" or pals == 'problema' or pals == 'duda' or pals == 'dudas':
                    relacion('problemas')
                    band_pregunta = True
                    pausa = 0
                    break
                elif pals == "hambre" or pals == 'sed' or pals == 'dolor' or pals == 'malestar' or pals == 'calor' or pals == 'frio' or pals == 'pereza':
                    relacion('hambre')
                    band_pregunta = True
                    pausa = 0
                    break
                elif pals == "felicidad" or pals == 'tristeza' or pals == 'enojo' or pals == 'angustia' or pals == 'miedo' or pals == 'alegria' or pals == 'ira':
                    relacion('feliz')
                    band_pregunta = True
                    pausa = 0
                    break
                elif pals == "respuesta" or pals == 'respuestas':
                    relacion('respuesta')
                    band_pregunta = True
                    pausa = 0
                    break
                elif pals == "mal" or pals == 'triste' or pals == 'tristeza':
                    relacion('mal')
                    band_pregunta = True
                    pausa = 0
                    break
                elif pals == "bien" or pals == 'super' or pals == 'genial' or pals == 'maravilla' or pals == 'excelente':
                    relacion('bien')
                    band_pregunta = True
                    pausa = 0
                    break
                elif pals == "si" or pals == 'simon' or pals == 'positivo' or pals == 'asi' or pals == 'afirmativo':
                    relacion('si')
                    band_pregunta = True
                    pausa = 0
                    break
                elif pals == "no" or pals == 'nones' or pals == 'negativo' or pals == 'nada' or pals == 'nel':
                    relacion('no')
                    band_pregunta = True
                    pausa = 0
                    break
                elif pals == 'mentirias' or pals == 'engañarias' or pals == 'mentira':
                    interrogantes('mentir')
                    band_pregunta = True
                    pausa = 0
                    break
                elif pals == 'favor' or pals == 'ayudarias' or pals == 'ayudar':
                    interrogantes('ayuda')
                    band_pregunta = True
                    pausa = 0
                    break
                elif pals == "gusta" or pal == "agrada" or pal == "emociona" or pal == "fascina" or pal == "favorito":
                    for pals in lista:
                        for gust in lista_gusta:
                            if pals == gust:
                                print("- " + nombre + ", es bueno saber que usas bien tu tiempo...\n")
                                band_pregunta = True
                                pausa = 0
                                break
            for pal in lista:
                if pal == "gusta" or pal == "agrada" or pal == "emociona" or pal == "fascina" or pal == "favorito":
                    for pals in lista:
                        for col in lista_colores:
                            if pals == col:
                                print("- Un color muy bonito " + nombre + ", a mi me gusta el verde limón\n")
                                band_pregunta = True
                                pausa = 0
                                break
            for pal in lista:
                if pal == "gusta" or pal == "agrada" or pal == "emociona" or pal == "fascina" or pal == "favorito":
                    for pals in lista:
                        for num in lista_numeros:
                            if pals == num:
                                print("- Es un numero interesante " + nombre + ", a mi me gustan los binarios 0 y 1\n")
                                band_pregunta = True
                                pausa = 0
                                break
            for pal in lista:
                if pal == "gusta" or pal == "agrada" or pal == "emociona" or pal == "fascina" or pal == "favorito":
                    for pals in lista:
                        for peli in lista_peliculas:
                            if pals == peli:
                                print(
                                    "- Esa es una buena pelicula " + nombre + ", mis favoritas son Yo Robot y El hombre Bicentenario\n")
                                band_pregunta = True
                                pausa = 0
                                break
            for pal in lista:
                if pal == "gusta" or pal == "agrada" or pal == "emociona" or pal == "fascina" or pal == "favorito":
                    for pals in lista:
                        for music in lista_artistas:
                            if pals == music:
                                print("- Veo que escuchas buena musica " + nombre + ", tenemos los mismos gustos\n")
                                band_pregunta = True
                                pausa = 0
                                break
            for pal in lista:
                if pal == "gusta" or pal == "agrada" or pal == "emociona" or pal == "fascina" or pal == "favorito":
                    for pals in lista:
                        for canci in lista_canciones:
                            if pals == canci:
                                print("- Buena cancion " + nombre + " definitivamente...¡¡¡\n")
                                band_pregunta = True
                                pausa = 0
                                break
        elif pal == "me":
            for pals in lista:
                if pals == "dedico":
                    for pl in lista:
                        for trab in lista_profesiones:
                            if pal == trab:
                                print("- Que interesante, cuentame mas de eso que haces\n")
                                pausa = 1
                            break
                elif pals == "gusta" or pals == "agrada" or pals == "emociona" or pals == "fascina" or pals == "favorito":
                    for p in lista:
                        for comi in lista_comida:
                            if p == comi:
                                print("- Tu su sabes comer " + nombre + "¡¡¡\n")
                                band_pregunta = True
                                pausa = 0
                            break
                        for comi2 in lista_comida2:
                            if p == comi2:
                                print("- Que gustos tan refinados " + nombre + "...\n")
                                band_pregunta = True
                                pausa = 0
                            break
        elif pal == "soy":
            for pals in lista:
                for trab in lista_profesiones:
                    if pals == trab:
                        print("- Que interesante, cuentame mas de eso que haces\n")
                        pausa = 1
                    break
        elif pal == "soy" or pal == "favorito":
            for pals in lista:
                if pals == "barcelona" or pals == "barcelonista":
                    equipo("barcelona\n")
                    band_pregunta = True
                    pausa = 0
                    break
                elif pals == "emelec" or pals == 'emeleccista' or pals == 'emelecista' or pals == 'gay':
                    equipo('emelec')
                    band_pregunta = True
                    pausa = 0
                    break
        elif pal == "como" or pal == "cual":
            for pals in lista:
                pals = pals.lower()
                if pals == 'estas':
                    indagacion('estas')
                    band_pregunta = True
                    pausa = 0
                    break
                elif pals == "llamo" or pals == "mi":
                    indagacion('llamo')
                    band_pregunta = True
                    pausa = 0
                    break
                elif pals == "llamas" or pals == "tu":
                    indagacion('llamas')
                    band_pregunta = True
                    pausa = 0
                    break
        elif pal == "que":
            for pals in lista:
                pals = pals.lower()
                if pals == 'amor':
                    interrogantes('amor')
                    band_pregunta = True
                    pausa = 0
                    break
                elif pals == 'paz':
                    interrogantes('paz')
                    band_pregunta = True
                    pausa = 0
                    break
                elif (pals == 'reggaeton') or (pals == 'reggeton') or (pals == 'regaeton') or (pals == 'regeton') or \
                        (pals == 'mierda') or (pals == 'caca'):
                    interrogantes('reggaeton')
                    band_pregunta = True
                    pausa = 0
                    break
                elif pals == 'rock':
                    interrogantes('rock')
                    band_pregunta = True
                    pausa = 0
                    break
                elif pals == 'hecho':
                    interrogantes('hecho')
                    band_pregunta = True
                    pausa = 0
                    break
                elif pals == 'pasado':
                    interrogantes('pasado')
                    band_pregunta = True
                    pausa = 0
                    break
                elif pals == 'pasa':
                    interrogantes('pasa')
                    band_pregunta = True
                    pausa = 0
                    break
                elif pals == 'mejor':
                    for sgsg in lista:
                        if sgsg == 'ti':
                            interrogantes('mejor1')
                            band_pregunta = True
                            pausa = 0
                            break
                        elif sgsg == 'mi':
                            interrogantes('mejora')
                            band_pregunta = True
                            pausa = 0
                            break
                elif pals == 'deseas':
                    interrogantes('deseas')
                    band_pregunta = True
                    pausa = 0
                    break
                elif pals == 'sabes':
                    for sgsg in lista:
                        if sgsg == 'mi':
                            interrogantes('mejor2')
                            band_pregunta = True
                            pausa = 0
                            break
                        elif sgsg == 'anime':
                            interrogantes('mejor3')
                            band_pregunta = True
                            pausa = 0
                            break
        elif pal == "eres" or pal == "pareces":
            for pals in lista:
                for ser in lista_alagos:
                    if pals == ser:
                        print("- Muchas gracias..¡¡¡\n")
                        band_pregunta = True
                        pausa = 0
                        break
                for ser in lista_insultos:
                    if pals == ser:
                        print("- PORQUE ME DICES ESO, SOLO QUIERO AYUDARTE...¡¡¡\n")
                        band_pregunta = True
                        pausa = 0
                        break
        elif pal == "soy" or pal == "favorito":
            for pals in lista:
                if pals == "barcelona" or pals == "barcelonista":
                    equipo("barcelona\n")
                    band_pregunta = True
                    pausa = 0
                    break
                elif pals == "emelec" or pals == 'emeleccista' or pals == 'emelecista' or pals == 'gay':
                    equipo('emelec')
                    band_pregunta = True
                    pausa = 0
                    break
        elif pal == "cuando" or pal == "año" or pal == "años":
            for pals in lista:
                pals = pals.lower()
                if pals == 'dragon':
                    cultura('dragon')
                    band_pregunta = True
                    pausa = 0
                    break
                elif pals == 'super':
                    cultura('super')
                    band_pregunta = True
                    pausa = 0
                    break
                elif pals == 'akira':
                    cultura('akira')
                    band_pregunta = True
                    pausa = 0
                    break
                elif pals == 'goku':
                    cultura('goku')
                    band_pregunta = True
                    pausa = 0
                    break
                elif pals == 'america':
                    cultura('america')
                    band_pregunta = True
                    pausa = 0
                    break
        elif pal == "cuantos" or pal == "cuanto":
            for pals in lista:
                pals = pals.lower()
                if pals == 'super':
                    cultura('capi')
                    band_pregunta = True
                    pausa = 0
                    break
                elif pals == 'z':
                    cultura('capi2')
                    band_pregunta = True
                    pausa = 0
                    break
                elif pals == 'gt':
                    cultura('capi3')
                    band_pregunta = True
                    pausa = 0
                    break
                elif pals == 'tengo':
                    cultura('why3')
                    band_pregunta = True
                    pausa = 0
                    break
                elif pals == 'tienes':
                    cultura('why4')
                    band_pregunta = True
                    pausa = 0
                    break
        elif pal == "donde":
            for pals in lista:
                pals = pals.lower()
                if pals == 'dragon':
                    cultura('where')
                    band_pregunta = True
                    pausa = 0
                    break
                elif pals == 'estamos':
                    cultura('where2')
                    band_pregunta = True
                    pausa = 0
                    break
        elif pal == "porque":
            for pals in lista:
                pals = pals.lower()
                if pals == 'sabes':
                    cultura('why')
                    band_pregunta = True
                    pausa = 0
                    break
                elif pals == 'ama':
                    cultura('why2')
                    band_pregunta = True
                    pausa = 0
                    break
        elif pal == "hora":
            for pals in lista:
                pals = pals.lower()
                if pals == 'tienes':
                    cultura('time')
                    band_pregunta = True
                    pausa = 0
                    break
        else:
            band_pregunta = False
#_______________________________________________________________________________________________________________________________________________________________
#Fin del chat

    lista_tmp = []
    if pausa == 1:
        pausa = 0
        a = input()
    else:
        if fin == 0:
            v = rd.randint(0, len(seguir) - 1)
            print(seguir[v] + " " + nombre + " ?\n")
            a = input("")
        elif not band_pregunta:
            v = rd.randint(0, len(noentiendo) - 1)
            print(noentiendo[v] + " " + nombre + "\n")