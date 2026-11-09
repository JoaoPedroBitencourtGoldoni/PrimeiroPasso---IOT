from pathlib import Path
import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
BASE = Path(__file__).resolve().parent.parent
class Retriever:
    def __init__(self, path: Path | None = None):
        self.docs = json.loads((path or BASE / 'knowledge' / 'base.json').read_text(encoding='utf-8'))
        self.vectorizer = TfidfVectorizer(ngram_range=(1,2), strip_accents='unicode', lowercase=True)
        self.matrix = self.vectorizer.fit_transform([d['texto'] for d in self.docs])
    def search(self, query: str, k: int=3, threshold: float=0.035):
        scores=cosine_similarity(self.vectorizer.transform([query]),self.matrix)[0]
        ranked=sorted(enumerate(scores),key=lambda x: x[1],reverse=True)
        return [{**self.docs[i], 'score':round(float(s),4)} for i,s in ranked[:k] if s >= threshold]
retriever = Retriever()
