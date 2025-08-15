
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
pip install -r requirements.txt
# Or install agno directly with the specific version
pip install agno==1.7.6 python-dotenv
```

3. Set up environment variables:
```bash
cp .env.example .env
# Edit .env and add your API keys
```
