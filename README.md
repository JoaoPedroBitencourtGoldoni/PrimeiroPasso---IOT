# PrimeiroPasso — EntrevistaLab
### Global Solution 2026/2 | FIAP

**Disciplina:** Disruptive Architectures: IoT, IoB & Generative IA  
**Tema:** CitizenTech — Tecnologia para inclusão e cidadania  
**Tecnologias:** Python • FastAPI • Ollama • Llama 3.2 • RAG • Scikit-learn • Pytest

---

## Sobre o projeto

O **PrimeiroPasso — EntrevistaLab** é uma solução educacional que utiliza inteligência artificial generativa e Retrieval-Augmented Generation (RAG) para ajudar jovens e pessoas sem experiência profissional a se prepararem para entrevistas de emprego.

A aplicação gera perguntas personalizadas conforme a área de interesse e oferece feedback educativo sobre as respostas dos candidatos, utilizando documentos de orientação profissional como base de conhecimento.

A proposta está alinhada aos Objetivos de Desenvolvimento Sustentável:

- **ODS 4:** Educação de Qualidade.
- **ODS 8:** Trabalho Decente e Crescimento Econômico.
- **ODS 10:** Redução das Desigualdades.

> O PrimeiroPasso é uma ferramenta de preparação profissional, não uma plataforma de seleção ou decisão de contratação.

## Integrantes

| RM | Nome completo | Turma |
|---|---|---|
| 563512 | Felipe Maglio Filho | 2TDSPF |
| 564339 | João Pedro Bitencourt Goldoni | 2TDSPX |
| 561786 | Marina Tamagnini Magalhães | 2TDSPX |
| 564930 | Mateus Granja dos Santos | 2TDSPF |
| 563509 | Vitória Valentina Maglio | 2TDSPX |

## Funcionalidades

- Geração de perguntas personalizadas utilizando LLM real.
- Feedback educativo com sugestões de melhoria.
- Recuperação de informações por RAG.
- Referências estruturadas das fontes utilizadas.
- API REST documentada com Swagger.
- Autenticação interna por chave de API.
- Mascaramento parcial de dados pessoais.
- Testes automatizados de funcionalidades, validação e segurança.
- Execução local sem necessidade de serviços pagos.

### Endpoints

| Método | Endpoint | Descrição |
|---|---|---|
| GET | `/health` | Verifica a disponibilidade básica da API |
| GET | `/api/v1/fontes` | Consulta a base de conhecimento |
| POST | `/api/v1/entrevistas/pergunta` | Gera perguntas com IA |
| POST | `/api/v1/entrevistas/feedback` | Gera feedback personalizado |

Documentação interativa: http://localhost:8000/docs

## Arquitetura da solução

O projeto utiliza uma arquitetura modular:

**Usuário / Swagger → FastAPI → Recuperador RAG → Llama 3.2 via Ollama → Resposta com referências**

### Componentes

**FastAPI:** disponibiliza os endpoints REST, valida as requisições e controla o acesso aos recursos protegidos.

**Ollama:** executa localmente o modelo `llama3.2:3b`, responsável pela geração das perguntas e dos feedbacks.

**RAG:** recupera documentos relevantes da base educativa antes da geração da resposta.

**Scikit-learn:** implementa a representação TF-IDF e a similaridade cosseno.

**Pytest:** executa testes automatizados de API, validação, privacidade e tratamento de erros.

### Funcionamento do RAG

O mecanismo utiliza:

1. Base de conhecimento educativa em `knowledge/base.json`.
2. Vetorização textual por TF-IDF.
3. Cálculo de similaridade cosseno.
4. Recuperação dos três documentos mais relevantes.
5. Aplicação de limiar mínimo de relevância.
6. Inclusão do contexto recuperado na geração da resposta.
7. Retorno de referências estruturadas ao usuário.

O TF-IDF foi escolhido por ser simples, interpretável, reproduzível e adequado ao tamanho reduzido da base de conhecimento.

Como limitação, a recuperação lexical pode apresentar dificuldades com sinônimos e paráfrases. Uma evolução possível é utilizar embeddings semânticos e busca vetorial.

Mais informações: `docs/arquitetura.md`.

## Como executar

### Pré-requisitos

- Python 3.11 ou superior.
- Ollama instalado.
- Modelo `llama3.2:3b`.
- Dependências Python descritas em `requirements.txt`.

### 1. Preparar o ambiente

No terminal do VS Code, dentro da pasta principal do projeto:

```bash
python -m pip install -r requirements.txt
```

Para um ambiente isolado, recomenda-se criar e ativar um ambiente virtual antes da instalação.

### 2. Configurar variáveis de ambiente

Copie `.env.example` para um novo arquivo `.env` e ajuste as variáveis conforme as opções reconhecidas pela aplicação.

Configure o provedor Ollama, o endereço local do serviço, o modelo `llama3.2:3b` e uma chave interna aleatória e forte.

**Nunca publique o arquivo `.env`, credenciais ou dados pessoais reais no GitHub.**

### 3. Preparar o Ollama

```bash
ollama pull llama3.2:3b
```

Se necessário, inicie o serviço:

```bash
ollama serve
```

Caso o Ollama já esteja em execução, não é necessário iniciar uma segunda instância.

