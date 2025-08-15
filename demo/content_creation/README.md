# Agno Multi-Agent Content Creation Demo

A comprehensive demonstration of multi-agent systems using the [agno framework v1.7.6](https://pypi.org/project/agno/1.7.6/). This project showcases an AI-powered content creation agency where specialized agents collaborate to produce high-quality content.

## 🤖 Meet the AI Team

This demo features 5 specialized agents working together in a coordinated workflow:

- **🔍 Research Agent** - Gathers comprehensive information and market insights
- **📋 Content Strategist** - Develops content strategy and SEO optimization plans  
- **✍️ Writer Agent** - Creates engaging, well-structured content
- **📖 Editor Agent** - Reviews, fact-checks, and ensures quality standards
- **🎯 Project Manager** - Coordinates workflows and manages deliverables

## 🚀 Features

- **Multi-Agent Collaboration**: Agents work together through coordinated workflows
- **Custom Tools**: Specialized tools for research, content planning, writing quality assessment, and project management
- **Flexible Workflows**: Complete content creation pipeline from research to final delivery
- **Interactive Demo**: Multiple demo modes including quick demo, interactive mode, and collaborative sessions
- **Real-time Coordination**: Agents hand off work and coordinate through the project manager
- **Quality Assurance**: Built-in editorial review and quality checking processes

## 📋 Requirements

- Python 3.8+
- agno framework v1.7.6
- Anthropic API key (for Claude models)
- Optional: OpenAI API key for additional model options

> **Note**: This demo is specifically designed for agno v1.7.6. The API imports, model initialization, and tool definitions have been updated to match this version's structure. Tools now use the `@tool` decorator pattern instead of class inheritance.

## 🛠️ Installation

1. Test the installation (optional but recommended):
```bash
python test_imports.py
# Or run comprehensive tool validation
python validate_tools.py
```

## 🎮 Running the Demo

### Quick Start
```bash
python demo.py
```

This will launch an interactive menu with several demo options:

1. **Quick Demo** - Runs a predefined "AI in Healthcare" content creation workflow
2. **Interactive Demo** - Choose your own topic and parameters  
3. **Collaborative Demo** - See agents working together on specific challenges
4. **Agent Details** - Learn about each agent's capabilities and tools

### Command Line Usage

You can also import and use the workflow programmatically:

```python
from demo.workflows.content_creation_workflow import ContentCreationWorkflow

# Initialize the workflow
workflow = ContentCreationWorkflow()

# Run complete content creation process
results = workflow.run_complete_workflow(
    topic="AI in Healthcare",
    content_type="blog_post", 
    target_audience="healthcare professionals",
    deadline="2024-12-31"
)

# Generate report
report = workflow.generate_workflow_report(results)
print(report)
```

## 🏗️ Architecture

### Agent Roles

#### Research Agent (`demo/agents/research_agent.py`)
- **Tools**: Web Search, Trend Analysis, Fact Checking
- **Responsibilities**: Comprehensive topic research, trend analysis, information verification

#### Content Strategist (`demo/agents/strategist_agent.py`)  
- **Tools**: Content Planner, SEO Optimizer
- **Responsibilities**: Strategy development, content planning, SEO optimization

#### Writer Agent (`demo/agents/writer_agent.py`)
- **Tools**: Writing Quality Assessment
- **Responsibilities**: Content creation, tone adaptation, readability optimization

#### Editor Agent (`demo/agents/editor_agent.py`)
- **Tools**: Writing Quality, SEO Optimizer, Fact Checker  
- **Responsibilities**: Quality review, fact-checking, final editing

#### Project Manager (`demo/agents/project_manager_agent.py`)
- **Tools**: Task Manager, Progress Tracker, Communication
- **Responsibilities**: Workflow coordination, progress tracking, team communication

### Custom Tools

#### Research Tools (`demo/tools/research_tools.py`)
- `web_search_tool` - Simulated web search functionality
- `trend_analysis_tool` - Market trend analysis and insights
- `fact_check_tool` - Information verification and credibility assessment

#### Content Tools (`demo/tools/content_tools.py`)
- `content_planner_tool` - Content structure and outline generation
- `writing_quality_tool` - Readability and quality assessment  
- `seo_optimizer_tool` - SEO analysis and optimization suggestions

#### Project Tools (`demo/tools/project_tools.py`)
- `task_manager_tool` - Task creation, assignment, and tracking
- `progress_tracker_tool` - Project progress monitoring and reporting
- `communication_tool` - Team and client communication management

### Workflow Pipeline

The complete content creation workflow follows these steps:

1. **Project Initialization** - Setup and planning
2. **Research Phase** - Comprehensive topic research  
3. **Strategy Development** - Content strategy and planning
4. **Requirements Definition** - Specific content requirements
5. **Content Writing** - Initial draft creation
6. **Editorial Review** - Quality review and optimization
7. **Final Quality Check** - Final QA and compliance verification  
8. **Project Completion** - Delivery and documentation

## 📊 Example Output

The workflow generates comprehensive deliverables including:

- **Final Content** - Publication-ready content piece
- **Research Report** - Detailed research findings and insights
- **Content Strategy** - Strategic approach and SEO plan
- **Editorial Feedback** - Quality assessment and recommendations
- **Project Documentation** - Complete workflow documentation

## 🔧 Customization

### Adding New Agents

1. Create agent class in `demo/agents/`
2. Define specialized tools and instructions
3. Add to workflow in `demo/workflows/content_creation_workflow.py`

### Creating Custom Tools

1. Use the `@tool` decorator from `agno.tools`
2. Define function with proper type hints
3. Add descriptive docstring with Args and Returns
4. Import and add to relevant agent configurations

Example:
```python
from agno.tools import tool

@tool(
    name="my_custom_tool",
    description="Description of what the tool does"
)
def my_custom_tool(param1: str, param2: int = 10) -> dict:
    """
    Tool function description.
    
    Args:
        param1: Description of first parameter
        param2: Description of second parameter
        
    Returns:
        Dictionary with results
    """
    return {"result": f"Processed {param1} with {param2}"}
```

### Extending Workflows

1. Modify `ContentCreationWorkflow` class
2. Add new workflow steps or parallel processes
3. Update agent coordination and handoffs

## 🤝 Contributing

This is a demonstration project showcasing agno framework capabilities. Feel free to:

- Extend the agent capabilities
- Add new workflow patterns
- Improve the custom tools
- Create additional demo scenarios

## 📄 License

This project is provided as a demonstration of the agno framework capabilities.

## 🔗 Related Links

- [Agno Framework](https://pypi.org/project/agno/)
- [Anthropic Claude](https://www.anthropic.com/claude)
- [Multi-Agent Systems](https://en.wikipedia.org/wiki/Multi-agent_system)
