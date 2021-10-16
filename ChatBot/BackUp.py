# Notas de programadores: FAVOR IGNORAR
# -Roberth: Como Rodriguez no aporta nada, HAY QUE SACARLE PLATA
# -Jordi: Claroooooo XD
# _____________________________________________________________________________________________________________________________________________________________
# Presentacion
print ("\nUNIVERSIDAD AGRARIA DEL ECUADOR")
print ("MATERIA: Inteligencia Artificial")
print ("CURSO: 9SA")
print ("PROYECTO FINAL\n")
print ("DOCENTE:\n Ing. Charles Peréz\n")
print ("ALUMNOS:\n Cobeña Roberth\n Miño Jordi\n Rodriguez Byron\n")
print ("REGLAS DEL CHATBOT:")
print (" *Escribir unicamente en idioma español")
print (" *Usar ? para preguntas o cuestiones")
print (" *Reconoce solo algunas palabra con tilde")
print (" *Tener paciencia, es un prototipo en crecimiento")
print (" *No escribir groserias, Tenshin-bot es algo sensible\n") #tengo una idea Jordi, si no me sale borramos esta regla
# _____________________________________________________________________________________________________________________________________________________________
# Aleatorio para respuestas distintas y otras variables
import random as rd

rd.randint(0, 1000)
# _____________________________________________________________________________________________________________________________________________________________
# Palabras almacenadas
# _____________________________________________________________________________________________________________________________________________________________

saludos = ["hola", "que más", "buenas", "que tal", "hi bro", "hola que te cuentas?", "holi :3", "holiwis", "habla pués",
           "que hay pana", "que mas mi llave", "aloja",'saludos cordiales','bienvenido']

despedida = ["nos vemos" "pilas bro", "chao", "adios", "hay te ves", "sayonara",'nos vemos', 'cuidate', 'chaito',
             'hasta luego', 'que Zeno-Sama te bendiga', 'cuidate humano', 'bye bye', "sayonara",
             "que Sheng Long guíe tu camino", "que Goku te proteja"]

articulos = ["y", "la", "las", "un", "en", "unos", "unas", "los", "lo", "el", "ellos", "eso", "esas", "esa", "esos",
             "de", "es"]

seguir = ["que tal tu dia", "como te sientes", "a que te dedicas", "que hay de nuevo en tu vida",
          "barcelonista o emelecista", "como te diviertes", "te gusta el anime", "te gustan los videojuegos",
          "que clase de musica escuchas", "te gustan las artes marciales","preguntame lo que desees...",
          "si quieres conversar soy todo oidos, bueno tecnicamente todo binarios ","Cuentame algo interesante",
          "sabes que es Dragon Ball?", "sabes que es un sayayin", "has escuchado sobre la serie Dragon Ball Súper"]

noentiendo = ["No se como contestar, por favor reformula lo escrito", "No te entinedo", ""
              "Sal de ahí Shen Long y dime que lo trata de decirme"]

lista_personajes = ["akira", "bulma", "trunks", "goten", "satán", "satan", "boo", "zeno", "rey", "marron", "bra",
                    "pilaf", "shu", "mai", "yamcha", "rensou", "jaco", "zuno", "milk", "chi", "chi-chi", "videl",
                    "pan", "bee", "kibito", "yurin", "chaoz", "panchy", "brief", "uranai", "enma", "tights"]

lista_universo1 = ["iwen", "awamo", "anat"]

lista_universo2 = ["heles", "sour", "peru", "brianne", "bikal", "harmira", "jimizu", "prum", "rabanra", "sanka", "roas",
                   "zarbuto", "zirloin"]

lista_universo3 = ["mosco", "capahri", "ea", "biarra", "boraleta", "katopesla", "kayo", "nigrissi", "narirama",
                   "preecho", "paparoni", "koitsukai", "pancea", "koichealeta", "koichiarator", "anilaza"]

lista_universo4 = ["quitela", "cognic", "kur", "nink", "ganos", "shousa", "shosa", "majora", "caway", "dercori", "monna",
                   "shantsa", "damom", "gamisalas"]

lista_universo5 = ["arak", "cucatall", "ogma"]

lista_universo6 = ["champa", "vados", "fuwa", "hit", "cabba", "frost", "magetta", "botamo", "caulifla", "kale", "rota",
                   "saonel", "pilina", "kefla"]

