# Revisão técnica — 09/11/2026

## Correções aplicadas
1. Exclusão de `.env` do pacote; não distribuir credenciais.
2. Comparação de chave com `secrets.compare_digest`.
3. Inclusão de três testes automatizados de segurança.
4. Remoção de caches e arquivos compilados da entrega.

## Pendências reais (não declarar como concluídas)
- Trocar imediatamente a chave interna exibida em capturas e arquivos anteriores.
- Executar testes reais com Ollama, registrar casos e resultados verificáveis.
- Completar identificação e URL do repositório GitHub.
- Confirmar se a integração Java será exigida na apresentação; o cliente incluído é somente exemplo.
- Medir latência e avaliar fidelidade factual, citações e robustez contra prompt injection em casos reais.
- A anonimização regex é parcial; evitar entrada de dados pessoais reais.

## Critérios FIAP
10 pontos: adequação; 25: IA generativa integrada; 25: aprofundamento; 15: arquitetura/dados; 15: avaliação; 10: organização e uso responsável. Não é possível garantir nota sem execução e avaliação do professor.
