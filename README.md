# ⚽ GoSoccer

GoSoccer is an **Information Retrieval (IR) project** designed to build, test, and evaluate retrieval systems applied to a textual corpus of football players' profiles.  

The project implements and compares two retrieval models:  
- **Boolean retrieval model** (based on logical operators).  
- **Vector space model** using **TF-IDF weighting** and **cosine similarity**.  

This setup allows us to evaluate how text normalization techniques (such as tokenization, stopword removal, and stemming) impact the **precision**, **recall**, and overall performance of the system.

---

## 📚 Features

- **Corpus:** Football player profiles extracted via the Wikipedia API.  
- **Query types:**
  - Boolean queries (AND, OR, NOT).  
  - Free-text queries (TF-IDF + cosine similarity).  
- **Preprocessing techniques:**
  - Tokenization.  
  - Stopword removal.  
  - Stemming (SnowballStemmer – NLTK).  
- **Evaluation:**
  - Precision & Recall for Boolean model.  
  - Average Precision (AP) and Mean Average Precision (MAP) for TF-IDF model.  

---

## 🛠️ Technologies Used

- **Python 3**  
- [NLTK](https://www.nltk.org/) – Text processing (tokenization, stopwords, stemming, metrics).  
- [Whoosh](https://whoosh.readthedocs.io/en/latest/) – Inverted index and Boolean search.  
- [scikit-learn](https://scikit-learn.org/) – TF-IDF vectorization, cosine similarity, evaluation metrics.  
- Standard Python library: `os`.  

---

## 📊 Results

- **Boolean model:**  
  - Stopword removal improves efficiency (smaller indexes, faster queries).  
  - Stemming increases recall but reduces precision due to false positives.  

- **TF-IDF model:**  
  - Achieved **MAP of 0.8059** with stemming vs **0.7933** without stemming.  
  - Outperformed Boolean retrieval in ranking relevant documents.  

---

## 📂 Project Structure

- `main.py` – Entry point with interactive menu.  
- `normalizador_textos.py` – Text preprocessing (with and without stemming).  
- `interfaz_consultas_booleanas.py` – Boolean queries.  
- `interfaz_consulta_tf_idf.py` – Free-text queries with TF-IDF.  
- `evaluar_sist_bool.py` – Boolean model evaluation.  
- `evaluar_sist_tf_idf.py` – TF-IDF model evaluation.  

---

## ▶️ How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/GoSoccer.git
   cd GoSoccer
