# PrimeiroPasso — EntrevistaLab | Global Solution 2026/2

**FIAP | Disruptive Architectures: IoT, IoB & Generative IA | CitizenTech**

## Propósito
O PrimeiroPasso ajuda jovens e pessoas sem experiência profissional a se preparar para entrevistas. O EntrevistaLab cria perguntas personalizadas e oferece feedback educacional baseado em uma base de conhecimento recuperada por RAG. **Não é plataforma de decisão de contratação.** Conecta-se aos ODS 4, 8 e 10.

## Integrantes
Preencher com RM, nome completo e turma de **todos os integrantes efetivos** antes de entregar. Não usar nomes de outros projetos sem confirmar.

## Funcionalidades
- `POST /api/v1/entrevistas/pergunta`: gera pergunta com LLM real.
- `POST /api/v1/entrevistas/feedback`: gera feedback com LLM real.
- `GET /api/v1/fontes`: lista a base de conhecimento.
- `GET /health`: saúde básica (não verifica disponibilidade do LLM).
- Swagger: `http://localhost:8000/docs`.
- RAG: TF-IDF + similaridade cosseno, top-3, limiar de relevância, referências estruturadas.

## Pré-requisitos
Python 3.11+; para execução local da IA: Ollama instalado e modelo `llama3.2:3b` baixado. Alternativamente API compatível OpenAI e chave própria. **Os testes automatizados não precisam de Ollama nem de chave.**

## Instalação (Windows PowerShell)
```powershell
cd primeiropasso-disruptive
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
Copy-Item .env.example .env
```
Edite `.env`: substitua `INTERNAL_API_KEY` por chave aleatória longa. Nunca commite `.env`.

### Modelo local Ollama (terminal separado)
```bash
ollama pull llama3.2:3b
ollama serve
```
Se o Ollama já estiver rodando, não é necessário executar `ollama serve` novamente.

### API externa (alternativa)
Configure `LLM_PROVIDER=openai`, `OPENAI_API_KEY`, `OPENAI_MODEL` e, se necessário, `OPENAI_BASE_URL` no `.env`. Uma API externa pode gerar custos. Nunca use chaves no aplicativo Mobile.

### Iniciar
```bash
uvicorn app.main:app --reload
```
Abra `http://localhost:8000/docs`. Nos endpoints protegidos, use o header `x-internal-api-key` igual à chave configurada.

### Testes
```bash
pytest -v
pytest -v > evidencias/pytest_resultados.txt
```
Os testes simulam a resposta do LLM e verificam lógica local; execute também os testes manuais com LLM real descritos em `docs/avaliacao.md`.

## Exemplo de chamada (PowerShell)
```powershell
$headers = @{ 'x-internal-api-key' = 'SUA_CHAVE'; 'Content-Type' = 'application/json' }
$body = @{ area='administrativa'; nivel='primeiro_emprego'; projeto='Organizei uma planilha em projeto da faculdade' } | ConvertTo-Json
Invoke-RestMethod -Uri http://localhost:8000/api/v1/entrevistas/pergunta -Method Post -Headers $headers -Body $body

$feedback = @{ area='administrativa'; pergunta='Conte sobre um trabalho em equipe que realizou'; resposta='Organizei tarefas de um projeto escolar e acompanhei prazos.' } | ConvertTo-Json
Invoke-RestMethod -Uri http://localhost:8000/api/v1/entrevistas/feedback -Method Post -Headers $headers -Body $feedback
```

## Arquitetura e escolhas
Veja `docs/arquitetura.md`. Python/FastAPI mantém a IA desacoplada da API Java; TF-IDF é simples, reproduzível e adequado à base pequena, mas é menos robusto que embeddings neurais para paráfrases. O LLM gera texto real via Ollama ou API. Base educativa original em `knowledge/base.json`; não foi coletada de usuários nem contém dados pessoais. Não é necessário IoT físico para os requisitos desta disciplina.

## Integração futura com Java
`integracao-java/EntrevistaLabClient.java` é um **exemplo** de cliente Spring Boot para adaptar. O backend Java deve autenticar usuários via JWT, validar autorização, chamar este serviço via rede privada e guardar a chave em variável de ambiente. **Ainda não existe integração ponta a ponta nem implementação Spring AI neste repositório.** O requisito de Spring AI da disciplina Java deve ser implementado pelo grupo no backend Java.

## Avaliação e uso responsável
`docs/avaliacao.md` define protocolo de avaliação, métricas e falhas. `evidencias/casos_teste.csv` é uma planilha de coleta **em branco** até a execução dos testes manuais. Respostas de IA não substituem recrutadores; não há garantia de emprego. Há risco de alucinação, citações não verificadas, viés e falhas de recuperação. CPF/email/telefone são mascarados por regex parcial, não anonimização completa. Não envie dados reais de terceiros. Em produção: HTTPS, rate limiting, controle de retenção e gestão de segredos.

## Declaração de uso de IA
O desenvolvimento inicial deste projeto foi assistido pelo ChatGPT para estruturação de código, documentação e testes. A equipe deve revisar, executar, compreender e validar cada componente antes de apresentar como trabalho acadêmico.

## Entrega FIAP
GitHub com este projeto, testes executados, evidências reais e README atualizado. No Portal do Aluno, enviar **apenas TXT** com RM, nome completo de todos os integrantes e URL do GitHub. Prazo geral: 19/11/2026 às 23h55 (confirmar com o professor).

## Revisão de segurança e entrega (09/11/2026)
- O arquivo `.env` foi excluído do pacote distribuível. Crie seu próprio `.env` a partir de `.env.example`.
- Chaves previamente compartilhadas em capturas de tela ou em ZIPs devem ser **substituídas**; apenas apagar o arquivo do ZIP não revoga uma chave.
- A autenticação compara credenciais com `secrets.compare_digest`.
- Testes extras verificam rejeição de chave incorreta, mascaramento de CPF/e-mail/telefone e ausência de segredo em `/health`.
- Testes automatizados usam mock do modelo: **não comprovam** a qualidade ou a disponibilidade do Ollama. Faça avaliação manual com modelo real e registre resultados.
- O exemplo Java é demonstrativo e **não comprova integração ponta a ponta**.
- Antes da entrega, preencha `IDENTIFICACAO_MODELO.txt` com todos os integrantes e link real. O Portal FIAP solicita somente esse TXT; o projeto deve estar no GitHub.

## Revisão final rápida
```bash
python -m pytest -v
uvicorn app.main:app --reload
```
Depois valide os endpoints no Swagger com Ollama ativo, documente tempos, pertinência das fontes e possíveis alucinações em `docs/avaliacao.md`.
