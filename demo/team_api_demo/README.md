# Team API Demo

This demo showcases Agno's Team API functionality, demonstrating how multiple AI agents can collaborate on tasks.

## Overview

The Team API allows you to:
- Create teams of specialized agents
- Coordinate collaborative tasks between agents
- Leverage different agent expertise for complex problems

## Files

- `simple_team_demo.py` - Basic Team API demonstration with researcher, analyst, and writer agents

## Running the Demo

### Prerequisites
You'll need AWS Bedrock credentials set as environment variables:
```bash
export AWS_BEDROCK_ACCESS_KEY_ID=your_access_key
export AWS_BEDROCK_SECRET_ACCESS_KEY=your_secret_key
```

### Validate Setup
First, check that everything is configured correctly:
```bash
python demo/team_api_demo/validate_setup.py
```

### Run the Demo
```bash
python demo/team_api_demo/simple_team_demo.py
```

## What the Demo Shows

1. **Team Creation** - How to create a team with multiple specialized agents
2. **Collaborative Tasks** - Agents working together on a shared topic
3. **Role-based Contributions** - Each agent contributing from their area of expertise

## Team Structure

The demo creates a team with three agents:
- **Researcher** - Gathers facts, data, and insights
- **Analyst** - Analyzes information and identifies patterns  
- **Writer** - Creates clear, structured content

## Key Concepts

- **Team Coordination** - The Team class orchestrates agent collaboration
- **Role Specialization** - Each agent has a specific role and instructions
- **Collaborative Output** - Combined expertise produces richer results

## Next Steps

- Experiment with different agent roles and instructions
- Try more complex collaborative tasks
- Add additional agents with specialized skills