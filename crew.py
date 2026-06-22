"""
CrewAI — Automacao Inteligente de Processos Corporativos
Sistema multi-agente com 3 especialistas para analise, planejamento e documentacao.
"""

import os
from dotenv import load_dotenv
from crewai import Crew, Process
from agents.process_analyst import build_analyst
from agents.automation_architect import build_architect
from agents.tech_writer import build_writer
from tasks.analysis_task import build_analysis_task
from tasks.architecture_task import build_architecture_task
from tasks.documentation_task import build_documentation_task

load_dotenv()


def run_crew(process_description: str) -> str:
    analyst   = build_analyst()
    architect = build_architect()
    writer    = build_writer()

    task_analysis  = build_analysis_task(analyst, process_description)
    task_architect = build_architecture_task(architect)
    task_doc       = build_documentation_task(writer)

    crew = Crew(
        agents=[analyst, architect, writer],
        tasks=[task_analysis, task_architect, task_doc],
        process=Process.sequential,
        verbose=os.getenv("VERBOSE", "true").lower() == "true",
    )

    result = crew.kickoff()
    return str(result)


if __name__ == "__main__":
    print("\n=== CrewAI — Automacao Inteligente de Processos ===\n")
    print("Descreva o processo que deseja analisar e automatizar.")
    print("(Ex: 'Nosso processo de onboarding leva 5 dias e envolve 4 departamentos')\n")

    desc = input("Processo: ").strip()
    if not desc:
        desc = "Processo de aprovacao de contratos via email com 4 departamentos, levando 5 dias uteis."

    print("\nIniciando analise com a crew de agentes...\n")
    resultado = run_crew(desc)

    output_dir = os.getenv("OUTPUT_DIR", "./output")
    os.makedirs(output_dir, exist_ok=True)
    output_file = f"{output_dir}/resultado_automacao.md"
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(resultado)

    print(f"\n=== Resultado salvo em: {output_file} ===\n")
    print(resultado[:1000] + "..." if len(resultado) > 1000 else resultado)
