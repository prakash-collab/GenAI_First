# Production GenAI Application

A production-oriented Generative AI application built while learning and implementing modern LLM application patterns using **Python, LangChain, NVIDIA NIM, and OpenAI-compatible APIs**.

The goal of this project is not to build a simple LLM POC, but to progressively develop the engineering practices required to build reliable, observable, secure, and scalable GenAI applications.

---

## 🚀 Project Goals

This project is part of a structured GenAI engineering learning sprint covering:

* Generative AI fundamentals
* LLM and Chat Model architecture
* Prompt engineering
* Structured outputs
* LangChain
* RAG (Retrieval-Augmented Generation)
* Advanced retrieval techniques
* LangGraph
* Agentic workflows
* LLM evaluation
* RAG evaluation
* Guardrails and security
* Observability and monitoring
* Cost and latency optimization
* Production system design
* Cloud deployment

The application will evolve throughout the learning process rather than being replaced by separate POCs.

---

## 🏗️ Current Implementation

The current version focuses on establishing a clean LLM application foundation.

### Implemented

* LangChain integration
* NVIDIA NIM integration
* OpenAI-compatible API integration
* Chat model invocation
* Temperature configuration
* Maximum output token configuration
* Environment-based configuration
* Token usage inspection
* Response metadata inspection
* Basic production-oriented configuration management

### Current Model

The project currently uses:

```text
nvidia/nemotron-3-super-120b-a12b
```

through the NVIDIA NIM API.

The model can be changed through environment configuration without modifying the application code.

---

## 🔄 Planned Architecture

The application will gradually evolve toward an enterprise-style GenAI architecture:

```text
                         ┌──────────────────┐
                         │      User        │
                         └────────┬─────────┘
                                  │
                                  ▼
                         ┌──────────────────┐
                         │      API        │
                         └────────┬─────────┘
                                  │
                                  ▼
                         ┌──────────────────┐
                         │ Authentication   │
                         │ & Authorization  │
                         └────────┬─────────┘
                                  │
                                  ▼
                         ┌──────────────────┐
                         │   LangGraph /    │
                         │   Orchestrator   │
                         └────────┬─────────┘
                                  │
                    ┌─────────────┴─────────────┐
                    │                           │
                    ▼                           ▼
             ┌──────────────┐           ┌──────────────┐
             │     RAG      │           │    Tools     │
             │   Pipeline   │           │   / APIs     │
             └──────┬───────┘           └──────┬───────┘
                    │                          │
                    ▼                          │
             ┌──────────────┐                  │
             │   Retrieval  │                  │
             │  + Reranking │                  │
             └──────┬───────┘                  │
                    │                          │
                    └────────────┬─────────────┘
                                 │
                                 ▼
                         ┌──────────────────┐
                         │       LLM        │
                         └────────┬─────────┘
                                  │
                                  ▼
                         ┌──────────────────┐
                         │    Guardrails    │
                         │  + Validation    │
                         └────────┬─────────┘
                                  │
                                  ▼
                         ┌──────────────────┐
                         │     Response     │
                         └──────────────────┘
```

---

## 🛠️ Tech Stack

### Core

* Python
* LangChain
* LangGraph
* NVIDIA NIM
* OpenAI-compatible APIs

### Planned

* RAG
* Vector databases
* Hybrid search
* Rerankers
* Ragas
* Docker
* FastAPI
* AWS
* CI/CD
* Observability and tracing

---

## 📁 Project Structure

The project will follow a modular structure as it grows:

```text
.
├── .env.example
├── .gitignore
├── README.md
├── requirements.txt
│
├── app/
│   ├── __init__.py
│   ├── config.py
│   ├── models/
│   ├── prompts/
│   ├── chains/
│   ├── rag/
│   ├── agents/
│   ├── evaluation/
│   └── api/
│
├── tests/
│
└── scripts/
```

The structure will evolve as new production capabilities are introduced.

---

## ⚙️ Setup

### 1. Clone the repository

```bash
git clone <repository-url>
cd <repository-name>
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on macOS/Linux:

```bash
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file:

```env
NVIDIA_API_KEY=your_api_key_here

LLM_MODEL=nvidia/nemotron-3-super-120b-a12b
LLM_TEMPERATURE=0
LLM_MAX_TOKENS=300
```

**Never commit `.env` or API keys to Git.**

Use `.env.example` as the template for required configuration.

---

## ▶️ Running the Application

Example LLM invocation:

