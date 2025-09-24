from consulta_tf_idf import buscar_documentos
from normalizador_consulta import normalizar_consulta_con_stem, normalizar_consulta_sin_stem
from sklearn.metrics import average_precision_score

def evaluar_sist_tf_idf(vectorizer_sin, tfidf_sin, doc_ids_sin,
    vectorizer_stem, tfidf_stem, doc_ids_stem):
    consultas = {
        "Porteros": "portero",
        "Defensas": "defensa",
        "Centrocampistas": "centrocampista",
        "Delanteros": "delantero",
        "Argentinos": "argentino",
        "Españoles": "español",
        "Italianos": "italiano",
        "Franceses": "francés",
        "Brasileños": "brasileño",
        "Holandeses": "holandés",
        "Portugueses": "portugués",
        "Capitanes": "capitán",
        "Ganadores_balon_de_oro": "ganador de balón de oro",
        "Ganadores_Champions": "ganador de champions",
        "Ganadores_Mundial": "ganador de mundial",
        "Internacionales": "internacional",
        "Entrenadores": "entrenador",
        "Exfutbolistas": "exfutbolista",
        "Ligados_al_Inter_de_Miami": "inter de miami",
        "De_Fuentealbilla": "fuentealbilla",
        }
    
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
    resultados_stem = {}
    resultados_sin_stem = {}
    recuperados_stem = set()
    recuperados_sin_stem = set()
    for necesidad, consulta in consultas.items():
        consulta_sin_stem = normalizar_consulta_sin_stem(consulta)
        consulta_con_stem = normalizar_consulta_con_stem(consulta)
        # los buscar_documentos devuelven una lista de tuplas (doc_id, similitud)
        recuperados_sin_stem = buscar_documentos(consulta_sin_stem, vectorizer_sin, tfidf_sin, doc_ids_sin)
        recuperados_stem = buscar_documentos(consulta_con_stem, vectorizer_stem, tfidf_stem, doc_ids_stem)
        resultados_stem[necesidad] = {
            "recuperados": recuperados_stem,
            "relevantes": relevantes[necesidad],
        }
        resultados_sin_stem[necesidad] = {
            "recuperados": recuperados_sin_stem,
            "relevantes": relevantes[necesidad],
        }
    map_stem = mean_average_precision(resultados_stem, relevantes)
    map_sin_stem = mean_average_precision(resultados_sin_stem, relevantes)
    print(f"MAP con stemming: {map_stem:.4f}")
    print(f"MAP sin stemming: {map_sin_stem:.4f}\n")        

def average_precision(relevantes, recuperados): # consideramos los 20 primeros doc, lo recomienda el libro
    y_true = []
    y_scores = []
    coincidencia = False
    if len(recuperados) != 0:
        for doc_id, sim in recuperados[:20] : # era una tupla por eso sacamos doc y sim
            if  doc_id in relevantes:
                y_true.append(1)
                coincidencia = True
            else:
                y_true.append(0) 
            y_scores.append(sim)
        if coincidencia:
            ap = average_precision_score(y_true, y_scores)
        else:
            ap = 0.0
    else:
        ap = 0.0
    return ap

def mean_average_precision(resultados, relevantes):
    map_scores = []

    for necesidad, datos in resultados.items():
        recuperados = datos['recuperados']  # es una tupla (doc_id, similitud)
        relevantes_necesidad = relevantes[necesidad] 
        ap = average_precision(relevantes_necesidad, recuperados)
        map_scores.append(ap)
    
    return sum(map_scores) / len(map_scores) if map_scores else 0.0
