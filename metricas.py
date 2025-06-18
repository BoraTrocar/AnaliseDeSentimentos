from transformers import pipeline
from sklearn.metrics import classification_report, confusion_matrix, ConfusionMatrixDisplay

# Carregar pipeline
classifier = pipeline("sentiment-analysis", model="nlptown/bert-base-multilingual-uncased-sentiment")

texts = [
    # Positivos (20)
    "Amei o livro, recomendo muito!",
    "Produto excelente, superou minhas expectativas",
    "Ótima qualidade, vale cada centavo",
    "Serviço impecável, muito satisfeito",
    "Adorei a experiência, sem defeitos",
    "Maravilhoso, compraria novamente",
    "Incrível, melhor do que eu esperava",
    "Perfeito para minhas necessidades",
    "Fantástico, uso todo dia com prazer",
    "Impressionante, não tenho críticas",
    "Top de linha, desempenho excepcional",
    "Encantado com a aquisição",
    "Simplesmente perfeito",
    "Recomendo sem dúvidas",
    "Surpreendentemente bom",
    "Vale muito a pena",
    "Qualidade premium",
    "Superou todos os elogios",
    "Nota 10, excelente",
    "Melhor compra do ano",
    
    # Negativos (20)
    "O produto é horrível",
    "Péssima qualidade, não recomendo",
    "Terrível, nunca mais compro",
    "Horrível, dinheiro jogado fora",
    "Muito ruim, arrependimento total",
    "Fraco, não cumpre o prometido",
    "Decepcionante em todos os aspectos",
    "Lixo completo, evitem",
    "Vergonhoso, qualidade inferior",
    "Pior experiência que já tive",
    "Nunca mais, produto defeituoso",
    "Horroroso, não funciona direito",
    "Estelionato, não compre",
    "Lamentável, desperdício de dinheiro",
    "Terrível, me arrependi amargamente",
    "Péssimo atendimento ao cliente",
    "Fraude, produto não corresponde",
    "Inaceitável, qualidade péssima",
    "Devolvi imediatamente",
    "Totalmente insatisfeito",
    
    # Neutros (10)
    "Gostei, mas poderia ser melhor",
    "Bom, porém tem seus defeitos",
    "Não é ruim, mas também não é excelente",
    "Aceitável, cumpre o básico",
    "Regular, nem bom nem ruim",
    "Mediano, atendiu minimamente",
    "Esperava mais, mas serve",
    "Nem amei nem odiei",
    "Bom custo-benefício",
    "Na média, sem grandes surpresas"
]

y_true = (
    ["positivo"] * 20 + 
    ["negativo"] * 20 + 
    ["neutro"] * 10
)

# Previsões
y_pred = [res['label'] for res in classifier(texts)]

# Relatório de métricas
print(classification_report(y_true, y_pred))

# Matriz de confusão
cm = confusion_matrix(y_true, y_pred, labels=["positivo", "neutro", "negativo"])
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=["positivo", "neutro", "negativo"])
disp.plot()