```python
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

chat_model = ChatOpenAI(
    model=os.getenv("LLM_MODEL"),
    temperature=float(os.getenv("LLM_TEMPERATURE", 0)),
    max_tokens=int(os.getenv("LLM_MAX_TOKENS", 300)),
    api_key=os.getenv("NVIDIA_API_KEY"),
    base_url="https://integrate.api.nvidia.com/v1"
)

response = chat_model.invoke(
    "Explain Retrieval-Augmented Generation in simple terms."
)

print(response.content)
```

---

## 🔐 Security

Secrets are intentionally separated from application configuration.

### Never commit:

```text
.env
API keys
Access tokens
Passwords
Private credentials
```

The `.env` file is excluded through `.gitignore`.

A safe `.env.example` file should contain only configuration placeholders:

```env
NVIDIA_API_KEY=
LLM_MODEL=nvidia/nemotron-3-super-120b-a12b
LLM_TEMPERATURE=0
LLM_MAX_TOKENS=300
```

For production deployments, secrets should be managed through a dedicated secret-management solution rather than committed to source control.

---

## 📊 LLM Observability

The application inspects model response metadata and token usage.

Example information:

```text
Input tokens
Output tokens
Total tokens
Model name
Finish reason
Response ID
```

This information becomes important in production for:

* Cost monitoring
* Latency analysis
* Debugging
* Token optimization
* Detecting unexpectedly large prompts
* Monitoring RAG context size

---

## 🧠 Key Engineering Concepts

This project emphasizes understanding the difference between:

### Temperature

Controls the randomness of token sampling.

For factual enterprise applications:

```text
temperature ≈ 0
```

is often a sensible starting point.

### Tokens

Tokens represent the units processed by the model.

Token usage affects:

```text
Context size
Latency
Cost
Model limits
```

### `max_tokens`

Controls the maximum amount of output the model can generate.

If the model reaches the configured limit before completing its response, the response may terminate with:

```text
finish_reason = "length"
```

---

## 📈 Production Roadmap

### Phase 1 — LLM Foundations

* [x] Connect LangChain to NVIDIA NIM
* [x] Configure Chat Model
* [x] Environment-based configuration
* [x] Understand temperature
* [x] Understand tokens
* [x] Inspect response metadata
* [x] Inspect token usage

### Phase 2 — Prompt Engineering

* [ ] System messages
* [ ] Human messages
* [ ] AI messages
* [ ] Prompt templates
* [ ] Few-shot prompting
* [ ] Structured output
* [ ] Output validation

### Phase 3 — RAG

* [ ] Document ingestion
* [ ] Document loaders
* [ ] Chunking
* [ ] Embeddings
* [ ] Vector database
* [ ] Retrieval
* [ ] Hybrid search
* [ ] Reranking
* [ ] Context filtering
* [ ] Citation/grounding

### Phase 4 — LangGraph

* [ ] State
* [ ] Nodes
* [ ] Edges
* [ ] Conditional routing
* [ ] Tool calling
* [ ] Agentic workflows
* [ ] Agentic RAG

### Phase 5 — Evaluation

* [ ] RAG evaluation
* [ ] Context relevance
* [ ] Answer relevance
* [ ] Faithfulness / groundedness
* [ ] Automated evaluation
* [ ] Human evaluation
* [ ] Regression evaluation

### Phase 6 — Production Engineering

* [ ] FastAPI
* [ ] Authentication
* [ ] Authorization
* [ ] RBAC
* [ ] Prompt injection protection
* [ ] PII protection
* [ ] Rate limiting
* [ ] Retries
* [ ] Timeouts
* [ ] Circuit breakers
* [ ] Caching
* [ ] Logging
* [ ] Tracing
* [ ] Metrics
* [ ] Cost monitoring

### Phase 7 — Deployment

* [ ] Docker
* [ ] CI/CD
* [ ] AWS deployment
* [ ] Horizontal scaling
* [ ] Production monitoring
* [ ] Load testing
* [ ] Failure testing

---

## 🎯 Learning Philosophy

This repository follows a **production-first** approach.

Instead of creating multiple disconnected tutorials and POCs, the application will continuously evolve:

```text
LLM
 ↓
Prompting
 ↓
RAG
 ↓
LangGraph
 ↓
Evaluation
 ↓
Security
 ↓
Observability
 ↓
Production System
```

Every new concept should answer two questions:

1. **How does it work?**
2. **How would I build and operate it in production?**

---

## 📚 Learning Resources

* LangChain documentation
* LangGraph documentation
* NVIDIA NIM documentation
* Ragas documentation
* OWASP LLM Top 10
* DeepLearning.AI GenAI/RAG courses

---

## ⚠️ Disclaimer

This repository is primarily a learning and engineering practice project.

It is designed to demonstrate production-oriented GenAI concepts and should not be considered production-ready without appropriate security reviews, testing, monitoring, infrastructure hardening, and organizational controls.
