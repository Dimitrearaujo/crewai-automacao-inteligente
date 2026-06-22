"""Tarefa 1: Diagnostico de processo."""

from crewai import Task, Agent


def build_analysis_task(analyst: Agent, process_description: str) -> Task:
    return Task(
        description=(
            f"Analise o seguinte processo corporativo:\n\n"
            f"'{process_description}'\n\n"
            f"Identifique:\n"
            f"1. Os principais gargalos e ineficiencias\n"
            f"2. Etapas manuais que podem ser automatizadas\n"
            f"3. Impacto estimado de cada gargalo (tempo, custo, risco)\n"
            f"4. Potencial geral de automacao (ALTO/MEDIO/BAIXO)\n\n"
            f"Seja especifico e objetivo. Cite exemplos concretos."
        ),
        expected_output=(
            "Relatorio de diagnostico estruturado com: lista de gargalos numerados, "
            "impacto de cada um, oportunidades de automacao e classificacao do potencial."
        ),
        agent=analyst,
    )
