from flask import Flask, request, jsonify
from preprocessamento import limpar_texto
from modelo import analisar_sentimento

app = Flask(__name__)

# 🔸 Endpoint para análise de sentimento de um único comentário
@app.route('/sentimento', methods=['POST'])
def sentimento():
    data = request.get_json()

    # Verificação dos campos obrigatórios
    campos_necessarios = {'id_comentario', 'comentario', 'id_livro', 'id_usuario'}
    if not data or not campos_necessarios.issubset(data):
        return jsonify({'error': f'O JSON precisa conter os campos: {", ".join(campos_necessarios)}'}), 400

    comentario = data['comentario']
    texto_limpo = limpar_texto(comentario)
    sentimento = analisar_sentimento(texto_limpo)

    resultado = {
        'id_comentario': data['id_comentario'],
        'id_livro': data['id_livro'],
        'id_usuario': data['id_usuario'],
        'comentario_original': comentario,
        'comentario_limpo': texto_limpo,
        'sentimento': sentimento
    }

    return jsonify(resultado)

    # 🔸 Endpoint para vários comentários
@app.route('/sentimento/lote', methods=['POST'])
def sentimento_lote():
    dados = request.get_json()

    if not isinstance(dados, list):
        return jsonify({'error': 'Envie uma lista de objetos JSON.'}), 400

    resultados = []

    for item in dados:
        campos_necessarios = {'id_comentario', 'comentario', 'id_livro', 'id_usuario'}
        if not campos_necessarios.issubset(item):
            resultados.append({
                'id_comentario': item.get('id_comentario', None),
                'error': f'Campos obrigatórios faltando: {", ".join(campos_necessarios)}'
            })
            continue

        comentario = item['comentario']
        texto_limpo = limpar_texto(comentario)
        sentimento = analisar_sentimento(texto_limpo)

        resultados.append({
            'id_comentario': item['id_comentario'],
            'id_livro': item['id_livro'],
            'id_usuario': item['id_usuario'],
            'comentario_original': comentario,
            'comentario_limpo': texto_limpo,
            'sentimento': sentimento
        })

    return jsonify(resultados)


if __name__ == '__main__':
    app.run(debug=True)
