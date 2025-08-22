
## 📋 Requirements

- Python 3.8+
- agno framework v1.7.6
- Anthropic API key (for Claude models)
- Optional: OpenAI API key for additional model options

> **Note**: This demo is specifically designed for agno v1.7.6. The API imports, model initialization, and tool definitions have been updated to match this version's structure. Tools now use the `@tool` decorator pattern instead of class inheritance.

## 🛠️ Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd agno
```

2. Install dependencies:
```bash
pip install -e .
```

3. Set up environment variables:
```bash
cp .env.example .env
# Edit .env and add your API keys
Fill in your API keys in the .env file
Export the env variables in your shell rc files, such as ~/.zshrc or ~/.bashrc
export OPENAI_API_KEY=your_openai_api_key_here
export OPENAI_DEFAULT_HEADER=your_openai_default_header_here

Source your shell rc file to apply changes
```bash
source ~/.zshrc
```

4. Run the demo:
```bash
python demo/text_analyzer/simple_demo.py
```