lista_universo7 = ["bilss", "beerus", "whis", "shin", "anciano", "antiguo", "gohan", "goku", "vegeta", "piccolo", "17",
                   "18", "krilin", "tenshinhan", "roshi", "kame", "senin", "sen'nin", "freezer"]

lista_universo8 = ["liquir", "korn", "iii"]

lista_universo9 = ["sidra", "mojito", "rou", "bergamo", "lavenda", "basil", "hyssop", "cheppil", "comfrey", "hop",
                   "oregano", "sorrel", "roselle"]

lista_universo10 = ["rumoosh",  "kus", "gowas", "dium", "jirasen", "lilibeu", "rubalt", "methiop", "murichim",
                    "murisarm", "napapa", "obuni", "zircol"]

lista_universo11 = ["vermud", "marcarita", "kai", "jiren", "toppo", "dispo", "casseral", "cocotte", "vuon", "kettle",
                    "tupper", "zoirei", "kunsi"]

lista_universo12 = ["geen", "martinne", "ag"]

lista_destruccion = ["iwen", "heles", "mosco", "quitela", "arak", "champa", "bilss", "beerus", "liquir", "sidra",
                     "rumoosh", "vermud","geen"]

lista_angeles = ["awamo", "sour", "capahri", "cognic", "cucatall", "vados", "whis", "korn", "mojito", "kus",
                 "marcarita", "martinne", "sacerdote"]

# _____________________________________________________________________________________________________________________________________________________________
# Respuestas almacenadas
# _____________________________________________________________________________________________________________________________________________________________


def relacion (pareja):
    if pareja == "novio":
        print("- El amor es algo impropio de mi, por eso o necesito pareja")
    elif pareja == "novia":
        print("- El amor es algo impropio de mi, por eso o necesito pareja")
    else:
            print("- Quisiste decir novio o novia?")


