from unittest.mock import patch
from fastapi.testclient import TestClient
from app.main import app
from app.core import settings

def test_anonimizacao_antes_da_ia():
    client = TestClient(app)
    capturado = {}

    async def fake_generate(prompt):
        capturado["prompt"] = prompt
        return "Feedback educacional seguro."

    payload = {
        "area": "administrativa",
        "nivel": "primeiro_emprego",
        "projeto": "Organizacao escolar",
        "pergunta": "Conte sobre sua experiencia.",
        "resposta": (
            "Meu email e teste@example.com e meu CPF "
            "e 123.456.789-09. Organizei um evento escolar."
        )
    }

    with patch("app.main.generate", side_effect=fake_generate):
        response = client.post(
            "/api/v1/entrevistas/feedback",
            headers={
                "x-internal-api-key": settings.internal_key
            },
            json=payload
        )

    assert response.status_code == 200
    assert "teste@example.com" not in capturado["prompt"]
    assert "123.456.789-09" not in capturado["prompt"]
    assert "[EMAIL]" in capturado["prompt"]
    assert "[CPF]" in capturado["prompt"]
