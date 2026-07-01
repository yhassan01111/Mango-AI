# 🥭 Mango AI (V1) — Lightweight Terminal AI Assistant

A fast, interactive, and terminal-based AI assistant built to handle fluid conversations without the bulk of a heavy web interface. Mango AI leverages advanced LLM orchestration and high-speed inference to bring a smart, context-aware AI companion straight into your command line.

Instead of running stateless API calls that forget context after every prompt, Mango AI features persistent local memory tracking and input validation architecture to ensure execution never crashes over typos or unexpected inputs.

---

## 🚀 Key Features & Engineering Mechanics

*   **High-Speed Inference Architecture:** Structured using the **Groq AI** SDK to utilize ultra-fast hardware acceleration, keeping response latencies down to milliseconds.
*   **Conversational State Tracking:** Orchestrated through **LangChain** memory modules, allowing Mango AI to retain contextual history and track reference threads naturally across multi-turn dialogues.
*   **Production-Grade Dependency Management:** Built and managed utilizing modern Python tooling (`uv` / `pyproject.toml`) to ensure clean environment separation, deterministic lockfiles, and zero library friction.
*   **Robust Input Exception Safety:** Engineered with explicit structural exception-handling blocks to intercept unexpected network issues or invalid terminal inputs gracefully without breaking the persistent runtime loop.

---

## 🛠️ Tech Stack & Architecture

*   **Language:** Python 3.12+
*   **Orchestration:** LangChain Core
*   **Inference Engine:** Groq API
*   **Environment & Package Management:** `uv` by Astral

---

## 📦 Local Setup & Installation

Ensure you have your environment manager configured, then follow these steps:

### 1. Clone the repository
```bash
git clone https://github.com/yhassan01111/Mango-AI.git
cd Mango-AI/V1
```

### 2. Add langchain-groq
Copy this command ```bash
uv add langchain-groq 
```
in your cloned repository, using windows powershell.

### 3. Add your api key
Head to https://console.groq.com/keys 
Get an API-key then paste it in the place it was assigned for in the ```.env``` file.

### 4. Running the program
run 
```bash
uv run main.py
``` 
then the app should run perfectly!

## 📢 Project Status & Updates

> 🧪 **Current Build: Alpha V1**
> This project is currently in its active **Alpha V1** release phase. The core architecture, local conversation tracking, and exception handlers are fully operational, but optimization tweaks are ongoing. 

> 🎥 **Tutorial Video Coming Soon!**
> A comprehensive, step-by-step video guide walking through local setup, environment installation using `uv`, and API configuration will be uploaded directly to this repository shortly. Stay tuned!

> 🐛 **Found a Bug?**
> If you encounter any installation errors or runtime crashes, please report them directly via our [Mango AI Support & Bug Report Form)[https://forms.gle/DrKsJn4uBDbs8Grp6] 
