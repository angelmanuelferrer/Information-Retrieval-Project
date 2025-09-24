from normalizador_consulta import normalizar_consulta_con_stem, normalizar_consulta_sin_stem
from ejecutar_consulta_booleana import ejecutar_consulta_boolean
def interfaz_principal():
    indices = {
    '1': ('Sin normalización', "indice_sin_norm"),
    '2': ('Normalizado sin stemming', "indice_sin_stem"),
    '3': ('Normalizado con stemming', "indice_con_stem")
    }
    print("Sistema de recuperación de información")
    print("Elige el índice para consultar:")
    for k, v in indices.items():
        print(f"{k}: {v[0]}")
    print("Escribe 'salir' para terminar.")

    while True:
        eleccion = input("Elige un índice (1/2/3): ")
        if eleccion.lower() == 'salir':
            break
        if eleccion not in indices:
            print("Opción inválida.")
            continue
        
        nombre_indice, ix = indices[eleccion]
        print(f"Has elegido: {nombre_indice}")
        
        while True:
            consulta = input(f"Consulta en {nombre_indice} > ")
            if consulta.lower() == 'salir':
                break
            
            if eleccion == '2':
                consulta_norm = normalizar_consulta_sin_stem(consulta)
            elif eleccion == '3':  
                consulta_norm = normalizar_consulta_con_stem(consulta)
            else:
                consulta_norm = consulta  # No normalizar para índice sin procesamiento
            documentos = ejecutar_consulta_boolean(consulta_norm, ix)
            print(f"Documentos encontrados {len(documentos)}:")
            for doc_id in documentos:
                print(doc_id)
            
                