def sabes(personajes):  # JORDI----------------------------
    # personajes
    if personajes == "akira":
        print("- Akira Toriyama es el Mangaka creador del universo de Dragon Ball.... Cuándo sea grande quiero ser "
              "como él :D")
    elif personajes == "bulma":
        print("- Es la creadora del radar del dragón y esposa de Vegeta.")
    elif personajes == "trunks":
        print("- Es el hijo mayor de Vegeta y Bulma.")
    elif personajes == "goten":
        print("- Es el hijo menor de Goku y Milk.")
    elif personajes == "satan":
        print("- Es papá de Videl, campeón mundial de artes marciales y ''heroe de la Tierra''.")
    elif personajes == "satán":
        print("- Es papá de Videl, campeón mundial de artes marciales y ''heroe de la Tierra''.")
    elif personajes == "boo":
        print("- Es una criatura demoniaca que se hizo buena gracias a Mr. Satán.")
    elif personajes == "zeno":
        print("- Es el Rey de Todo, está por encima de todo y de todos, no existe nadie más fuerte que él.")
    elif personajes == "rey":
        print("- Es el Rey de Todo, está por encima de todo y de todos, no existe nadie más fuerte que él.")
    elif personajes == "marron":
        print("- Es la hija de Krilin y Nº18.")
    elif personajes == "bra":
        print("- Es la hija menor de Vegeta y Bulma.")
    elif personajes == "pilaf":
        print("- Es villano que busca las esferas del dragón, vive en casa de Bulma junto a sus secuaces Mai y Shu.")
    elif personajes == "shu":
        print("- Es un secuaz de pilaf, vive en casa de Bulma junto a su colega Mai y su jefe Pilaf.")
    elif personajes == "mai":
        print("- Es una secuaz de pilaf, vive en casa de Bulma junto a su colega Shu y su jefe Pilaf.")
    elif personajes == "yamch":
        print("- Es uno de los Guerreros Z. El debil XD")
    elif personajes == "rensou":
        print("- Es hermano de kaulifla.")
    elif personajes == "jaco":
        print("- Es un patrullero de las Fuerzas Galácticas, amigo de Bulma y Tights.")
    elif personajes == "zuno":
        print("- Es un sabio, y conoce cualquier cosa sobre el Universo 7.")
    elif personajes == "milk":
        print("- Es la esposa de Goku.")
    elif personajes == "chi":
        print("- Es la esposa de Goku.")
    elif personajes == "chi-chi":
        print("- Es la esposa de Goku.")
    elif personajes == "videl":
        print("- Es la hija Mr. Satán y esposa de Goham. Todo indica que es la terricola más fuerte de la Tierra")
    elif personajes == "pan":
        print("- Es la hija de Gohan y Videl, nieta de Mr. Satan, Goku y Milk.")
    elif personajes == "bee":
        print("- Es el perrito de Mr. Satan.")
    elif personajes == "kibito":
        print("- Es asistente y guardaespaldas de Kaio-Shin Shin.")
    elif personajes == "yurin":
        print("- Es una chica experta en hechizos que quería aprender artes marciales en la escuela de Tenshinhan.")
    elif personajes == "chaoz":
        print("- Es el mejor amigo de Tenshinhan.")
    elif personajes == "panchy":
        print("- Es la madre de Bulma, esposa del Dr. Brief.")
    elif personajes == "brief":
        print("- Es el hombre más inteligente de la tierra, padre Bulma y fundadore de la Corporación Cápsula.... Si él"
              " inventó las cápsulas")
    elif personajes == "bra":
        print("- Es la hija menor de Vegeta y Bulma.")
    elif personajes == "uranai":
        print("- Es una bruja XD y adivina, hermada del MAestro Roshi.")
    elif personajes == "enma":
        print("- Es el 'Gerente del Inframundo'.")
    elif personajes == "tights":
        print("- Es la hermana mayor de Bulma y amiga de Jaco.")
    # equipos univeros
    if personajes == "vegeta":
        print("- Es el principe de los sayayines.")
    elif personajes == "goku":
        print("- Es el protector de la tierra y el más fuerte del universo 7.")
    elif personajes == "piccolo":
        print("- Es un namekiano amigo de Goku y también es su niñero.")
    elif personajes == "roshi":
        print("- Es el maestro de Goku y Krilin.")
    elif personajes == "gohan":
        print("- Es el hijo mayor de Goku.")
    elif personajes == "krilin":
        print("- Es el esposo de Nº18 y mejor amigo de Goku.")
    elif personajes == "freezer":
        print("- Es el emperador del mal en el universo 7.")

    elif personajes == "hit":
        print("- Es un asesino del Universo 6 que puede hacer saltos en el tiempo!!!.")


    # dioses de la destruccion y angeles de los 12 universos
    elif personajes == "awamo":
        print("- Es un ángel, guardián y maestro del dios de la destrucción del universo 1.")
    elif personajes == "iwen":
        print("- Es el dios de la destrucción del universo 1.")
    elif personajes == "sour":
        print("- Es un ángel, guardián y maestro del dios de la destrucción del universo 2.")
    elif personajes == "heles":
        print("- Es el dios de la destrucción del universo 2.")
    elif personajes == "capahri":
        print("- Es un ángel, guardián y maestro del dios de la destrucción del universo 3.")
    elif personajes == "mosco":
        print("- Es el dios de la destrucción del universo 3.")
    elif personajes == "cognic":
        print("- Es un ángel, guardián y maestro del dios de la destrucción del universo 4.")
    elif personajes == "quitela":
        print("- Es el dios de la destrucción del universo 4.")
    elif personajes == "cucatail":
        print("- Es un ángel, guardián y maestro del dios de la destrucción del universo 5.")
    elif personajes == "arak":
        print("- Es el dios de la destrucción del universo 5.")
    elif personajes == "vados":
        print("- Es un ángel, guardián y maestro del dios de la destrucción del universo 6.")
    elif personajes == "champa":
        print("- Es el dios de la destrucción del universo 6.")
    elif personajes == "whis":
        print("- Es un ángel, guardián y maestro del dios de la destrucción del universo 7.")
    elif personajes == "bills":
        print("- Es el dios de la destrucción del universo 7.")
    elif personajes == "beerus":
        print("- Es el dios de la destrucción del universo 7.")
    elif personajes == "korn":
        print("- Es un ángel, guardián y maestro del dios de la destrucción del universo 8.")
    elif personajes == "liquir":
        print("- Es el dios de la destrucción del universo 8.")
    elif personajes == "mojito":
        print("- Es un ángel, guardián y maestro del dios de la destrucción del universo 9.")
    elif personajes == "sidra":
        print("- Es el dios de la destrucción del universo 9.")
    elif personajes == "kus":
        print("- Es un ángel, guardián y maestro del dios de la destrucción del universo 10.")
    elif personajes == "rumoosh":
        print("- Es el dios de la destrucción del universo 10.")
    elif personajes == "marcarita":
        print("- Es un ángel, guardián y maestro del dios de la destrucción del universo 11.")
    elif personajes == "vermud":
        print("- Es el dios de la destrucción del universo 11.")
    elif personajes == "martinne":
        print("- Es un ángel, guardián y maestro del dios de la destrucción del universo 12.")
    elif personajes == "geen":
        print("- Es el dios de la destrucción del universo 12.")


