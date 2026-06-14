# VentureMind AI  
### *Because optimism is expensive.*

<p align="center">
  <b>AI-Powered Multi-Agent Startup Reasoning Engine</b><br/>
  Helping founders decide whether a startup idea should be <b>pursued</b>, <b>pivoted</b>, or <b>abandoned</b> through structured reasoning and forced skepticism.
</p>

---

# 🚀 Overview

**VentureMind AI** is an intelligent startup evaluation system powered by **multi-agent reasoning**.

Unlike traditional AI startup tools that generate **blind optimism**, VentureMind AI challenges assumptions, debates trade-offs, and pressure-tests startup ideas from multiple perspectives before founders invest time, money, and effort.

The system behaves like a panel of experts:

- 🧠 Venture Capitalist  
- ⚙️ Technical Architect  
- 📈 Market Strategist  
- 💰 Financial Analyst  
- 🥊 Devil’s Advocate  
- 🏆 Decision Judge

Instead of saying:

> “Great idea, you should build this!”

VentureMind AI asks:

> “Will users actually pay?”  
> “Can this realistically be built?”  
> “What kills this startup in 2 years?”  
> “Where is the moat?”  
> “Should this be pivoted?”

The result is a **reasoning-first startup intelligence system**, not just another chatbot.

---

# ❌ Problem Statement

Most startup founders fail because they make decisions based on:

- optimism bias
- weak market validation
- incomplete research
- founder assumptions
- hype-driven AI suggestions

Current AI startup assistants are broken.

They usually:

✅ Generate ideas  
✅ Validate assumptions blindly  
✅ Encourage founders

But they rarely:

❌ Criticize weak ideas  
❌ Simulate failure  
❌ Challenge monetization  
❌ Debate contradictions  
❌ Evaluate technical realism

This creates **false confidence**, leading founders to waste:

```text
months of effort
engineering time
money
opportunity cost
```

---

# 💡 Our Solution

**VentureMind AI** solves this problem using a **multi-agent reasoning architecture**.

Instead of one AI assistant, we orchestrate **multiple specialized agents** that independently analyze the startup from different perspectives.

These agents:

- research
- challenge assumptions
- disagree
- debate
- expose contradictions
- simulate failure

Finally, a **Decision Judge Agent** produces a verdict:

```text
PROCEED
PIVOT
AVOID
```

---

# 🔥 Key Innovation

### Forced Skepticism

Most AI startup systems optimize for:

```text
helpfulness
optimism
idea generation
```

VentureMind AI optimizes for:

```text
critical thinking
skepticism
contradiction
reasoned decisions
```

The **Devil’s Advocate Agent** intentionally attacks assumptions.

Example:

### Founder Assumption

> Students will pay ₹500/month.

### Devil's Advocate Response

> Evidence weak. Students prefer free tools.  
> Retention risk is high.  
> B2B college partnerships may be stronger.

This makes VentureMind AI fundamentally different.

---

# 🏗️ System Architecture

## High-Level Workflow

```text
USER INPUT
      ↓
Input Understanding Agent
      ↓
Context Builder Layer
      ↓
┌────────────┬────────────┬────────────┬────────────┬
↓            ↓            ↓            ↓            ↓
Market    Technical   Financial   Competition   Devil's
Agent     Agent       Agent       Agent         Advocate
└────────────┴────────────┴────────────┴────────────┘
                      ↓
              Debate & Contradiction
                      ↓
               Decision Judge Agent
                      ↓
                  Final Report
```

---

# 🤖 Multi-Agent Architecture

VentureMind AI uses **9 specialized agents**.

---

## 1. Startup Intake Agent

### Purpose

Converts vague startup ideas into structured startup data.

### Example Input

```text
I want to build AI for students
```

### Extracted Output

```json
{
  "domain": "education",
  "customer_type": "students",
  "business_model": null,
  "market": null,
  "problem": null
}
```

### Responsibilities

- identify startup category
- extract metadata
- detect ambiguity
- identify missing information

---

## 2. Context Builder Agent

### Purpose

Creates research-backed context.

This layer prevents hallucination.

Research includes:

- market trends
- industry demand
- competitors
- pricing models
- technology stack
- startup ecosystem signals

---

## 3. Market Analyst Agent

### Core Question

> Will people actually care?

Analyzes:

- problem pain level
- willingness to pay
- market timing
- demand validation
- TAM / SAM / SOM

### Output Example

```json
{
  "market_score": 76,
  "growth_potential": "high",
  "market_risk": "medium"
}
```

---

## 4. Technical Architect Agent

### Core Question

> Can this realistically be built?

Analyzes:

- technical complexity
- timeline realism
- infrastructure cost
- vendor dependency
- AI feasibility

### Example Reasoning

```text
2 developers
2 months
AI video generation

→ unrealistic timeline
→ infrastructure cost too high
```

---

## 5. Financial Analyst Agent

### Core Question

