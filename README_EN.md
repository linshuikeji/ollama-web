# 🤖 Ollama Web - Local AI Model Tools

<div align="center">

[![GitHub stars](https://img.shields.io/github/stars/YOUR_USERNAME/ollama-web?style=flat&logo=github)](https://github.com/YOUR_USERNAME/ollama-web)
[![Python](https://img.shields.io/badge/Python-3.10+-blue?style=flat&logo=python)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.0+-green?style=flat&logo=flask)](https://flask.palletsprojects.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow?style=flat)](LICENSE)

**Local AI Model Web Interface based on Ollama, supporting chat, OCR text recognition, and PDF text extraction**

[English](./README_EN.md) | [简体中文](./README.md)

</div>

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 💬 **Chat** | Chat with local Ollama models, supports multi-turn conversation |
| 🔍 **OCR** | Upload images, use vision models to recognize text |
| 📄 **PDF** | Upload PDF files, extract text content |
| 🎯 **Quick Modes** | Quick, Think, Expert modes available |
| 💾 **History** | Local chat history, preserved after refresh |
| 🎨 **Modern UI** | Dark theme, clean and beautiful |

---

## 🚀 Quick Start

### One-Click Start (Recommended)

1. Clone the project:
```bash
git clone https://github.com/YOUR_USERNAME/ollama-web.git
cd ollama-web
```

2. Double-click `一键启动.bat`

3. Open browser: http://localhost:5000

---

## 📋 Prerequisites

### 1. Install Ollama

Download from [ollama.com](https://ollama.com/download)

### 2. Start Ollama

```bash
ollama serve
```

### 3. Download Models

```bash
# Chat models
ollama pull llama2
ollama pull qwen

# Vision models (for OCR)
ollama pull llava
ollama pull qwen2vl
```

---

## 📁 Project Structure

```
ollama-web/
├── 一键启动.bat          # One-click start script
├── app.py               # Flask backend
├── templates/
│   └── index.html       # Frontend
├── requirements.txt     # Python dependencies
├── README.md           # Chinese documentation
├── README_EN.md        # English documentation
├── LICENSE            # MIT License
└── .gitignore        # Git ignore file
```

---

## 🛠️ Tech Stack

- **Backend**: Python + Flask
- **Frontend**: HTML + CSS + JavaScript
- **PDF**: PyPDF2
- **Image**: Pillow
- **HTTP**: requests

---

## 🤝 Contributing

Welcome to submit Issues and Pull Requests!

---

## 📄 License

MIT License - See [LICENSE](LICENSE)

---

<div align="center">

**If this project helps you, please ⭐ Star!**

</div>
