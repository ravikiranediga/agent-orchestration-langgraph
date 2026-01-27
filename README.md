# 🎭 LangGraph Joke Bot

**Agentic Workflow Demonstration Without LLMs**

---

## 📌 Project Overview

The **LangGraph Joke Bot** is a **state-driven, agentic workflow application** built using **LangGraph** and **Python**.
It demonstrates how autonomous agents can manage **state, routing, and control flow** without relying on Large Language Models (LLMs).

The project focuses on:

* Declarative state management
* Deterministic decision routing
* Clean separation of logic and interface

This makes it an excellent example of **modern AI orchestration architecture** suitable for production systems.

---

## 🎯 Key Objectives

* Demonstrate **agentic workflow design** using LangGraph
* Showcase **state evolution** using reducers
* Implement **conditional routing** between agent nodes
* Maintain a clean and extensible project structure
* Build an interactive system without LLM dependency

---

## 🧠 System Architecture

The system is composed of the following layers:

### 1️⃣ State Layer

* Defined using **Pydantic models**
* Maintains:

  * Joke history
  * Selected category
  * Selected language
  * User action choice

### 2️⃣ Agent Nodes

Each node represents a **single responsibility**:

* Menu display
* Joke fetching
* Category update
* Language update
* History reset
* Graceful exit

### 3️⃣ Router

* A conditional router determines the next node
* Ensures deterministic and controlled execution

### 4️⃣ Graph Engine

* Built using **LangGraph’s StateGraph**
* Manages transitions, state updates, and execution flow

---

## ⚙️ Technologies Used

| Technology           | Purpose                          |
| -------------------- | -------------------------------- |
| Python 3.10+         | Core programming language        |
| LangGraph            | Agent orchestration & state flow |
| Pydantic             | State validation & modeling      |
| pyjokes              | Joke data source                 |  

---

## 🧩 Core Features

✔ Stateful joke tracking
✔ Multi-category support
✔ Multi-language support
✔ Resettable session history
✔ Clean exit handling
✔ Reducer-based state updates

---

## 🧠 Key Concepts Demonstrated

* **Agentic Design Patterns**
* **State Reducers (`add`)**
* **Conditional Routing**
* **Immutable State Updates**
* **Separation of Concerns**
* **Workflow Compilation**

---

## ▶️ How to Run the Project

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/ravikiranediga/langgraph-joke-bot.git
cd langgraph-joke-bot
```

### 2️⃣ Install Dependencies

```bash
pip install langgraph pyjokes pydantic 
```

### 3️⃣ Run the Application

```bash
python langgraph_joke_bot.py
```

---

## 🖥️ Sample Interaction

```
🎭 Category : NEUTRAL
🌐 Language : en
😂 Jokes Told : 1

[n] Next Joke  [c] Change Category  [l] Change Language  [r] Reset History  [q] Quit
```

## 👤 Contact

**Ravikiran**
📧 *www.ravikirangowd91@gmail.com*

---
## 📜 License

This project is licensed under the **MIT License**.
