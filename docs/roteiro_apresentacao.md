# Demonstração presencial — IoT (sem Java)

1. **Problema (30 s):** jovens sem experiência precisam treinar entrevistas; conexão com ODS 4, 8 e 10.
2. **Arquitetura (45 s):** Swagger → FastAPI → busca TF-IDF/cosseno → trechos da base → Ollama → resposta e fontes.
3. **Demonstração (90 s):** com Ollama em execução, gerar pergunta e feedback no Swagger. Não usar mocks na demonstração.
4. **Avaliação (60 s):** mostrar `pytest -v`, `python -m scripts.avaliar_rag` e evidências reais; distinguir testes simulados de execução do modelo.
5. **Limitações e adaptação (45 s):** citar falhas em paráfrases, risco de alucinação, proteção parcial de PII e como adaptar para outra área/base.

**Pergunta provável:** "Onde está o Java?" — "A entrega desta disciplina é o serviço de IA em Python, executável e testável independentemente. O Java será integrado quando o backend estiver disponível; não afirmamos que a integração já exista."
