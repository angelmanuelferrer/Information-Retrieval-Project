import wikipediaapi
import os

# Este script fue utilizado para la busqueda de las fichas de los jugadores, no es necesario ejecutarlo
# ya que en la entrega del proyecto se especifica que se proporcione el corpus de documentos


def obtener_ficha_jugador(nombre_jugador):
    wiki = wikipediaapi.Wikipedia(user_agent='mi-proyecto-recuperacion-informacion', language='es')#me pedia un user agent
    pagina = wiki.page(nombre_jugador)
    if pagina.exists():
        texto = pagina.text
        palabras = texto.split()
        resumen = ' '.join(palabras[:1000])  # Limita a 1000 palabras
        return resumen
    else:
        return None

jugadores = [
    "Lionel Messi",
    "Cristiano Ronaldo",
    "Luka Modrić",
    "Ronaldinho",
    "Kaká",
    "Andrés Iniesta",
    "Xavi Hernández",
    "Carles Puyol",
    "Zinedine Zidane",
    "Franz Beckenbauer",
    "Pelé",
    "Sergio Ramos",
    "Karim Benzema",
    "Toni Kroos",
    "Mohamed Salah",
    "Virgil van Dijk",
    "Robert Lewandowski",
    "Thibaut Courtois",
    "Erling Haaland",
    "Kylian Mbappé",
    "Jadon Sancho",
    "Frenkie de Jong",
    "João Félix",
    "Phil Foden",
    "Pedri",
    "Ansu Fati",
    "Jude Bellingham",
    "Vinícius Júnior",
    "Eduardo Camavinga",
    "Bukayo Saka",
    "Diego Maradona",
    "Johan Cruyff",
    "Michel Platini",
    "George Best",
    "Gianluigi Buffon",
    "Iker Casillas",
    "Manuel Neuer",
    "Jan Oblak",
    "Alisson Becker",
    "Gerard Piqué",
    "Dani Alves",
    "Fabio Cannavaro",
    "Sadio Mané",
    "Raheem Sterling",
    "Paul Pogba",
    "Thiago Alcántara",
    "Ángel Di María",
    "David Beckham",
    "Zlatan Ibrahimović",
    "Kevin De Bruyne",
    "Gareth Bale",
    "Julián Alvarez",
    "Antoine Griezmann",
    "Pep Guardiola",
    "Carlo Ancelotti",
    "Xabi Alonso",
    "Diego Simeone"
]

corpus = {}

for jugador in jugadores:
    ficha = obtener_ficha_jugador(jugador)
    if ficha:
        corpus[jugador] = ficha

os.makedirs("fichas_jugadores", exist_ok=True)
for jugador, texto in corpus.items():
    nombre_archivo = jugador.replace(" ", "_").replace("á","a").replace("í","i").replace("é","e").replace("ó","o").replace("ú","u") + ".txt"
    with open(os.path.join("fichas_jugadores", nombre_archivo), "w", encoding="utf-8") as f:
        f.write(texto)
