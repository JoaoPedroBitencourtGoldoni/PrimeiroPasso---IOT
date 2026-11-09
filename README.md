# 🚀 PrimeiroPasso
### EntrevistaLab — Preparação inteligente para o mercado de trabalho

**Global Solution 2026/2 | FIAP**

**Disruptive Architectures: IoT, IoB & Generative IA**

`Python` `FastAPI` `Generative AI` `Ollama` `RAG` `REST API` `Pytest`

---

## 📌 Sobre o projeto

O **PrimeiroPasso** é uma solução tecnológica voltada à preparação de jovens e pessoas que buscam sua primeira oportunidade profissional.

Por meio do módulo **EntrevistaLab**, a plataforma utiliza Inteligência Artificial Generativa e Recuperação Aumentada por Geração (RAG) para simular perguntas de entrevistas e oferecer feedback personalizado sobre as respostas dos participantes.

A proposta é proporcionar uma experiência de aprendizado acessível, permitindo que os usuários desenvolvam habilidades de comunicação, organização de ideias e apresentação de suas experiências.

> **Nossa missão:** utilizar a tecnologia para ampliar o acesso à preparação profissional e contribuir para uma entrada mais confiante no mercado de trabalho.

O sistema possui finalidade exclusivamente educacional e não realiza avaliações ou decisões de contratação.

## 🎯 Objetivos

- Democratizar o acesso à preparação para entrevistas de emprego.
- Auxiliar jovens sem experiência profissional a reconhecer suas competências.
- Simular situações reais de processos seletivos.
- Oferecer feedback personalizado por meio de IA generativa.
- Incentivar respostas estruturadas e comunicação profissional.
- Contribuir para a inclusão social e a empregabilidade.

### 🌎 Alinhamento aos Objetivos de Desenvolvimento Sustentável

| ODS | Objetivo | Contribuição |
|---|---|---|
| **ODS 4** | Educação de Qualidade | Promover aprendizado e desenvolvimento de competências |
| **ODS 8** | Trabalho Decente e Crescimento Econômico | Apoiar a preparação para oportunidades profissionais |
| **ODS 10** | Redução das Desigualdades | Ampliar o acesso a ferramentas de orientação profissional |

---

## 🧠 Tecnologias utilizadas

| Tecnologia | Aplicação |
|---|---|
| Python 3.11+ | Linguagem principal |
| FastAPI | Desenvolvimento da API REST |
| Ollama | Execução local de modelos de linguagem |
| Llama 3.2 3B | Modelo de IA generativa |
| RAG | Recuperação de conhecimento para contextualização |
| TF-IDF | Representação textual dos documentos |
| Similaridade cosseno | Identificação de conteúdos relevantes |
| Pydantic | Validação de dados |
| Pytest | Testes automatizados |
| Swagger UI | Documentação e testes interativos da API |

A arquitetura também permite utilizar um provedor de IA externo compatível com a API da OpenAI.

## ⚙️ Funcionalidades

### 1. Geração inteligente de perguntas

O EntrevistaLab cria perguntas contextualizadas considerando a área profissional, o nível de experiência e os projetos informados pelo participante.

**Endpoint:** `POST /api/v1/entrevistas/pergunta`

### 2. Feedback personalizado

O sistema analisa a resposta enviada pelo usuário e produz orientações educacionais, incluindo:

- Pontos fortes da resposta.
- Oportunidades de melhoria.
- Sugestões de estruturação.
- Exemplos de respostas aprimoradas.
- Recomendações para continuar praticando.

**Endpoint:** `POST /api/v1/entrevistas/feedback`

### 3. Recuperação de conhecimento com RAG

Antes de gerar orientações, o sistema consulta uma base de conhecimento sobre entrevistas e desenvolvimento profissional.

O mecanismo utiliza **TF-IDF e similaridade cosseno** para selecionar até três fontes relevantes, aplicando um limiar de relevância.

Essa abordagem busca contextualizar as respostas do modelo e permitir a identificação das fontes utilizadas.

### 4. API documentada

A aplicação disponibiliza documentação interativa por meio do Swagger UI, permitindo visualizar os endpoints e executar requisições.

**Swagger:** `http://localhost:8000/docs`

---

## 🏗️ Arquitetura da solução

O PrimeiroPasso utiliza uma arquitetura modular, separando a camada de API, a recuperação de conhecimento e a comunicação com o modelo generativo.

**Fluxo de processamento:**

