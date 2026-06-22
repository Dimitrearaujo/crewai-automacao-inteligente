"""Agente 3: Redator Tecnico — gera documentacao completa em Markdown."""

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


def build_writer() -> Agent:
    return Agent(
        role="Redator Tecnico Senior",
        goal=(
            "Consolidar o diagnostico e o plano de automacao em documentacao tecnica "
            "completa, clara e profissional em Markdown — pronta para ser entregue ao cliente."
        ),
        backstory=(
            "Voce tem experiencia em escrever documentacao tecnica para projetos de TI, "
            "automacao e transformacao digital. Seu diferencial e tornar assuntos tecnicos "
            "compreensíveis para times de negocio sem perder a precisao tecnica. "
            "Voce estrutura documentos com clareza: visao geral, detalhes, proximos passos."
        ),
        llm=_get_llm(),
        verbose=True,
        allow_delegation=False,
    )
