from sklearn.metrics.pairwise import cosine_similarity

def buscar_documentos(consulta, vectorizer, tfidf_matrix, doc_ids):
    # Vectorizamos la consuta
    consulta_tfidf = vectorizer.transform([consulta])
    
    similitudes = cosine_similarity(consulta_tfidf, tfidf_matrix).flatten() # Calculamos la similitud, flatten para pasar a vector
    indices_ordenados = similitudes.argsort()[::-1] # Orden descendente    
    resultados = [(doc_ids[i], similitudes[i]) for i in indices_ordenados if similitudes[i] > 0] #Creamos tupla doc sim
    return resultados


