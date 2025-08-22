# Agno Demo Examples

This directory contains two different demo examples showcasing different aspects of the agno framework.

## 🎯 Simple Structured Output Example

**Location**: `demo/structured_output/`

A simple, focused example that demonstrates:
- Single agent with structured output using Pydantic models
- Type-safe responses with validation
- Text analysis with sentiment, topics, and statistics
- Perfect for learning the basics or building API endpoints

**Run the demo**:
```bash
python demo/structured_output/simple_demo.py
```

**Key Files**:
- `text_analyzer.py` - The main agent that analyzes text and returns structured data
- `simple_demo.py` - Demo script with predefined examples and interactive mode

## 🏢 Content Creation Agency Example

**Location**: `demo/content_creation/`

A complex, multi-agent workflow that demonstrates:
- Multiple specialized agents working together
- Coordinated workflows and team collaboration
- Tool integration and complex task orchestration
- Real-world agency simulation

**Run the demo**:
```bash
python demo/content_creation/content_creation_demo.py
```

**Key Components**:
- **Agents**: Research, Content Strategist, Writer, Editor, Project Manager
- **Tools**: Web search, content planning, writing quality assessment, project management
- **Workflows**: Complete content creation pipeline from research to final output

## 🚀 Getting Started

1. **Set up environment**:
   ```bash
   cp .env.example .env
   # Add your ANTHROPIC_API_KEY to .env
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Test imports**:
   ```bash
   python test_imports.py
   ```


## 📚 Which Example to Use?

### Use **Structured Output** if you:
- Are new to agno
- Need a simple, single-agent solution
- Want structured data output for APIs
- Are building data processing applications
- Want to understand the basics first

### Use **Content Creation** if you:
- Want to see complex multi-agent workflows
- Are interested in agent collaboration
- Need inspiration for enterprise-level applications
- Want to understand tool integration
- Are building sophisticated AI systems

## 🛠️ Development

Both examples follow similar patterns:
- Pydantic models for structured data
- Agent initialization with specific roles
- Clear separation of concerns
- Comprehensive error handling
- Detailed logging and output

The structured output example is ideal for learning the fundamentals, while the content creation example showcases the full power of multi-agent coordination.