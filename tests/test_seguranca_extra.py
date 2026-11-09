from app.main import redact


def test_credencial_incorreta(client):
    response = client.get('/api/v1/fontes', headers={'x-internal-api-key': 'chave-incorreta'})
    assert response.status_code == 401


def test_redacao_telefone_e_dados_sem_formatacao():
    texto = 'Email pessoa@exemplo.com CPF 12345678909 telefone (11) 91234-5678'
    saida = redact(texto)
    assert 'pessoa@exemplo.com' not in saida
    assert '12345678909' not in saida
    assert '91234-5678' not in saida
    assert '[EMAIL]' in saida and '[CPF]' in saida and '[TELEFONE]' in saida


def test_sem_exposicao_de_credencial_no_health(client):
    resultado = client.get('/health')
    assert resultado.status_code == 200
    assert 'internal_key' not in resultado.text
    assert 'teste-chave-local' not in resultado.text
