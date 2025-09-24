import os
from whoosh import index
from whoosh.fields import Schema, TEXT, ID

def crear_indice(corpus_dir, indice_dir):
    schema = Schema(
        doc_id=ID(stored=True, unique=True),
        content=TEXT(stored=True)  
    )#definimos el esquema del índice, no tocamos el contenido ya que lo normalizamos antes de crear el índice

    if not os.path.exists(indice_dir):
        os.mkdir(indice_dir)
        ix = index.create_in(indice_dir, schema) 
    else:
        ix = index.open_dir(indice_dir) 

    writer = ix.writer()

    for filename in os.listdir(corpus_dir):
        if filename.endswith(".txt"):
            doc_id = filename.replace(".txt", "")
            with open(os.path.join(corpus_dir, filename), "r", encoding="utf-8") as f:
                text = f.read()
            writer.update_document(doc_id=doc_id, content=text)

    writer.commit() #necesario para guardar y cerrar el índice

