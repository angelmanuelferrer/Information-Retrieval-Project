from Interfaz_consultas_booleanas import interfaz_principal
from normalizador_textos import descargar_recursos, normalizar_corpus
from tf_idf import crear_matriz_tfidf
from Interfaz_consulta_tf_idf import interfaz_consulta_multimodelo
from indice_invertido import crear_indice
from evaluar_sist_bool_necesidades_info import evaluar_todas_booleanas
from evaluar_sist_tf_idf import evaluar_sist_tf_idf

def main():
    # Descarga recursos
    descargar_recursos()

    # Obtenemos los corpus normalizados
    documentos_sin_stem, documentos_con_stem = normalizar_corpus(
        "fichas_jugadores",
        "corpus_normalizado_sin_stem",
        "corpus_normalizado_con_stem"
    )
    
    # Creamos todos los índices
    crear_indice("fichas_jugadores", "indice_sin_norm")
    crear_indice("corpus_normalizado_con_stem", "indice_con_stem")
    crear_indice("corpus_normalizado_sin_stem", "indice_sin_stem")

    
    # Creamos las matrices tf-idf    
    vectorizer_sin_stem, tfidf_sin_stem, doc_ids_sin_stem = crear_matriz_tfidf("corpus_normalizado_sin_stem")
    vectorizer_con_stem, tfidf_con_stem, doc_ids_con_stem = crear_matriz_tfidf("corpus_normalizado_con_stem")
    
    while True:
        print("Elige el sistema de recuperación:")
        print("1 - Modelo booleano")
        print("2 - Modelo tf-idf y similitud del coseno")
        print("3 - Evaluar sistemas booleanos")
        print("4 - Evaluar sistemas tf-idf")
        print("Escribe 'salir' para terminar.\n")
        eleccion = input("Opción (1/2/3/4): ").strip()
        if eleccion.lower() == 'salir':
            print("Saliendo del sistema.")
            break

        if eleccion not in ['1', '2', '3', '4']:
            print("Opción no válida.\n")
            continue

        if eleccion == '1': # para cada eleccion nos vamos a sus respectivas interfaces
            interfaz_principal()
            print("Has elegido sistema con modelo booleano.\n")
        elif( eleccion == '2'):
            interfaz_consulta_multimodelo(
            vectorizer_sin_stem, tfidf_sin_stem, doc_ids_sin_stem, vectorizer_con_stem, tfidf_con_stem, doc_ids_con_stem)
            print("Has elegido sistema con modelo tf-idf y la similitud del coseno.\n")
        elif eleccion == '3':
            print("Evaluando sistemas booleanos.\n")
            evaluar_todas_booleanas()
        else:
            print("Evaluando sistemas tf-idf.\n")
            evaluar_sist_tf_idf(
                vectorizer_sin_stem, tfidf_sin_stem, doc_ids_sin_stem,
                vectorizer_con_stem, tfidf_con_stem, doc_ids_con_stem
            )
main()
