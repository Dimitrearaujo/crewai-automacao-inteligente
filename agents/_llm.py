"""Resolve qual modelo cada agente usa.

crewai>=1.0 roteia LLM via LiteLLM e espera o identificador do modelo como
string (ex: "claude-sonnet-4-6", "gpt-4o") — nao mais um objeto LangChain
(ChatAnthropic/ChatOpenAI). As chaves de API continuam vindo das variaveis
de ambiente padrao (ANTHROPIC_API_KEY, OPENAI_API_KEY), que o LiteLLM le
sozinho a partir do prefixo do nome do modelo.
"""

import os


def get_model_name() -> str:
    if os.getenv("LLM_PROVIDER", "anthropic") == "anthropic":
        return os.getenv("MODEL_NAME", "claude-sonnet-4-6")
    return os.getenv("MODEL_NAME", "gpt-4o")
