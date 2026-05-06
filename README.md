# 🤖 Simple Reflex Agent

A beginner-friendly implementation of a **Simple Reflex AI Agent** using Python.

---

# 🧠 What is a Simple Reflex Agent?

A Simple Reflex Agent makes decisions based only on the **current input**.

It does **NOT**:

* remember past inputs ❌
* learn from experience ❌
* plan future actions ❌

It simply follows predefined rules.

---

# 🏗️ Architecture

```text
        +------------------+
        |   User Input     |
        +--------+---------+
                 |
                 v
        +------------------+
        |  Input Cleaner   |
        +--------+---------+
                 |
                 v
        +------------------+
        |  Rule Matching   |
        +--------+---------+
                 |
                 v
        +------------------+
        |     Output       |
        +------------------+
```

---

# 🔄 Agent Flow

```text
User → main.py → agent.py → processor.py → rules.py → Response
```

---

# 📂 Project Structure

```text
simple-reflex-agent/
│
├── agent/
│   ├── rules.py
│   ├── processor.py
│   └── agent.py
│
├── main.py
├── README.md
└── .gitignore
```

---

# ⚙️ Features

✅ Rule-based responses
✅ Input cleaning
✅ Keyword matching
✅ Modular architecture
✅ Beginner-friendly project structure

---

# 🚀 How to Run

## 1️⃣ Create Virtual Environment

```bash
python -m venv venv
```

## 2️⃣ Activate Environment

### Windows

```bash
venv\Scripts\activate
```

### Mac/Linux

```bash
source venv/bin/activate
```

## 3️⃣ Run Agent

```bash
python main.py
```

---

# 🧪 Example

```text
You: hi
Agent: Hello!

You: how are you
Agent: I am fine!

You: bye
Agent: Goodbye!
```

---

# ⚠️ Limitations

* No memory
* No learning
* No reasoning
* Only reacts to current input

---

# 🎯 Learning Goal

This project helps understand the foundation of all AI agents:

```text
Input → Decision → Action
```

---

# 🚀 Future Improvements

* Add memory
* Add planning
* Add learning
* Add reasoning

---

# 📚 Concepts Learned

* Rule-based systems
* Input processing
* Decision making
* Modular architecture
* Git & GitHub workflow

---
