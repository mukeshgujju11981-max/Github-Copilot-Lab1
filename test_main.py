"""Unit tests for the FastAPI checksum application."""

import hashlib

from fastapi.testclient import TestClient

from main import app


client = TestClient(app)


def test_home_returns_welcome_message() -> None:
	"""The root endpoint should return the welcome page and name."""

	response = client.get("/")

	assert response.status_code == 200
	assert "Gujju Mukesh" in response.text


def test_generate_returns_valid_checksum() -> None:
	"""The generate endpoint should return the SHA-256 digest for the input."""

	response = client.post("/generate", json={"text": "test"})

	assert response.status_code == 200
	checksum = response.json()["checksum"]
	assert len(checksum) == 64
	assert checksum == hashlib.sha256(b"test").hexdigest()
