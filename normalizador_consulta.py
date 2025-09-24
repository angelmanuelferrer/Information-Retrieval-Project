from normalizador_textos import normalizar_texto_con_stem, normalizar_texto_sin_stem
def normalizar_consulta_con_stem(consulta):
    operadores = {'AND', 'OR', 'NOT'}
    tokens = consulta.split()
    tokens_normalizados = []
    for token in tokens:
        if token.upper() in operadores:
            # Los operadores no hay que normalizarlos
            tokens_normalizados.append(token.upper())
        else:
            norm = normalizar_texto_con_stem(token)
            tokens_normalizados.append(norm)

    # Reconstruir la consulta normalizada
    consulta_norm = ' '.join(tokens_normalizados)
    consulta_norm = ' '.join(consulta_norm.split()) #A veces al normalizar se generan espacios extra al quitar las stopwords
    return consulta_norm

def normalizar_consulta_sin_stem(consulta):
    operadores = {'AND', 'OR', 'NOT'}
    tokens = consulta.split()
    tokens_normalizados = []
    for token in tokens:
        if token.upper() in operadores:
            tokens_normalizados.append(token.upper())
        else:
            norm = normalizar_texto_sin_stem(token)
            tokens_normalizados.append(norm)
            
    consulta_norm = ' '.join(tokens_normalizados)
    consulta_norm = ' '.join(consulta_norm.split())

    return consulta_norm
