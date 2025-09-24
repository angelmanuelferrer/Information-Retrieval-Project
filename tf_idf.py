import os
from sklearn.feature_extraction.text import TfidfVectorizer

def crear_matriz_tfidf(carpeta_corpus):
    documentos_normalizados = {}
    for archivo in os.listdir(carpeta_corpus):
        if archivo.endswith(".txt"):
            doc_id = archivo.replace(".txt", "")
            with open(os.path.join(carpeta_corpus, archivo), "r", encoding="utf-8") as f:
                texto = f.read()
            documentos_normalizados[doc_id] = texto

    doc_ids = list(documentos_normalizados.keys())
    corpus = [documentos_normalizados[doc_id] for doc_id in doc_ids]

    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(corpus)

    return vectorizer, tfidf_matrix, doc_ids
