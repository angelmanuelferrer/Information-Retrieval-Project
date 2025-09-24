from whoosh.qparser import QueryParser
from whoosh.index import open_dir

def ejecutar_consulta_boolean(consulta_norm, indice):
    ix = open_dir(indice)
    parser = QueryParser("content", schema=ix.schema)
    with ix.searcher() as searcher: # Abrimos el buscador del índice
        query = parser.parse(consulta_norm) # Para entender la consulta (los operadores booleanos)
        results = searcher.search(query, limit=None) 
        documentos = set()
        for r in results:
            documentos.add(r['doc_id'])  # Agrega el nombre/id del documento al set
    return documentos    