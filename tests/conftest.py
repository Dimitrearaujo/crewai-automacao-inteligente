import pytest


@pytest.fixture(autouse=True)
def dummy_api_keys(monkeypatch):
    """crewai/LiteLLM exigem uma chave presente para montar o Agent, mesmo
    que nenhuma chamada de rede aconteça nestes testes (nao rodamos kickoff)."""
    monkeypatch.setenv("ANTHROPIC_API_KEY", "sk-ant-test-dummy-not-real")
    monkeypatch.setenv("OPENAI_API_KEY", "sk-test-dummy-not-real")