### 4. Iniciar a API

```bash
python -m uvicorn app.main:app --reload
```

Acesse:

http://127.0.0.1:8000/docs

Nos endpoints protegidos, informe o header `x-internal-api-key` com o valor configurado na aplicação.

## Testes e validação

A solução foi submetida a testes automatizados e a testes manuais utilizando o modelo Llama 3.2 em execução local.

### Resultados comprovados

| Validação | Resultado |
|---|---|
| Testes automatizados com Pytest | 14/14 aprovados |
| Avaliação automatizada do recuperador RAG | 2/2 casos aprovados |
| Inicialização da API FastAPI | Concluída |
| Execução local do modelo Llama 3.2 | Confirmada |
| Geração de perguntas via API | HTTP 200 |
| Geração de feedback via API | HTTP 200 |
| Recuperação de fontes nas respostas | Confirmada nos dois testes manuais |

Os testes automatizados utilizam simulações do LLM em determinados cenários. A geração real foi verificada separadamente com Ollama, por meio do Swagger.

### Executar testes automatizados

```bash
python -m pytest -v
```

Para registrar os resultados:

```bash
python -m pytest -v > evidencias/pytest_resultados.txt
```

### Avaliar a recuperação RAG

```bash
python -m scripts.avaliar_rag
```

O comando gera o relatório:

`evidencias/resultado_rag.json`

Esse relatório avalia a recuperação de informações, não a qualidade global das respostas do LLM.

### Evidências

A pasta `evidencias/` contém arquivos de apoio à validação, incluindo:

- `teste_perguntas_ollama_http200.png` — execução real da geração de perguntas.
- `teste_feedback_ollama_http200.png` — execução real do feedback.
- `resultado_rag.json` — avaliação automatizada da recuperação.
- `consultas_rag.csv` — consultas para análise do RAG.
- `casos_teste.csv` — cenários para avaliação manual.
- `pytest_resultados.txt` — resultados dos testes automatizados, quando gerado.

As evidências demonstram o funcionamento dos endpoints e a recuperação de referências. Elas não substituem uma avaliação sistemática de precisão, fidelidade, viés e qualidade pedagógica das respostas.

O protocolo de avaliação está descrito em `docs/avaliacao.md`.

## Segurança e uso responsável

O projeto adota medidas básicas de segurança e privacidade:

- Proteção de endpoints por chave interna.
- Comparação segura de credenciais.
- Mascaramento parcial de CPF, e-mail e telefone.
- Validação das entradas recebidas.
- Tratamento de indisponibilidade do provedor LLM.
- Separação de configurações sensíveis por variáveis de ambiente.

O mascaramento por expressões regulares não garante anonimização completa.

A solução também possui limitações inerentes à IA generativa, incluindo possíveis alucinações, vieses, referências inadequadas e respostas imprecisas.

As recomendações são exclusivamente educativas. A aplicação não substitui profissionais de recrutamento e não toma decisões de contratação.

Em um ambiente de produção, seriam necessários controles adicionais, como HTTPS, limitação de requisições, políticas de retenção e gerenciamento seguro de segredos.

## Integração futura com Java

O PrimeiroPasso foi desenvolvido como um serviço independente de inteligência artificial.

A API Python, o recuperador RAG e o modelo Llama 3.2 podem ser executados e demonstrados diretamente pelo Swagger, sem dependência de Java.

O diretório `integracao-java/` contém um exemplo de cliente para futura integração com um backend Spring Boot.

**A integração ponta a ponta com Java ainda não foi implementada.**

A arquitetura permite uma integração futura, mantendo o serviço de IA desacoplado da aplicação principal.

Detalhes: `docs/plano_integracao.md`.

## Documentação complementar

| Documento | Conteúdo |
|---|---|
| `docs/arquitetura.md` | Arquitetura e decisões técnicas |
| `docs/avaliacao.md` | Metodologia de avaliação e métricas |
| `docs/plano_integracao.md` | Planejamento de integração futura |
| `docs/roteiro_apresentacao.md` | Roteiro para apresentação presencial |
| `knowledge/base.json` | Base de conhecimento educativa |

## Melhorias futuras

- Ampliação e revisão da base de conhecimento.
- Avaliação com um conjunto maior de perguntas.
- Recuperação semântica por embeddings.
- Medição sistemática de latência e qualidade.
- Interface web para simulação de entrevistas.
- Histórico de evolução do candidato com consentimento.
- Integração futura com backend Java.
- Fortalecimento dos controles de segurança e observabilidade.

## Entrega acadêmica

**Instituição:** FIAP  
**Global Solution:** 2026/2  
**Disciplina:** Disruptive Architectures: IoT, IoB & Generative IA

Repositório oficial:

https://github.com/JoaoPedroBitencourtGoldoni/PrimeiroPasso---IOT

A entrega contempla código-fonte, documentação técnica, testes automatizados, evidências de execução e instruções de reprodução.

O projeto utiliza IA generativa real em execução local e RAG, com validação dos principais endpoints.

**Prazo informado no enunciado:** 19/11/2026 às 23h55, sujeito às orientações da disciplina.

---

**PrimeiroPasso — Tecnologia para transformar preparação em oportunidade.**