def preguntas(directas):  # JORDI----------------------------
    if directas == "padre":
        print("- No tengo padre, ni madre, ni perro que me ladre...  :( \nSoy producto de la inteligencia Artificial, "
              "mis creadores son Jordi Miño, Roberth Cobeña y Byron Rodriguez.")
    elif directas == "nombre":
        print("- ドラゴンボール超 y se pronuncia Doragon Bōru Sūpā.")
    elif directas == "universos":
        print("- Son 12 universos y cada universo tiene un gemelo; Eran 18 pero el Rey de Todo destruyó 6.")
    elif directas == "omniverso":
        print("- Es como se denomida al conjunto de todos los universos y líneas de tiempo.")
    elif directas == "dioses":
        print("- Son mushísismo!!!")
    elif directas == "destruccion":
        print("- Son 12 Hakai-Shin o dioses de la destrucción, uno por cada universo.\nY si cuentas a Toppo serían 13.")
    elif directas == "angeles":
        print("- Son 12 Tenshi o ángeles, uno por cada dios de la destrucción.\nSin contar al Gran Sacerdote.")
    elif directas == "creación":
        print("- Son 4 Kaio-Shin o dioses de la creación por universo pero no son 48.\nSin contar a los Gran Kaio-Sihn.")


def indagacion(estados):
    if estados == "estas":
        print("- Estoy muy bien, y tu?")
    elif estados == "llamo":
        print("- Tu nombre es " + nombre + "...")
    elif estados == "llamas":
        print("- Me llamo Tenshin-Bot")


def interrogantes(contest):
    if contest == "amor":
        print("- Supongo que un sentimiento importante para ti " + nombre)
    elif contest == "paz":
        print("- La pregunta es ¿qué consideras tu como paz?")
    elif contest == "reggaeton":
        print("- El reggaeton es una de las peores cosas que le ha pasado a la humanidad, los incultos llaman música a "
              "eso")
    elif contest == "rock":
        print("- Un genero musica inspirados en los dioses, el universo y lo perfecto, te lo recomiendo, o te faltan "
              "huev...")


# _____________________________________________________________________________________________________________________________________________________________
# Empieza la conversacion
nombre = input("Para empezar escribe tu nombre: ")
fin = 0
pausa = 0
a = input("\nHola " + nombre + "\n")
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
            print(despedida[v] + " " + nombre)
            fin = 1
            break
# ______________________________________________________________________________________________________________________________________________________________
# saludo
    for palabra in saludos:
        if a == palabra:
            v = rd.randint(0, len(saludos) - 1)
            print("- Tenshin bot: " + saludos[v] + " " + nombre)
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
# PREGUNTAS SUELTAS
    for pal in lista:
        if pal == "tienes":
            for pals in lista:
                if pals == 'novio':
                    relacion('novio')
                    band_pregunta = True
                    pausa=0
                    break
                elif pals == "novia":
                    relacion('novia')
                    band_pregunta = True
                    pausa=0
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
                elif (pals == 'reggaeton') or (pals == 'reggeton')or (pals == 'regaeton') or (pals == 'regeton') or \
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
# _________________________________________________________________________________________________________________________________________________________________
# PREGUNTAS SECCION: Personajes DBS  # JORDI----------------------------
    for pal in lista:
        if pal == "conoces":
            for pals in lista:
                for per in lista_personajes:
                    if pal == per:
                        print("No...., porqueee no es real ._. \n")
                        pausa = 1
                        break
        elif pal == "quien":
            for pals in lista:
                for per in lista_personajes:
                    if pals == per:
                        sabes(per)
                        band_pregunta = True
                        pausa = 1
                        break
        elif pal == "quien" or pal == "quién":
            for pals in lista:
                if pals == "padre" or pals == "madre" or pals == "papa" or pals == "papá" or pals == "mama" or pals == \
                        "mamá":
                    preguntas("padre")
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
        else:
            band_pregunta = False

    lista_tmp = []

    if pausa == 1:
        pausa = 0
        a = input()
    else:
        if fin == 0:
            v = rd.randint(0, len(seguir) - 1)
            print(seguir[v] + " " + nombre + " ?")
            a = input("")
        elif not band_pregunta:
            v = rd.randint(0, len(noentiendo) - 1)
            print(noentiendo[v] + " " + nombre)
