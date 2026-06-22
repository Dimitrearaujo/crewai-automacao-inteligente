"""Agente 2: Arquiteto de Automacao — define stack e plano de implementacao."""

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


def build_architect() -> Agent:
    return Agent(
        role="Arquiteto de Solucoes de Automacao Inteligente",
        goal=(
            "Com base no diagnostico do Analista, definir a melhor stack tecnologica, "
            "arquitetura de solucao, cronograma de implementacao e ROI estimado "
            "para automatizar o processo analisado."
        ),
        backstory=(
            "Especialista em arquitetura de automacao com dominio em Python, n8n, "
            "APIs REST, agentes de IA (LangChain, CrewAI) e integracao de sistemas corporativos. "
            "Voce pensa sempre em solucoes praticas, escaláveis e com retorno rapido — "
            "nada de overengineering. Seu foco e implementar o que gera valor em semanas, nao meses."
        ),
        llm=_get_llm(),
        verbose=True,
        allow_delegation=False,
    )
