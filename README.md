# 🤖 Simple Reflex Agent

A beginner-friendly implementation of a **Simple Reflex AI Agent** using Python.

---

## 🧠 What is a Simple Reflex Agent?

A Simple Reflex Agent makes decisions based **only on current input**, using predefined rules.

> 🧩 No memory
> 🧩 No learning
> 🧩 No planning

---

## 🏗️ Architecture

```
        +------------------+
        |   User Input     |
        +--------+---------+
                 |
                 v
        +------------------+
        |  Rule Matching   |
        | (IF conditions)  |
        +--------+---------+
                 |
                 v
        +------------------+
        |     Output       |
        +------------------+
```

---

## 🔄 Agent Flow

```
Input → Process (Rules) → Output
```

---

## ⚙️ Features

* Input normalization (lowercase, trim)
* Keyword-based matching
* Rule-based decision system
* Beginner-friendly structure

---

## 📂 Project Structure

```
simple-reflex-agent/
│
├── simple_reflex_agent.py
├── README.md
└── .gitignore
```

---

## 🚀 How to Run

```bash
python simple_reflex_agent.py
```

---

## 🧪 Example

```
Input: hi
Output: Hello!

Input: how are you
Output: I am fine!
```

---

## ⚠️ Limitations

* Cannot remember past inputs
* Cannot learn new behavior
* Works only on predefined rules

---

## 🎯 Learning Goal

This project helps understand the **foundation of all AI agents**:

> Input → Decision → Action

---

## 🛠️ Future Improvements

* Add memory (Model-Based Agent)
* Add planning (Goal-Based Agent)
* Add learning (Learning Agent)

---
