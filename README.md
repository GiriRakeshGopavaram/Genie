# CodeGen Assistant

An AI-powered code generation assistant that takes natural language prompts and returns code snippets in various programming languages. Built with a FastAPI backend and a React frontend. Supports models like Salesforce CodeGen and DeepSeek Coder.

## Features

- Generate code from prompts in Python, JavaScript, Java, Bash, Git, and more
- FastAPI backend with pluggable open-source LLMs (CodeGen, DeepSeek, etc.)
- Easy to switch models or extend with new features

## Tech Stack

- **Frontend**: React (Create React App)
- **Backend**: FastAPI (Python 3.9+)
- **Model**: Hugging Face Transformers (e.g., `deepseek-coder-1.3b`,`Salesforce/codegen-350M-multi`)
- **Deployment Ready**: Works locally or can be deployed to cloud with GPU support
