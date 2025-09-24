from ejecutar_consulta_booleana import ejecutar_consulta_boolean
import nltk
from nltk.metrics import precision, recall
from normalizador_consulta import normalizar_consulta_con_stem, normalizar_consulta_sin_stem

# Diccionario con consultas booleanas
def evaluar_sist_bool_necesidades_info(i):

    consultas = {
        "Porteros": "portero NOT delantero NOT defensa NOT centrocampista",
        "Defensas": "defensa NOT delantero NOT portero NOT centrocampista",
        "Centrocampistas": "centrocampista NOT delantero NOT defensa NOT portero",
        "Delanteros": "delantero NOT defensa NOT portero NOT centrocampista",
        "Argentinos": "argentino",
        "Españoles": "español",
        "Italianos": "italiano",
        "Franceses": "francés",
        "Brasileños": "brasileño",
        "Holandeses": "holandés",
        "Portugueses": "portugués",
        "Capitanes": "capitán",
        "Ganadores_balon_de_oro": "ganar AND balón AND oro",
        "Ganadores_Champions": "ganar AND champions",
        "Ganadores_Mundial": "ganar AND mundial",
        "Internacionales": "internacional",
        "Entrenadores": "entrenador",
        "Exfutbolistas": "exfutbolista OR retiro OR retirado",
        "Ligados_al_Inter_de_Miami": "inter AND miami",
        "De_Fuentealbilla": "fuentealbilla",
        }

    # Diccionario con documentos relevantes
    relevantes = {
        "Porteros": {
            "Gianluigi_Buffon",
            "Iker_Casillas",
            "Manuel_Neuer",
            "Jan_Oblak",
            "Alisson_Becker",
            "Thibaut_Courtois"
        },
        "Defensas": {
            "Carles_Puyol",
            "Franz_Beckenbauer",
            "Gerard_Pique",
            "Dani_Alves",
            "Fabio_Cannavaro",
            "Sergio_Ramos",
            "Virgil_van_Dijk"
        },
        "Centrocampistas": {
            "Luka_Modrić",
            "Kaka",
            "Andres_Iniesta",
            "Xavi_Hernandez",
            "Zinedine_Zidane",
            "Toni_Kroos",
            "Frenkie_de_Jong",
            "Phil_Foden",
            "Pedri",
            "Jude_Bellingham",
            "Eduardo_Camavinga",
            "Bukayo_Saka",
            "Michel_Platini",
            "Paul_Pogba",
            "Thiago_Alcantara",
            "Ángel_Di_Maria",
            "David_Beckham",
            "Kevin_De_Bruyne",
            "Pep_Guardiola",
            "Carlo_Ancelotti",
            "Xabi_Alonso",
            "Diego_Simeone"
        },
        "Delanteros": {
            "Lionel_Messi",
            "Cristiano_Ronaldo",
            "Ronaldinho",
            "Pele",
            "Karim_Benzema",
            "Mohamed_Salah",
            "Robert_Lewandowski",
            "Erling_Haaland",
            "Kylian_Mbappe",
            "Jadon_Sancho",
            "João_Felix",
            "Ansu_Fati",
            "Vinicius_Junior",
            "George_Best",
            "Diego_Maradona",
            "Johan_Cruyff",
            "Sadio_Mane",
            "Raheem_Sterling",
            "Zlatan_Ibrahimović",
            "Gareth_Bale",
            "Julian_Alvarez",
            "Antoine_Griezmann"
        },
        "Argentinos": {
            "Lionel_Messi",
            "Diego_Maradona",
            "Ángel_Di_Maria",
            "Julian_Alvarez",
            "Diego_Simeone"
        },
        "Españoles": {
            "Andres_Iniesta",
            "Xavi_Hernandez",
            "Carles_Puyol",
            "Sergio_Ramos",
            "Iker_Casillas",
            "Gerard_Pique",
            "Pedri",
            "Ansu_Fati",
            "Thiago_Alcantara",
            "Xabi_Alonso",
            "Pep_Guardiola"
        },
        "Italianos": {
            "Gianluigi_Buffon",
            "Fabio_Cannavaro",
            "Carlo_Ancelotti"
        },
        "Franceses": {
            "Zinedine_Zidane",
            "Karim_Benzema",
            "Kylian_Mbappe",
            "Michel_Platini",
            "Paul_Pogba",
            "Eduardo_Camavinga",
            "Antoine_Griezmann"
        },
        "Brasileños": {
            "Ronaldinho",
            "Kaka",
            "Pele",
            "Dani_Alves",
            "Alisson_Becker",
            "Vinicius_Junior"
        },
        "Holandeses": {
            "Johan_Cruyff",
            "Frenkie_de_Jong"
        },
        "Portugueses": {
            "Cristiano_Ronaldo",
            "João_Felix"
        },
        "Capitanes": {
            "Lionel_Messi",
            "Cristiano_Ronaldo",
            "Luka_Modrić",
            "Xavi_Hernandez",
            "Carles_Puyol",
            "Zinedine_Zidane",
            "Franz_Beckenbauer",
            "Pele",
            "Sergio_Ramos",
            "Diego_Maradona",
            "Johan_Cruyff",
            "Michel_Platini",
            "Gianluigi_Buffon",
            "Iker_Casillas",
            "Manuel_Neuer",
            "Gerard_Pique",
            "Fabio_Cannavaro",
            "Diego_Simeone",
            "David_Beckham"
        },
        "Ganadores_balon_de_oro": {
            "Lionel_Messi",
            "Cristiano_Ronaldo",
            "Luka_Modrić",
            "Ronaldinho",
            "Kaka",
            "Michel_Platini",
            "Fabio_Cannavaro",
            "Zinedine_Zidane"
        },
        "Ganadores_Champions": {
            "Lionel_Messi",
            "Cristiano_Ronaldo",
            "Luka_Modrić",
            "Ronaldinho",
            "Kaka",
            "Andres_Iniesta",
            "Xavi_Hernandez",
            "Carles_Puyol",
            "Zinedine_Zidane",
            "Franz_Beckenbauer",
            "Sergio_Ramos",
            "Karim_Benzema",
            "Toni_Kroos",
            "Mohamed_Salah",
            "Virgil_van_Dijk",
            "Robert_Lewandowski",
            "Thibaut_Courtois",
            "Gianluigi_Buffon",
            "Iker_Casillas",
            "Manuel_Neuer",
            "Alisson_Becker",
            "Gerard_Pique",
            "Dani_Alves",
            "Fabio_Cannavaro",
            "Paul_Pogba",
            "Thiago_Alcantara",
            "Ángel_Di_Maria",
            "David_Beckham",
            "Kevin_De_Bruyne",
            "Gareth_Bale",
            "Antoine_Griezmann",
            "Pep_Guardiola",
            "Carlo_Ancelotti",
            "Xabi_Alonso"
        },
        "Ganadores_Mundial": {
            "Ronaldinho",
            "Kaka",
            "Andres_Iniesta",
            "Xavi_Hernandez",
            "Carles_Puyol",
            "Zinedine_Zidane",
            "Franz_Beckenbauer",
            "Pele",
            "Manuel_Neuer",
            "Diego_Maradona",
            "Kylian_Mbappe",
            "Fabio_Cannavaro"
        },
        "Internacionales": {
            "Lionel_Messi",
            "Cristiano_Ronaldo",
            "Luka_Modrić",
            "Ronaldinho",
            "Kaka",
            "Andres_Iniesta",
            "Xavi_Hernandez",
            "Carles_Puyol",
            "Zinedine_Zidane",
            "Franz_Beckenbauer",
            "Pele",
            "Sergio_Ramos",
            "Karim_Benzema",
            "Toni_Kroos",
            "Mohamed_Salah",
            "Virgil_van_Dijk",
            "Robert_Lewandowski",
            "Thibaut_Courtois",
            "Erling_Haaland",
            "Kylian_Mbappe",
            "Jadon_Sancho",
            "Frenkie_de_Jong",
            "João_Felix",
            "Phil_Foden",
            "Pedri",
            "Ansu_Fati",
            "Jude_Bellingham",
            "Vinicius_Junior",
            "Eduardo_Camavinga",
            "Bukayo_Saka",
            "Diego_Maradona",
            "Johan_Cruyff",
            "Michel_Platini",
            "George_Best",
            "Gianluigi_Buffon",
            "Iker_Casillas",
            "Manuel_Neuer",
            "Jan_Oblak",
            "Alisson_Becker",
            "Gerard_Pique",
            "Dani_Alves",
            "Sadio_Mane",
            "Raheem_Sterling",
            "Paul_Pogba",
            "Thiago_Alcantara",
            "Ángel_Di_Maria",
            "David_Beckham",
            "Zlatan_Ibrahimović",
            "Kevin_De_Bruyne",
            "Gareth_Bale",
            "Julian_Alvarez",
            "Antoine_Griezmann",
            "Pep_Guardiola",
            "Carlo_Ancelotti",
            "Xabi_Alonso",
            "Diego_Simeone"
        },
        "Entrenadores": {
            "Xavi_Hernandez",
            "Zinedine_Zidane",
            "Franz_Beckenbauer",
            "Johan_Cruyff",
            "Pep_Guardiola",
            "Carlo_Ancelotti",
            "Diego_Simeone"
        },
        "Exfutbolistas": {
            "Ronaldinho",
            "Kaka",
            "Andres_Iniesta",
            "Xavi_Hernandez",
            "Carles_Puyol",
            "Zinedine_Zidane",
            "Franz_Beckenbauer",
            "Pele",
            "Diego_Maradona",
            "Johan_Cruyff",
            "Michel_Platini",
            "George_Best",
            "Gianluigi_Buffon",
            "Iker_Casillas",
            "Gerard_Pique",
            "Dani_Alves",
            "Fabio_Cannavaro",
            "David_Beckham",
            "Xabi_Alonso",
            "Diego_Simeone"
        },
        "Ligados_al_Inter_de_Miami": {
            "Lionel_Messi",
            "David_Beckham"
        },
        "De_Fuentealbilla": {
            "Andres_Iniesta"
        }
    }

    resultados = {}
    for necesidad, consulta in consultas.items():
        if i == "indice_sin_stem":
            consulta = normalizar_consulta_sin_stem(consulta)
        elif i == "indice_con_stem":
            consulta = normalizar_consulta_con_stem(consulta)
        recuperados = set(ejecutar_consulta_boolean(consulta,i))
        resultados[necesidad] = {
            "recuperados": recuperados,
            "relevantes": relevantes[necesidad],
        }
        
    resultados_metricas = {}
    lista_precision = []
    lista_sensibilidad = []
    
    for necesidad, datos in resultados.items():
        recuperados = datos['recuperados']
        relevantes = datos['relevantes']
    
        prec = precision(relevantes, recuperados)
        rec = recall(relevantes, recuperados)
    
        if prec is None:
            prec = 0.0
        if rec is None:
            rec = 0.0
    
        lista_precision.append(prec)
        lista_sensibilidad.append(rec)
    
    media_precision = sum(lista_precision) / len(lista_precision) if lista_precision else 0
    media_sensibilidad = sum(lista_sensibilidad) / len(lista_sensibilidad) if lista_sensibilidad else 0
    
    return  media_precision, media_sensibilidad

    
def evaluar_todas_booleanas():
    indices = ["indice_sin_norm", "indice_sin_stem", "indice_con_stem"]
    
    for i in indices:
        print(f"Evaluando {i}:\n")
        media_precision, media_sensibilidad = evaluar_sist_bool_necesidades_info(i)
        print(f"Media de Precisión: {media_precision:.4f}")
        print(f"Media de Sensibilidad: {media_sensibilidad:.4f}\n")
        
        
