# 🤖 Ollama 本地模型工具

<div align="center">

[![GitHub stars](https://img.shields.io/github/stars/opendatalab/mineru?style=flat&logo=github)](https://github.com/opendatalab/mineru)
[![Python](https://img.shields.io/badge/Python-3.10+-blue?style=flat&logo=python)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.0+-green?style=flat&logo=flask)](https://flask.palletsprojects.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow?style=flat)](LICENSE)

**基于 Ollama 的本地大模型 Web 界面，支持聊天、OCR 文字识别、PDF 文本提取**

[English](./README_EN.md) | [简体中文](./README.md)

</div>

---

## ✨ 功能特性

| 功能 | 说明 |
|------|------|
| 💬 **智能聊天** | 与本地 Ollama 模型对话，支持多轮对话和历史记录 |
| 🔍 **OCR 识别** | 上传图片，使用视觉模型识别图片中的文字 |
| 📄 **PDF 提取** | 上传 PDF 文件，提取文本内容 |
| 🎯 **快捷模式** | 快捷、思考、专家三种模式可选 |
| 💾 **历史记录** | 本地保存聊天历史，刷新不丢失 |
| 🎨 **现代界面** | 豆包风格深色主题，简洁美观 |

---

## 🚀 快速开始

### 方式一：一键启动（推荐）

1. 克隆项目：
```bash
git clone https://github.com/linshuikeji/ollama-web.git
cd ollama-web
```

2. 双击运行 `一键启动.bat`

3. 打开浏览器访问：http://localhost:5000

### 方式二：手动启动

```bash
# 创建虚拟环境
python -m venv venv

# 激活虚拟环境
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Linux/Mac

# 安装依赖
pip install -r requirements.txt

# 启动服务
python app.py
```

---

## 📋 准备工作

### 1. 安装 Ollama

访问 [ollama.com](https://ollama.com/download) 下载安装

### 2. 启动 Ollama 服务

```bash
ollama serve
```

### 3. 下载模型

```bash
# 聊天模型（必备）
ollama pull llama2      # Meta Llama 2
ollama pull qwen       # 阿里通义千问
ollama pull mistral    # Mistral

# 视觉模型（OCR 识别需要）
ollama pull llava      # 多模态模型
ollama pull qwen2vl   # 千问视觉模型
```

---

## 📖 使用说明

### 💬 聊天功能

1. 在左侧边栏选择聊天模型
2. 输入消息，按 Enter 发送
3. 支持快捷模式切换：
   - ⚡ 快捷：适用于大部分场景
   - 🧠 思考：深入思考，解决复杂问题
   - 🎓 专家：专业详细回答
4. 支持上传图片（多模态模型）
5. 消息复制和保存功能
6. 历史对话记录自动保存

### 🔍 OCR 识别

1. 点击顶部的「🔍 OCR」切换到识别页面
2. 选择视觉模型
3. 上传图片，自动开始识别
4. 左边预览图片，右边查看结果
5. 支持复制和保存结果

### 📄 PDF 提取

1. 点击顶部的「📄 PDF」切换到提取页面
2. 上传 PDF 文件
3. 左边预览 PDF，右边查看提取的文本
4. 支持复制和保存结果

---

## 🎯 高级功能

### 工具栏按钮

| 按钮 | 功能 |
|------|------|
| 📝 新话题 | 创建新的对话 |
| 📎 上传 | 上传图片/PDF/文本文件 |
| 🌐 搜索 | 开启网络搜索模式 |
| 🗑️ 清空 | 清空当前对话 |
| 💨 清上下文 | 保留对话但清除历史 |

### 记住选择

- 聊天模型选择自动保存
- OCR 模型选择自动保存
- PDF 模型选择自动保存
- 快捷模式自动保存

---

## 📁 项目结构

```
ollama-web/
├── 一键启动.bat          # 一键启动脚本（Windows）
├── app.py               # Flask 后端服务
├── templates/
│   └── index.html       # 前端界面
├── requirements.txt     # Python 依赖
└── README.md            # 说明文档
```

---

## 🛠️ 技术栈

- **后端**：Python + Flask
- **前端**：HTML + CSS + JavaScript
- **PDF 解析**：PyPDF2
- **图片处理**：Pillow
- **HTTP 请求**：requests

---

## ⚠️ 常见问题

### Q: 启动报错 "No module named 'flask'"？

**A**: 重新运行 `一键启动.bat`，会自动安装所有依赖

### Q: 无法连接 Ollama？

**A**: 确保已运行 `ollama serve`，服务地址 http://localhost:11434

### Q: OCR 找不到模型？

**A**: 需要安装视觉模型：
```bash
ollama pull llava
```

### Q: 上传文件太大？

**A**: 默认支持 16MB 以内的文件，可在 app.py 中修改 `MAX_CONTENT_LENGTH`

---

## 🤝 贡献指南

欢迎提交 Issue 和 Pull Request！

---

## 📄 License

MIT License - 查看 [LICENSE](LICENSE) 了解详情

---

<div align="center">

**如果这个项目对你有帮助，欢迎 ⭐ Star！**

</div>
