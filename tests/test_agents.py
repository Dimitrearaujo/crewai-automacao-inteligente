from agents._llm import get_model_name
from agents.automation_architect import build_architect
from agents.process_analyst import build_analyst
from agents.tech_writer import build_writer


def test_get_model_name_usa_default_anthropic(monkeypatch):
    monkeypatch.delenv("LLM_PROVIDER", raising=False)
    monkeypatch.delenv("MODEL_NAME", raising=False)
    assert get_model_name() == "claude-sonnet-4-6"


def test_get_model_name_troca_pra_openai(monkeypatch):
    monkeypatch.setenv("LLM_PROVIDER", "openai")
    monkeypatch.setenv("MODEL_NAME", "gpt-4o-mini")
    assert get_model_name() == "gpt-4o-mini"


def test_build_analyst_monta_agent_real_do_crewai():
    agent = build_analyst()
    assert agent.role == "Analista Senior de Processos Corporativos"
    assert agent.allow_delegation is False


def test_build_architect_monta_agent_real_do_crewai():
    agent = build_architect()
    assert agent.role == "Arquiteto de Solucoes de Automacao Inteligente"


def test_build_writer_monta_agent_real_do_crewai():
    agent = build_writer()
    assert agent.role == "Redator Tecnico Senior"
