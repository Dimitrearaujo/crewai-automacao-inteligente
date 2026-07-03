# CrewAI — Automacao Inteligente de Processos Corporativos

[![CI](https://github.com/Dimitrearaujo/crewai-automacao-inteligente/actions/workflows/ci.yml/badge.svg)](https://github.com/Dimitrearaujo/crewai-automacao-inteligente/actions/workflows/ci.yml)
![Python](https://img.shields.io/badge/Python-3.12-blue)
![CrewAI](https://img.shields.io/badge/CrewAI-0.28%2B-orange)
![License](https://img.shields.io/badge/license-MIT-lightgrey)

Um **sistema multi-agente** que automatiza o ciclo completo de analise e implementacao de automacoes corporativas. Tres agentes especializados trabalham em equipe: Analista de Processos, Arquiteto de Automacao e Redator Tecnico.

## Quick Start

```bash
git clone https://github.com/Dimitrearaujo/crewai-automacao-inteligente.git
cd crewai-automacao-inteligente
pip install -r requirements.txt
cp .env.example .env  # configure sua API key
python crew.py
```

## O que voce vai ter

- Crew de 3 agentes IA com papeis e objetivos distintos
- Analise automatica de processos e identificacao de gargalos
- Plano de automacao gerado com tecnologias, prazos e ROI
- Documentacao tecnica completa gerada automaticamente
- Resultado exportado em Markdown estruturado
- Compativel com Claude (Anthropic) e GPT-4o (OpenAI)

## Arquitetura

### Os 3 Agentes

```
┌─────────────────────────────────────────────────────────┐
│                        CREW                             │
│                                                         │
│  Agente 1: Analista de Processos                        │
│  - Entende o processo descrito pelo usuario             │
│  - Identifica gargalos e ineficiencias                  │
│  - Produz relatorio de diagnostico                      │
│                  |                                      │
│                  v                                      │
│  Agente 2: Arquiteto de Automacao                       │
│  - Recebe diagnostico do Analista                       │
│  - Define stack tecnologica (Python, n8n, APIs)         │
│  - Estima prazo, custo e ROI da implementacao           │
│                  |                                      │
│                  v                                      │
│  Agente 3: Redator Tecnico                              │
│  - Recebe plano do Arquiteto                            │
│  - Gera documentacao completa em Markdown               │
│  - Cria guia de implementacao passo a passo             │
└─────────────────────────────────────────────────────────┘
```

### Stack

- **CrewAI** — orquestracao dos agentes e tarefas sequenciais
- **Anthropic Claude / OpenAI GPT-4o** — LLM base (configuravel)
- **Python 3.10+** — runtime
- **Pydantic** — validacao de outputs estruturados

## Estrutura

```
crewai-automacao-inteligente/
├── crew.py                   <- Ponto de entrada principal
├── agents/
│   ├── process_analyst.py    <- Agente analista de processos
│   ├── automation_architect.py <- Agente arquiteto de automacao
│   └── tech_writer.py        <- Agente redator tecnico
├── tasks/
│   ├── analysis_task.py      <- Tarefa de diagnostico
│   ├── architecture_task.py  <- Tarefa de arquitetura
│   └── documentation_task.py <- Tarefa de documentacao
├── tools/
│   └── process_tools.py      <- Tools compartilhadas entre agentes
├── output/                   <- Resultados gerados
├── .env.example
├── requirements.txt
└── README.md
```

## Exemplo de Uso

Voce informa o processo:
> "Nosso processo de aprovacao de contratos envolve 4 departamentos, usa email para comunicacao e leva em media 5 dias uteis."

A crew entrega:

**Agente 1 — Diagnostico:**
```
Gargalos identificados:
- Comunicacao por email: sem rastreabilidade, SLA implicito
- 4 departamentos em sequencia: nenhum passo em paralelo
- Aprovacao manual em 100% dos contratos: sem regras automaticas
Potencial de automacao: ALTO
```

**Agente 2 — Plano de Automacao:**
```
Stack recomendada:
- n8n: orquestracao do fluxo de aprovacao
- API REST interna: integracao com sistema de contratos
- Regras de negocio em Python: aprovacao automatica para contratos < R$10k
- Notificacoes via WhatsApp Business API

Estimativa: 3 semanas | ROI: 340% em 12 meses
```

**Agente 3 — Documentacao:**
- Arquivo .md completo com fluxo, diagrama textual e guia de implementacao

## Configuracao

```env
# .env.example
LLM_PROVIDER=anthropic
ANTHROPIC_API_KEY=sk-ant-...
OPENAI_API_KEY=sk-...
MODEL_NAME=claude-sonnet-4-6
VERBOSE=true
OUTPUT_DIR=./output
```

## Casos de Uso

- Automacao de aprovacoes e workflows corporativos
- Modernizacao de processos legados (email -> API)
- Documentacao automatica de processos existentes
- Identificacao e priorizacao de oportunidades de RPA

## Requisitos

- Python 3.10+
- API key da Anthropic (Claude) ou OpenAI
- Conexao com internet para chamar a API LLM

## Licenca

MIT — use livremente em producao.

---

<details>
<summary>🇺🇸 English</summary>

# CrewAI — Intelligent Corporate Process Automation

[![CI](https://github.com/Dimitrearaujo/crewai-automacao-inteligente/actions/workflows/ci.yml/badge.svg)](https://github.com/Dimitrearaujo/crewai-automacao-inteligente/actions/workflows/ci.yml)
![Python](https://img.shields.io/badge/Python-3.12-blue)
![CrewAI](https://img.shields.io/badge/CrewAI-0.28%2B-orange)
![License](https://img.shields.io/badge/license-MIT-lightgrey)

A **multi-agent system** that automates the full cycle of analyzing and implementing corporate automations. Three specialized agents work as a team: Process Analyst, Automation Architect and Technical Writer.

## Quick Start

```bash
git clone https://github.com/Dimitrearaujo/crewai-automacao-inteligente.git
cd crewai-automacao-inteligente
pip install -r requirements.txt
cp .env.example .env  # configure your API key
python crew.py
```

## What you get

- A crew of 3 AI agents with distinct roles and goals
- Automatic process analysis and bottleneck identification
- Automation plan generated with technologies, timeline and ROI
- Complete technical documentation generated automatically
- Result exported as structured Markdown
- Compatible with Claude (Anthropic) and GPT-4o (OpenAI)

## Architecture

### The 3 Agents

```
┌─────────────────────────────────────────────────────────┐
│                        CREW                             │
│                                                         │
│  Agent 1: Process Analyst                                │
│  - Understands the process described by the user        │
│  - Identifies bottlenecks and inefficiencies             │
│  - Produces a diagnosis report                           │
│                  |                                      │
│                  v                                      │
│  Agent 2: Automation Architect                           │
│  - Receives diagnosis from the Analyst                   │
│  - Defines the tech stack (Python, n8n, APIs)            │
│  - Estimates timeline, cost and ROI of implementation     │
│                  |                                      │
│                  v                                      │
│  Agent 3: Technical Writer                               │
│  - Receives the plan from the Architect                  │
│  - Generates complete documentation in Markdown          │
│  - Creates a step-by-step implementation guide            │
└─────────────────────────────────────────────────────────┘
```

### Stack

- **CrewAI** — agent orchestration and sequential tasks
- **Anthropic Claude / OpenAI GPT-4o** — base LLM (configurable)
- **Python 3.10+** — runtime
- **Pydantic** — structured output validation

## Structure

```
crewai-automacao-inteligente/
├── crew.py                   <- Main entry point
├── agents/
│   ├── process_analyst.py    <- Process analyst agent
│   ├── automation_architect.py <- Automation architect agent
│   └── tech_writer.py        <- Technical writer agent
├── tasks/
│   ├── analysis_task.py      <- Diagnosis task
│   ├── architecture_task.py  <- Architecture task
│   └── documentation_task.py <- Documentation task
├── tools/
│   └── process_tools.py      <- Tools shared between agents
├── output/                   <- Generated results
├── .env.example
├── requirements.txt
└── README.md
```

## Usage Example

You describe the process:
> "Our contract approval process involves 4 departments, uses email for communication and takes an average of 5 business days."

The crew delivers:

**Agent 1 — Diagnosis:**
```
Bottlenecks identified:
- Email communication: no traceability, implicit SLA
- 4 sequential departments: no parallel steps
- Manual approval on 100% of contracts: no automatic rules
Automation potential: HIGH
```

**Agent 2 — Automation Plan:**
```
Recommended stack:
- n8n: approval flow orchestration
- Internal REST API: integration with contract system
- Python business rules: automatic approval for contracts under $2k
- Notifications via WhatsApp Business API

Estimate: 3 weeks | ROI: 340% in 12 months
```

**Agent 3 — Documentation:**
- Complete .md file with flow, text diagram and implementation guide

## Configuration

```env
# .env.example
LLM_PROVIDER=anthropic
ANTHROPIC_API_KEY=sk-ant-...
OPENAI_API_KEY=sk-...
MODEL_NAME=claude-sonnet-4-6
VERBOSE=true
OUTPUT_DIR=./output
```

## Use Cases

- Automation of corporate approvals and workflows
- Modernization of legacy processes (email -> API)
- Automatic documentation of existing processes
- Identification and prioritization of RPA opportunities

## Requirements

- Python 3.10+
- Anthropic (Claude) or OpenAI API key
- Internet connection to call the LLM API

## License

MIT — use freely in production.

</details>

---

**Feito por [Dimitre Araujo](https://github.com/Dimitrearaujo) — CD Tech**
Junho 2026 | v1.0
