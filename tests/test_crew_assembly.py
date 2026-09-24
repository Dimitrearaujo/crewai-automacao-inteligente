"""Monta o Crew completo (agentes + tasks reais) sem chamar kickoff() —
ou seja, sem gastar tokens de LLM. Isso pega bug de wiring (ex: parametro
errado, agent nao aceito pela versao instalada do crewai) que um teste
que so verifica string em arquivo nunca pegaria."""

from crewai import Crew, Process

from agents.automation_architect import build_architect
from agents.process_analyst import build_analyst
from agents.tech_writer import build_writer
from tasks.analysis_task import build_analysis_task
from tasks.architecture_task import build_architecture_task
from tasks.documentation_task import build_documentation_task


def test_crew_completo_monta_sem_chamar_llm():
    analyst = build_analyst()
    architect = build_architect()
    writer = build_writer()

    task_analysis = build_analysis_task(analyst, "processo de teste com 4 etapas manuais")
    task_architect = build_architecture_task(architect)
    task_doc = build_documentation_task(writer)

    crew = Crew(
        agents=[analyst, architect, writer],
        tasks=[task_analysis, task_architect, task_doc],
        process=Process.sequential,
        verbose=False,
    )

    assert len(crew.agents) == 3
    assert len(crew.tasks) == 3
    assert crew.tasks[0].agent.role == analyst.role
