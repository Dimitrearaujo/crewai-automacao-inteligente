"""Tarefa 3: Documentacao tecnica completa em Markdown."""

from crewai import Task, Agent


def build_documentation_task(writer: Agent) -> Task:
    return Task(
        description=(
            "Consolide o diagnostico do Analista e o plano do Arquiteto em um documento "
            "tecnico completo e profissional em Markdown. O documento deve ter:\n\n"
            "1. Cabecalho com titulo, data e status\n"
            "2. Resumo executivo (3-4 linhas para gestores)\n"
            "3. Diagnostico do processo atual (gargalos e impacto)\n"
            "4. Proposta de automacao (stack + arquitetura)\n"
            "5. Cronograma de implementacao (por semanas)\n"
            "6. ROI e metricas de sucesso\n"
            "7. Proximos passos e responsaveis\n\n"
            "Escreva de forma clara, sem jargao excessivo, adequada para apresentar "
            "tanto ao time tecnico quanto a gestores de negocio."
        ),
        expected_output=(
            "Documento Markdown completo e profissional, pronto para ser entregue ao cliente, "
            "com todas as secoes preenchidas e formatadas corretamente."
        ),
        agent=writer,
    )
