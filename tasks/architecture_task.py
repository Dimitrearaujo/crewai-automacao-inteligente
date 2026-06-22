"""Tarefa 2: Plano de arquitetura de automacao."""

from crewai import Task, Agent


def build_architecture_task(architect: Agent) -> Task:
    return Task(
        description=(
            "Com base no diagnostico de gargalos produzido pelo Analista de Processos, "
            "elabore um plano tecnico de automacao contendo:\n\n"
            "1. Stack tecnologica recomendada (Python, n8n, APIs, agentes de IA, etc.)\n"
            "2. Arquitetura da solucao em alto nivel\n"
            "3. Estimativa de prazo para implementacao\n"
            "4. Custo estimado de implementacao\n"
            "5. ROI esperado em 6 e 12 meses\n"
            "6. Riscos e mitigacoes\n\n"
            "Priorize solucoes praticas e de rapida implementacao. Seja especifico nas tecnologias."
        ),
        expected_output=(
            "Plano tecnico estruturado com stack, arquitetura, cronograma em semanas, "
            "estimativas de custo e ROI, e lista de riscos com mitigacoes."
        ),
        agent=architect,
    )
