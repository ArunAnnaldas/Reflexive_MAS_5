# 🤖 Reflexive Multi-Agent AI System (LangChain + OpenAI)

This project demonstrates a **self-correcting multi-agent AI system** built using [LangChain](https://www.langchain.com/) and OpenAI GPT-3.5. It simulates real-world AI collaboration between a Planner, Coder, and Critic agent working in a **reflexive loop** to improve generated Python code based on feedback.

---

## 🧩 Agent Roles

| Agent        | Description |
|--------------|-------------|
| 🧠 Planner Agent | Breaks down user intent into coding steps |
| 💻 Coder Agent   | Generates Python code based on the plan |
| 🧐 Critic Agent  | Reviews the code and suggests improvements |
| 🔁 Reflexive Loop | Retries code generation based on critic feedback until approved |

---

## 🎯 Sample Use Case

**Input Prompt:**

Write a function to check if a number is prime



**System Behavior:**
1. Planner defines coding steps
2. Coder generates a Python function
3. Critic reviews the code
4. If not approved, the Coder improves the function based on feedback
5. Loop continues until the Critic says **APPROVED**

---

## 🛠 Tech Stack

- Python 3.9+
- LangChain
- OpenAI GPT-3.5 Turbo
- Reflexive Agent Pattern (AutoGen inspired)
- Token tracking via `get_openai_callback`

---


---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://bitbucket.org/YOUR_TEAM/your-repo-name.git
cd your-repo-name


2. Install Dependencies

pip install langchain openai


3. Set Your OpenAI API Key

export OPENAI_API_KEY="your-key-here"


python main.py
