from transformers import pipeline

print("Carregando modelo de análise de sentimentos...")
sentiment_pipeline = pipeline("sentiment-analysis", model="nlptown/bert-base-multilingual-uncased-sentiment")

def interpretar_sentimento(resultado):
    label = resultado['label']
    if '1' in label or '2' in label:
        return 'Negativo'
    elif '3' in label:
        return 'Neutro'
    else:
        return 'Positivo'

def analisar_sentimento(texto):
    try:
        resultado = sentiment_pipeline(texto)[0]
        return interpretar_sentimento(resultado)
    except Exception as e:
        print(f"Erro ao analisar: {texto} -> {e}")
        return 'Erro'
