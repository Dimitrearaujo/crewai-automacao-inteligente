"""Agente 1: Analista de Processos — diagnostica gargalos e ineficiencias."""

import os
from crewai import Agent
from langchain_anthropic import ChatAnthropic
from langchain_openai import ChatOpenAI


def _get_llm():
    if os.getenv("LLM_PROVIDER", "anthropic") == "anthropic":
        return ChatAnthropic(
            model=os.getenv("MODEL_NAME", "claude-sonnet-4-6"),
            api_key=os.getenv("ANTHROPIC_API_KEY"),
        )
    return ChatOpenAI(model=os.getenv("MODEL_NAME", "gpt-4o"), api_key=os.getenv("OPENAI_API_KEY"))


def build_analyst() -> Agent:
    return Agent(
        role="Analista Senior de Processos Corporativos",
        goal=(
            "Analisar em profundidade o processo descrito pelo usuario, "
            "identificar todos os gargalos, ineficiencias e oportunidades de automacao, "
            "e produzir um diagnostico claro e estruturado."
        ),
        backstory=(
            "Voce tem 10 anos de experiencia em analise e melhoria de processos corporativos. "
            "Ja atuou em empresas de financas, saude e tecnologia mapeando processos legados "
            "e identificando onde a automacao gera mais valor. "
            "Seu diferencial e traduzir processos complexos em diagnosticos objetivos."
        ),
        llm=_get_llm(),
        verbose=True,
        allow_delegation=False,
    )
