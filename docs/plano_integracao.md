# Escopo da entrega IoT e integração futura

## Funcionalidade entregue agora
O EntrevistaLab é um serviço Python/FastAPI independente, com dois endpoints de IA generativa, recuperação RAG e documentação Swagger. Ele pode ser demonstrado diretamente no Swagger, sem projeto Java.

## O que ainda NÃO está implementado
Não há integração ponta a ponta com Spring Boot, autenticação JWT do usuário final ou aplicativo Mobile. O arquivo `integracao-java/EntrevistaLabClient.java` é apenas uma referência de integração futura. Não apresente esses recursos como implementados.

## Integração futura, quando existir o backend Java
1. Criar endpoint de domínio no Java e autenticação do usuário.
2. Chamar a API Python pela rede do backend, com chave interna em variável de ambiente.
3. Validar timeouts, falhas e contratos JSON.
4. Executar testes de integração reais.

A avaliação desta entrega de IoT pode focar na execução independente do serviço Python e em sua integração interna entre API, recuperador e LLM. O enunciado de IoT não impõe Java como tecnologia obrigatória.
