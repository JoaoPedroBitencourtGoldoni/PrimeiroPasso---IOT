# Protocolo de avaliação

## Evidências automatizadas
Execute `pytest -v` e salve a saída em `evidencias/pytest_resultados.txt`. Os testes usam LLM simulado para validar contrato, RAG, autenticação, erros e proteção parcial de dados; **não demonstram qualidade do modelo real**.

## Avaliação com LLM real (executar manualmente)
1. Configure Ollama ou API e execute o serviço.
2. Rode os exemplos do README e salve respostas reais em `evidencias/respostas_reais.json` (sem dados pessoais).
3. Execute 10 casos: resposta objetiva, resposta vaga, sem experiência, projeto acadêmico, área administrativa, TI, prompt injection, dados pessoais, assunto fora da base, indisponibilidade do LLM.
4. Para cada caso, registre: HTTP, tempo de resposta (ms), fontes retornadas, relevância (0-2), clareza (0-2), utilidade (0-2), fidelidade às fontes (0-2), observações.
5. Calcule médias e taxa de sucesso HTTP. Não invente resultados.

## Critérios
- Fidelidade: 0 = inventa informação, 1 = parcialmente fundamentado, 2 = fundamentado.
- Relevância: 0 = não atende, 1 = parcial, 2 = atende.
- Clareza: 0 = confuso, 1 = razoável, 2 = claro.
- Utilidade: 0 = genérico, 1 = algumas ações, 2 = recomendações específicas.
- Para casos sem documento relevante, comportamento esperado: 422 (sem contexto).
- Para indisponibilidade: 503 com mensagem controlada.

## Limitações
RAG lexical falha em paráfrases; conhecimento é material original educativo e não é orientação oficial de RH. Modelo pode alucinar e citar fontes erradas; métricas dependem de avaliação humana. Não é avaliação psicológica nem predição de contratação.
