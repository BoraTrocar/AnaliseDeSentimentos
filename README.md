# AnaliseDeSentimentos🚀 API de Análise de Sentimentos de Comentários
API REST para realizar análise de sentimentos em comentários de livros utilizando modelos da Hugging Face (nlptown/bert-base-multilingual-uncased-sentiment). A API permite processar um único comentário ou vários comentários em lote.

📦 Tecnologias utilizadas

🔸 Python 🐍

🔸 Flask 🌐

🔸 Transformers (Hugging Face) 🤗

🔸 Pandas

🔸 NLTK (Natural Language Toolkit)

🔧 Instalação
1️⃣ Clone o repositório:
```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```
2️⃣ Crie um ambiente virtual (opcional, mas recomendado):
```bash
python -m venv venv
# No Windows
venv\Scripts\activate
# No Linux/Mac
source venv/bin/activate
```
3️⃣ Instale as dependências:
```bash
pip install -r requirements.txt
```
4️⃣ Execute a aplicação:
```bash
python app.py
```
O servidor será iniciado em:

```cpp
http://127.0.0.1:5000
```
🚀 Endpoints disponíveis
🔹 Analisar um único comentário
POST /sentimento

✔️ JSON de entrada:
```json
{
    "id_comentario": 1,
    "comentario": "Esse livro é sensacional!",
    "id_livro": 3,
    "id_usuario": 4
}
```
📤 JSON de saída:
```json
{
    "id_comentario": 1,
    "id_livro": 3,
    "id_usuario": 4,
    "comentario_original": "Esse livro é sensacional!",
    "comentario_limpo": "livro sensacional",
    "sentimento": "Positivo"
}
```
🔸 Analisar vários comentários (lote)
POST /sentimento/lote

✔️ JSON de entrada (lista):
```json
[
    {
        "id_comentario": 1,
        "comentario": "Gostei muito desse livro!",
        "id_livro": 3,
        "id_usuario": 4
    },
    {
        "id_comentario": 2,
        "comentario": "Achei meio chato e confuso.",
        "id_livro": 4,
        "id_usuario": 5
    }
]
```
📤 JSON de saída:
```json
[
    {
        "id_comentario": 1,
        "id_livro": 3,
        "id_usuario": 4,
        "comentario_original": "Gostei muito desse livro!",
        "comentario_limpo": "gostei livro",
        "sentimento": "Positivo"
    },
    {
        "id_comentario": 2,
        "id_livro": 4,
        "id_usuario": 5,
        "comentario_original": "Achei meio chato e confuso.",
        "comentario_limpo": "achei meio chato confuso",
        "sentimento": "Negativo"
    }
]
```
🔥 Como testar a API
Você pode testar a API utilizando ferramentas como:

🔸Postman

🔸Insomnia

Ou via terminal usando curl:

```bash
curl -X POST http://127.0.0.1:5000/sentimento \
-H "Content-Type: application/json" \
-d "{\"id_comentario\": 1, \"comentario\": \"Adorei esse livro!\", \"id_livro\": 3, \"id_usuario\": 4}
```