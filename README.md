# Roz — Mac Assistant (DeepSeek R1)


## Prerequisites
- macOS (Apple Silicon or Intel)
- Python 3.10+
- A DeepSeek API Key — create at https://platform.deepseek.com (free tier available)


## 1. Setup
```bash
# 1) Create a project folder and enter it
mkdir roz && cd roz


# 2) Create a virtual environment
python3 -m venv .venv && source .venv/bin/activate


# 3) Save the files from this guide into the shown filenames
# (requirements.txt, .env, app.py, mac_control.py, static/index.html)


# 4) Install dependencies
pip install -r requirements.txt


# 5) Put your API key into .env (see .env.example)


# 6) Run the server
python app.py