# 🧠 Eliza300: A CLI-Based Therapy Chatbot (Python)

Eliza300 is a modular command-line chatbot that simulates therapeutic conversation by identifying keywords in user input and responding with context-specific advice. This project was built as part of BU METCS300 and highlights foundational Python skills including file I/O, string processing, modular design, and CLI interactivity.

## 📌 Features

- Reads structured complaint types and keywords from an external file
- Classifies user input into predefined complaint categories
- Suggests customized advice based on matched type
- Uses clean modular Python files for separation of logic and data
- Designed to run entirely in the command line

## 🛠 Technologies

Python · CLI Interaction · File I/O · Modular Programming · String Matching · Lists & Sets

## 🗂 File Overview

| File | Description |
|------|-------------|
| `eliza300_5_main.py` | Main program entry point with user input and response loop |
| `eliza300_5_functions.py` | Core logic to extract complaint types using keyword matching |
| `eliza300_5_runtime_data.py` | Loads and parses keyword-type mappings from file |
| `ElizaData.txt` | Raw data file mapping complaint types to keywords |

## 💬 Sample Interaction

```text
Thank you for using Eliza300, a fun therapy program.
Please state your complaint:
> I feel sad and tired all the time.

[Matched complaint type]: Depression  
[Advice]:
- Get out more.
- Take up a hobby that you love.
