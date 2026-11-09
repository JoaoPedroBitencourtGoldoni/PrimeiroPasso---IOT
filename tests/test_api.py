from app.main import redact
from app.rag import retriever

def test_health(client):
    r=client.get('/health'); assert r.status_code==200 and r.json()['documentos']>=8

def test_auth(client):
    assert client.get('/api/v1/fontes').status_code==401

def test_sources(client,headers):
    assert len(client.get('/api/v1/fontes',headers=headers).json())>=8

def test_validation(client,headers):
    assert client.post('/api/v1/entrevistas/feedback',headers=headers,json={'area':'TI','pergunta':'curta','resposta':'oi'}).status_code==422

def test_retrieval():
    docs=retriever.search('Como organizar minha resposta em situação tarefa ação resultado STAR?')
    assert docs and docs[0]['id']=='K01'

def test_empty_retrieval():
    assert retriever.search('zzzxqv_123_xyz',threshold=0.1)==[]

def test_redaction():
    result=redact('meu CPF 123.456.789-00 e email teste@exemplo.com')
    assert '123.456' not in result and 'teste@' not in result

def test_question_with_mock_llm(client,headers,monkeypatch):
    async def fake(_): return 'Conte sobre um projeto em equipe. [K02]'
    monkeypatch.setattr('app.main.generate',fake)
    r=client.post('/api/v1/entrevistas/pergunta',headers=headers,json={'area':'administrativa','projeto':'planilha em equipe'})
    assert r.status_code==200 and r.json()['fontes'] and '[K02]' in r.json()['texto']

def test_feedback_with_mock_llm(client,headers,monkeypatch):
    async def fake(_): return 'Descreva suas ações e resultados. [K01]'
    monkeypatch.setattr('app.main.generate',fake)
    r=client.post('/api/v1/entrevistas/feedback',headers=headers,json={'area':'administrativa','pergunta':'Conte sobre trabalho em equipe','resposta':'Organizei as tarefas de um projeto escolar e acompanhei os prazos.'})
    assert r.status_code==200 and r.json()['fontes']

def test_provider_unavailable(client,headers,monkeypatch):
    from fastapi import HTTPException
    async def unavailable(_): raise HTTPException(503,'Modelo indisponível')
    monkeypatch.setattr('app.main.generate',unavailable)
    r=client.post('/api/v1/entrevistas/pergunta',headers=headers,json={'area':'tecnologia'})
    assert r.status_code==503
