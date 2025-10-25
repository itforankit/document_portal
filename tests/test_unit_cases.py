# tests/test_unit_cases.py

import pytest
from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)

def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert "DocSmart" in response.text

""" def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_analyze_document_missing_file():
    response = client.post("/analyze")
    assert response.status_code == 422  # Unprocessable Entity (missing file)

def test_compare_documents_missing_files():
    response = client.post("/compare")
    assert response.status_code == 422  # Unprocessable Entity (missing files)

def test_chat_index_missing_files():
    response = client.post("/chat/index")
    assert response.status_code == 422  # Unprocessable Entity (missing files) """