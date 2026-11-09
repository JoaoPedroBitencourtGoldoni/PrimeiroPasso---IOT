import os
os.environ['INTERNAL_API_KEY']='teste-chave-local'
import pytest
from fastapi.testclient import TestClient
from app.main import app
@pytest.fixture
def client(): return TestClient(app)
@pytest.fixture
def headers(): return {'x-internal-api-key':'teste-chave-local'}
