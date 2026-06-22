# CrewAI — Automacao Inteligente de Processos Corporativos

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

**Feito por [Dimitre Araujo](https://github.com/Dimitrearaujo) — CD Tech**
Junho 2026 | v1.0
