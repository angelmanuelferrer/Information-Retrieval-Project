import os
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer

def descargar_recursos(): # para utilizar en main
    nltk.download('punkt')
    nltk.download('stopwords')

stop_words = stopwords.words('spanish')
stemmer = SnowballStemmer('spanish')



def normalizar_texto_con_stem(texto):
    tokens = word_tokenize(texto.lower(), language='spanish')
    tokens = [t for t in tokens if t.isalpha() and t not in stop_words]
    stems = [stemmer.stem(t) for t in tokens]
    return " ".join(stems)

def normalizar_texto_sin_stem(texto):
    tokens = word_tokenize(texto.lower(), language='spanish')
    tokens = [t for t in tokens if t.isalpha() and t not in stop_words]
    return " ".join(tokens)

def normalizar_corpus(carpeta_entrada, carpeta_salida_sin_stem, carpeta_salida_con_stem):
    documentos_sin_stem = {}
    documentos_con_stem = {}

    for archivo in os.listdir(carpeta_entrada): 
        if archivo.endswith(".txt"):
            with open(os.path.join(carpeta_entrada, archivo), "r", encoding="utf-8") as f:
                texto = f.read()

            texto_sin_stem = normalizar_texto_sin_stem(texto)
            texto_con_stem = normalizar_texto_con_stem(texto)

            doc_id = archivo.replace(".txt", "")
            documentos_sin_stem[doc_id] = texto_sin_stem
            documentos_con_stem[doc_id] = texto_con_stem

    os.makedirs(carpeta_salida_sin_stem, exist_ok=True)
    os.makedirs(carpeta_salida_con_stem, exist_ok=True)

    for doc_id in documentos_sin_stem:
        with open(os.path.join(carpeta_salida_sin_stem, f"{doc_id}.txt"), "w", encoding="utf-8") as f:
            f.write(documentos_sin_stem[doc_id])
        with open(os.path.join(carpeta_salida_con_stem, f"{doc_id}.txt"), "w", encoding="utf-8") as f:
            f.write(documentos_con_stem[doc_id])


    return documentos_sin_stem, documentos_con_stem