> Can this survive economically?

Analyzes:

- burn rate
- monetization
- pricing realism
- CAC vs LTV
- subscription viability

### Example Insight

```text
Students rarely pay subscriptions.

Better monetization:
B2B partnerships with colleges.
```

---

## 6. Competition Agent

### Core Question

> Why would users choose this?

Analyzes:

- competitors
- market saturation
- switching cost
- defensibility
- moat strength

### Example

Weak moat:

```text
ChatGPT wrapper
```

Strong moat:

```text
proprietary education dataset
```

---

## 7. Devil’s Advocate Agent

### Core Question

> Why does this fail?

Responsibilities:

- destroy assumptions
- attack weak logic
- predict failure
- identify blind spots

### Example

```text
If Google launches this feature,
your startup dies.
```

This is the system’s strongest differentiator.

---

## 8. Debate Layer

### Purpose

Agents challenge one another.

Example:

### Market Agent

> High demand.

### Finance Agent

> Demand exists, but users won’t pay.

### Devil's Advocate

> Weak retention. Easy to copy.

This layer resolves contradictions.

No fake consensus.

---

## 9. Decision Judge Agent

### Purpose

Makes the final decision.

### Verdict Options

| Score | Decision |
|--------|----------|
| 80–100 | PROCEED |
| 60–79 | PIVOT |
| 0–59 | AVOID |

---

# ⚡ Working Flow

## Step 1 — User Input

Founder submits startup idea.

Example:

```text
Idea:
AI interview preparation platform

Target Users:
College students

Budget:
₹80,000

Timeline:
3 months

Team:
2 developers

Country:
India
```

---

## Step 2 — Startup Understanding

System converts messy input into structured startup profile.

---

## Step 3 — Research Layer

Builds market context.

Researches:

- competitors
- pricing
- industry growth
- technical needs

---

## Step 4 — Specialist Analysis

Multiple agents independently analyze the startup.

Each expert produces separate reasoning.

---

## Step 5 — Cross-Agent Debate

Agents challenge assumptions.

Example:

```text
Market:
Strong demand.

Finance:
Poor monetization.

Competition:
No defensible moat.

Devil’s Advocate:
Easy feature clone.
```

---

## Step 6 — Final Verdict

The Decision Judge produces:

```text
Startup Viability Score: 68/100

Verdict:
PIVOT
```

---

# 📊 Scoring Framework

```text
Market        → 30%
Technical     → 20%
Financial     → 20%
Competition   → 15%
Risk           → 15%
```

---

# 🛠️ Tech Stack

### AI Orchestration

- CrewAI

### Local LLM

- Ollama
- qwen3:1.7b

### Language

- Python

### Research Layer

- Serper API
- Tavily Search

### Framework

- Multi-Agent Reasoning

---

# 📂 Project Structure

```text
startup_reasoning/
│
├── src/
│   └── startup_reasoning/
│       ├── config/
│       │   ├── agents.yaml
│       │   └── tasks.yaml
│       │
│       ├── crew.py
│       ├── main.py
│       │
│       ├── models/
│       │   └── schemas.py
│       │
│       ├── tools/
│       │   ├── startup_research_tool.py
│       │   ├── competitor_tool.py
│       │   └── market_tool.py
│       │
│       └── prompts/
│           └── debate_rules.md
```

---

# ⚙️ Installation

## Clone Repository

```bash
git clone <repo_url>
cd startup_reasoning
```

## Create Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🧠 Local LLM Setup

Install Ollama:

```bash
brew install ollama
```

Pull model:

```bash
ollama pull qwen3:1.7b
```

Start server:

```bash
ollama serve
```

---

# ▶️ Run Project

```bash
PYTHONPATH=src python3 -m startup_reasoning.main
```

---

# 📌 Example Output

```markdown
Startup Viability Score: 68/100

Verdict:
PIVOT

Strengths:
- Strong market demand
- Real user pain point

Weaknesses:
- Weak monetization
- High competition

Major Risks:
- Low retention
- Easy to replicate

Recommended Pivot:
B2B SaaS for colleges

Confidence:
81%
```

---

# 🚀 Future Improvements

- Real-time web research
- Startup trend intelligence
- VC-style benchmarking
- Investor report export
- Startup pitch scoring
- Team risk analysis
- Market forecasting
- Multi-model reasoning

---

# 🏆 Why VentureMind AI Matters

Building a startup is expensive.

Bad startup decisions cost:

```text
time
money
career years
mental energy
```

**VentureMind AI helps founders think before they build.**

Instead of chasing hype, founders get:

✅ skepticism  
✅ structured reasoning  
✅ realistic evaluation  
✅ investor-like thinking

---

## Built For

```text
Hackathons
Founders
Indie Hackers
Startup Teams
Accelerators
Students
VC Simulation
```

---

<p align="center">
<b>VentureMind AI</b><br/>
<i>Because optimism is expensive.</i>
</p>