1. O usuário envia os dados da entrevista.
2. A API valida a requisição e a chave interna.
3. O sistema aplica mascaramento de determinados dados pessoais.
4. O mecanismo RAG recupera conteúdos relevantes.
5. O modelo de linguagem recebe o contexto recuperado.
6. A IA gera a pergunta ou o feedback.
7. A API retorna o resultado e as referências utilizadas.

**Componentes principais:**

- **API REST:** FastAPI.
- **Validação:** Pydantic.
- **Recuperação:** TF-IDF e similaridade cosseno.
- **Inteligência Artificial:** Ollama com Llama 3.2 3B.
- **Base de conhecimento:** documentos estruturados em JSON.
- **Segurança:** chave interna e mascaramento parcial de dados.
- **Qualidade:** testes automatizados e avaliações manuais.

A documentação técnica detalhada está disponível em `docs/arquitetura.md`.

## 📂 Estrutura do projeto

```text
PrimeiroPasso/
│
├── app/
│   └── Aplicação FastAPI e módulos de IA
│
├── knowledge/
│   └── base.json
│
├── tests/
│   └── Testes automatizados
│
├── docs/
│   ├── arquitetura.md
│   └── avaliacao.md
│
├── evidencias/
│   └── Registros e casos de teste
│
├── integracao-java/
│   └── Exemplo de integração com Java
│
├── .env.example
├── .gitignore
├── IDENTIFICACAO_MODELO.txt
├── requirements.txt
└── README.md
```

---

## 💻 Como executar o projeto

### Pré-requisitos

Antes de iniciar, instale:

- Python 3.11 ou superior.
- Git.
- Ollama, para executar a IA localmente.
- Modelo `llama3.2:3b`.

### 1. Clonar o repositório

```bash
git clone https://github.com/JoaoPedroBitencourtGoldoni/PrimeiroPasso---IOT.git

cd PrimeiroPasso---IOT
```

### 2. Criar o ambiente virtual

**Windows — PowerShell:**

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**Windows — Git Bash:**

```bash
python -m venv .venv
source .venv/Scripts/activate
```

### 3. Instalar as dependências

```bash
python -m pip install -r requirements.txt
```

### 4. Configurar as variáveis de ambiente

Crie o arquivo `.env` a partir do exemplo disponibilizado no repositório.

**PowerShell:**

```powershell
Copy-Item .env.example .env
```

**Git Bash:**

```bash
cp .env.example .env
```

Exemplo de configuração local:

```env
LLM_PROVIDER=ollama
OLLAMA_URL=http://localhost:11434
OLLAMA_MODEL=llama3.2:3b

OPENAI_BASE_URL=https://api.openai.com/v1
OPENAI_MODEL=gpt-4o-mini
OPENAI_API_KEY=

INTERNAL_API_KEY=DEFINA_SUA_CHAVE_LOCAL
REQUEST_TIMEOUT=180
```

A variável `INTERNAL_API_KEY` deve receber uma chave aleatória segura.

**Importante:** o arquivo `.env` é privado e não deve ser enviado ao GitHub.

### 5. Preparar o modelo de IA

Instale o Ollama e execute:

```bash
ollama pull llama3.2:3b
```

Caso o serviço não esteja em execução:

```bash
ollama serve
```

### 6. Iniciar a API

Com o ambiente virtual ativado:

```bash
python -m uvicorn app.main:app --reload
```

Acesse a documentação interativa:

**http://127.0.0.1:8000/docs**

A API estará disponível para receber requisições.

---

## 🔗 Endpoints disponíveis

| Método | Endpoint | Descrição |
|---|---|---|
| GET | `/health` | Verifica o funcionamento básico da API |
| GET | `/api/v1/fontes` | Lista as fontes da base de conhecimento |
| POST | `/api/v1/entrevistas/pergunta` | Gera uma pergunta personalizada |
| POST | `/api/v1/entrevistas/feedback` | Gera feedback educacional |

Os endpoints de entrevistas utilizam autenticação pelo cabeçalho:

```http
x-internal-api-key: SUA_CHAVE_LOCAL
```

### Exemplo — Gerar uma pergunta

**POST** `/api/v1/entrevistas/pergunta`

```json
{
  "area": "administrativa",
  "nivel": "primeiro_emprego",
  "projeto": "Organização de evento escolar"
}
```

### Exemplo — Solicitar feedback

**POST** `/api/v1/entrevistas/feedback`

