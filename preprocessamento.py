import re
import unicodedata
import nltk
from nltk.corpus import stopwords
from nltk.tokenize.toktok import ToktokTokenizer

nltk.download('stopwords')
nltk.download('punkt')

tokenizer_nltk = ToktokTokenizer()
stop_words = set(stopwords.words('portuguese')) - {'legal', 'bom', 'ruim', 'excelente', 'horrivel', 'horrível'}

def limpar_texto(texto):
    if not texto:
        return ''
    texto = str(texto)
    texto = unicodedata.normalize('NFKD', texto).encode('ASCII', 'ignore').decode('utf-8')
    texto = texto.lower()
    texto = re.sub(r'[^a-zA-Z\s]', '', texto)
    palavras = tokenizer_nltk.tokenize(texto)
    palavras_filtradas = [p for p in palavras if p not in stop_words and len(p) > 1]
    return ' '.join(palavras_filtradas)
