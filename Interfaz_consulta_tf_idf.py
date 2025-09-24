from consulta_tf_idf import buscar_documentos
from normalizador_consulta import normalizar_consulta_con_stem, normalizar_consulta_sin_stem

def interfaz_consulta_multimodelo(
    vectorizer_sin, tfidf_sin, doc_ids_sin,
    vectorizer_stem, tfidf_stem, doc_ids_stem
):
    print("Sistema de recuperación de información basado en TF-IDF y similitud coseno\n")

    while True:
        print("Elige el sistema de recuperación:")
        print("1 - Sin stemming")
        print("2 - Con stemming")
        print("Escribe 'salir' para terminar.\n")

        eleccion = input("Opción (1/2): ").strip()
        if eleccion.lower() == 'salir':
            print("Saliendo del sistema.")
            break

        if eleccion not in ['1', '2']:
            print("Opción no válida.\n")
            continue

        if eleccion == '1':
            vectorizer, tfidf_matrix, doc_ids = vectorizer_sin, tfidf_sin, doc_ids_sin
            normalizar = False
            print("Has elegido sistema sin stemming.\n")
        else:
            vectorizer, tfidf_matrix, doc_ids = vectorizer_stem, tfidf_stem, doc_ids_stem
            normalizar = True
            print("Has elegido sistema con stemming.\n")

        while True:
            consulta = input("Consulta> ").strip()
            if consulta.lower() == 'salir':
                break
            if not consulta:
                print("Por favor, ingresa una consulta válida.")
                continue

            if normalizar:
                consulta = normalizar_consulta_con_stem(consulta)
            else:
                consulta = normalizar_consulta_sin_stem(consulta)

            resultados = buscar_documentos(consulta, vectorizer, tfidf_matrix, doc_ids)

            if not resultados:
                print("No se encontraron documentos relevantes para esa consulta.\n")
                continue

            print(f"\nResultados encontrados ({len(resultados)} documentos relevantes):")
            for i, (doc_id, score) in enumerate(resultados[:10], 1):
                print(f"{i}. Documento: {doc_id} - Similitud: {score:.4f}")
            print("\n")