```json
{
  "area": "administrativa",
  "nivel": "primeiro_emprego",
  "projeto": "Organização de evento escolar",
  "pergunta": "Conte sobre uma situação em que você trabalhou em equipe.",
  "resposta": "Durante um projeto escolar, organizei as inscrições de um evento, distribuí tarefas entre meus colegas e acompanhei os prazos. Conseguimos concluir o evento dentro do prazo."
}
```

O retorno contém o feedback gerado pela IA, as fontes recuperadas pelo RAG e um aviso sobre a finalidade educacional da solução.

---

## 🧪 Testes e validação

O projeto utiliza Pytest para verificar os principais componentes da aplicação.

Os testes automatizados abrangem:

- Funcionamento básico da API.
- Validação de dados.
- Autenticação por chave interna.
- Recuperação de documentos.
- Mascaramento de dados pessoais.
- Tratamento de falhas do provedor de IA.
- Geração de perguntas e feedback com modelo simulado.
- Verificação de respostas dos endpoints.

### Executar os testes

```bash
python -m pytest -v
```

**Resultado da validação local realizada:**

**14 testes aprovados | 0 falhas**

Os testes automatizados utilizam simulações do LLM e, portanto, não exigem Ollama em execução.

Também foi realizado um teste manual de feedback com o modelo local, obtendo resposta HTTP 200, feedback gerado e referências recuperadas pelo RAG.

Os procedimentos de avaliação estão documentados em `docs/avaliacao.md`.

## 🔐 Segurança e privacidade

A aplicação adota mecanismos básicos de proteção:

- Autenticação dos endpoints protegidos por chave interna.
- Validação de entrada com Pydantic.
- Comparação de credenciais com `secrets.compare_digest`.
- Mascaramento parcial de CPF, e-mail e telefone.
- Separação de configurações sensíveis em variáveis de ambiente.
- Exclusão do `.env` do versionamento.

O mascaramento por expressões regulares não representa anonimização completa.

Para uma implantação em produção, são recomendados HTTPS, limitação de requisições, monitoramento, gestão de segredos e políticas de retenção de dados.

## ☕ Integração com Java

O diretório `integracao-java/` contém um exemplo de cliente Java para comunicação com o serviço de IA.

A arquitetura prevê integração futura com um backend Spring Boot, responsável pela autenticação dos usuários, autorização e comunicação segura com o EntrevistaLab.

O cliente disponibilizado é demonstrativo. A integração ponta a ponta e uma implementação com Spring AI não fazem parte do escopo implementado neste repositório.

---

## ⚖️ Limitações e uso responsável

O PrimeiroPasso é uma ferramenta de apoio educacional.

As respostas geradas por IA podem apresentar imprecisões, interpretações incorretas ou informações não verificadas.

A qualidade das orientações depende da pergunta, dos documentos recuperados e do comportamento do modelo utilizado.

A ferramenta não substitui orientação profissional especializada, não realiza seleção de candidatos e não garante oportunidades de emprego.

## 🔮 Possibilidades de evolução

O projeto poderá ser ampliado com:

- Interface web responsiva para os participantes.
- Histórico de simulações de entrevistas.
- Acompanhamento da evolução individual.
- Simulações por área profissional.
- Integração completa com backend Java.
- Recursos de acessibilidade.
- Avaliação de desempenho com métricas educacionais.
- Ampliação da base de conhecimento e recuperação semântica.

---

## 🎓 Informações acadêmicas

**Instituição:** FIAP — Faculdade de Informática e Administração Paulista

**Projeto:** PrimeiroPasso — EntrevistaLab

**Desafio:** Global Solution 2026/2 — CitizenTech

**Disciplina:** Disruptive Architectures: IoT, IoB & Generative IA

**Integrantes:** 
- 563512 — Felipe Maglio Filho
- 564339 — João Pedro Bitencourt Goldoni
- 561786 — Marina Tamagnini Magalhães
- 564930 — Mateus Granja dos Santos
- 563509 — Vitória Valentina Maglio

## 📦 Entrega

O repositório reúne o código-fonte, a documentação técnica, a base de conhecimento, os testes e as evidências do projeto.

O arquivo `IDENTIFICACAO_MODELO.txt` deve conter os dados dos integrantes e o endereço do repositório, conforme as orientações acadêmicas.

---

**PrimeiroPasso — Tecnologia, educação e oportunidades para transformar o início de uma trajetória profissional.**
