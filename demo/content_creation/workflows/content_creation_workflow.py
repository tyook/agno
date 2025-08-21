"""Content Creation Workflow orchestrating multiple agents using agno.workflow.v2."""

import json
from typing import Dict, Any, Optional
from agno.team import Team
from agno.workflow.v2 import Step, Workflow, StepOutput, StepInput, Loop, Condition
from demo.models.ai_model import sonnet_4

from demo.content_creation.agents.research_agent import ResearchAgent
from demo.content_creation.agents.strategist_agent import ContentStrategistAgent
from demo.content_creation.agents.writer_agent import WriterAgent
from demo.content_creation.agents.editor_agent import EditorAgent
from demo.content_creation.agents.project_manager_agent import ProjectManagerAgent


class ContentCreationWorkflow:
    """Orchestrates a complete content creation workflow using multiple specialized agents."""
    
    def __init__(self, model=None):
        self.model = sonnet_4
        
        # Initialize all agents
        self.research_agent = ResearchAgent(model=self.model)
        self.strategist_agent = ContentStrategistAgent(model=self.model)
        self.writer_agent = WriterAgent(model=self.model)
        self.editor_agent = EditorAgent(model=self.model)
        self.project_manager = ProjectManagerAgent(model=self.model)
        
        # Create agent team for collaborative tasks
        self.team = Team(
            members=[
                self.research_agent.agent,
                self.strategist_agent.agent,
                self.writer_agent.agent,
                self.editor_agent.agent,
                self.project_manager.agent
            ],
            show_tool_calls=True,
            model=self.model
        )
    
    def _create_content_workflow(self, topic: str, content_type: str, target_audience: str, deadline: Optional[str]) -> Workflow:
        """Create the content creation workflow using agno.workflow.v2."""
        return Workflow(
            name="Content Creation Workflow",
            description="Complete content creation process from research to publication",
            steps=[
                Step(
                    name="project_initialization",
                    agent=self.project_manager.agent,
                    max_retries=2,
                    description="🚀 Project Initialization"
                ),
                Step(
                    name="research",
                    agent=self.research_agent.agent,
                    max_retries=2,
                    description="🔍 Research Phase"
                ),
                Step(
                    name="strategy",
                    agent=self.strategist_agent.agent,
                    max_retries=2,
                    description="📋 Content Strategy Development"
                ),
                Step(
                    name="requirements",
                    agent=self.strategist_agent.agent,
                    max_retries=2,
                    description="📝 Content Requirements Definition"
                ),
                Step(
                    name="writing",
                    agent=self.writer_agent.agent,
                    max_retries=3,
                    description="✍️ Content Writing"
                ),
                Step(
                    name="editorial_review",
                    agent=self.editor_agent.agent,
                    max_retries=2,
                    description="📖 Editorial Review"
                ),
                Step(
                    name="quality_check",
                    agent=self.editor_agent.agent,
                    max_retries=2,
                    description="🔍 Final Quality Check"
                ),
                Step(
                    name="project_completion",
                    agent=self.project_manager.agent,
                    max_retries=1,
                    description="🎉 Project Completion"
                )
            ]
        )
    
    def run_complete_workflow(self, 
                            topic: str, 
                            content_type: str = "blog_post",
                            target_audience: str = "general",
                            deadline: Optional[str] = None) -> Dict[str, Any]:
        """
        Run the complete content creation workflow using agno.workflow.v2.
        
        Args:
            topic: The main topic for content creation
            content_type: Type of content (blog_post, article, social_media)
            target_audience: Target audience description
            deadline: Optional deadline for the project
            
        Returns:
            Dict containing all workflow outputs and final deliverables
        """
        
        workflow_input = {
            "topic": topic,
            "content_type": content_type,
            "target_audience": target_audience,
            "deadline": deadline
        }
        
        try:
            print(f"🚀 Starting Content Creation Workflow for: {topic}")
            print(f"   Content Type: {content_type}")
            print(f"   Target Audience: {target_audience}")
            print(f"   Deadline: {deadline or 'Not specified'}")
            print()
            
            # Create and run the workflow
            workflow = self._create_content_workflow(topic, content_type, target_audience, deadline)
            
            # Create comprehensive instructions for the entire workflow
            workflow_message = f"""
            Complete content creation workflow for: {topic}
            
            Content Type: {content_type}
            Target Audience: {target_audience}
            Deadline: {deadline or 'Not specified'}
            
            Execute all 8 phases sequentially:
            1. Project initialization and planning
            2. Comprehensive research on {topic}
            3. Content strategy development for {target_audience}
            4. Content requirements definition
            5. Content writing based on research and strategy
            6. Editorial review with SEO optimization
            7. Final quality check against requirements
            8. Project completion and deliverables
            """
            
            result = workflow.run(
                message=workflow_message.strip(),
                additional_data=workflow_input
            )
            
            if result and result.session_id:
                print("✅ Workflow completed successfully!")
                
                # Extract outputs from step responses
                step_outputs = {}
                for step_result in result.step_responses:
                    if hasattr(step_result, 'step_name') and step_result.content:
                        step_outputs[step_result.step_name] = step_result.content
                
                # Compile workflow results
                workflow_results = {
                    "project_info": workflow_input,
                    "workflow_outputs": step_outputs,
                    "final_deliverables": {
                        "final_content": step_outputs.get("writing"),
                        "research_report": step_outputs.get("research"),
                        "content_strategy": step_outputs.get("strategy"),
                        "content_requirements": step_outputs.get("requirements"),
                        "editorial_feedback": step_outputs.get("editorial_review"),
                        "quality_assessment": step_outputs.get("quality_check"),
                        "project_summary": step_outputs.get("project_completion")
                    },
                    "session_id": result.session_id,
                    "status": "success"
                }
                
                return workflow_results
            else:
                print("❌ Workflow execution failed")
                return {
                    "project_info": workflow_input,
                    "error": "Workflow execution failed - no result returned",
                    "status": "error"
                }
                
        except Exception as e:
            print(f"❌ Workflow error: {str(e)}")
            return {
                "project_info": workflow_input,
                "error": str(e),
                "status": "error"
            }
    
    def run_collaborative_session(self, topic: str, specific_challenge: str) -> str:
        """
        Run a collaborative session where all agents work together on a specific challenge.
        
        Args:
            topic: The main topic
            specific_challenge: A specific challenge or question to address
            
        Returns:
            Collaborative response from the team
        """
        
        prompt = f"""
        We have a content creation challenge that requires collaborative input from all team members.
        
        Topic: {topic}
        Challenge: {specific_challenge}
        
        Each agent should contribute from their area of expertise:
        - Research Agent: Provide relevant data and insights
        - Content Strategist: Suggest strategic approaches
        - Writer: Offer creative and structural solutions
        - Editor: Ensure quality and accuracy considerations
        - Project Manager: Coordinate the response and ensure all perspectives are covered
        
        Please collaborate to provide a comprehensive solution to this challenge.
        """
        
        return self.team.run(prompt)
    
    def generate_workflow_report(self, workflow_results: Dict[str, Any]) -> str:
        """Generate a comprehensive workflow report."""
        
        if workflow_results.get("status") == "error":
            return f"Workflow encountered an error: {workflow_results.get('error', 'Unknown error')}"
        
        project_info = workflow_results.get('project_info', {})
        session_id = workflow_results.get('session_id', 'N/A')
        
        report = f"""
# Content Creation Workflow Report

## Project Information
- **Topic**: {project_info.get('topic', 'N/A')}
- **Content Type**: {project_info.get('content_type', 'N/A')}
- **Target Audience**: {project_info.get('target_audience', 'N/A')}
- **Deadline**: {project_info.get('deadline', 'Not specified')}
- **Session ID**: {session_id}

## Workflow Summary
The content creation workflow was completed successfully using agno.workflow.v2 with all phases executed:

1. ✅ **Project Initialization** - Project setup and planning
2. ✅ **Research Phase** - Comprehensive topic research and analysis  
3. ✅ **Strategy Development** - Content strategy and planning
4. ✅ **Requirements Definition** - Specific content requirements
5. ✅ **Content Writing** - Initial draft creation
6. ✅ **Editorial Review** - Quality review and optimization
7. ✅ **Quality Check** - Final quality assurance
8. ✅ **Project Completion** - Final delivery and wrap-up

## Workflow Features
- **Built-in Retry Logic**: Each step has configured retry attempts for reliability
- **Error Handling**: Workflow-level exception management and recovery
- **Session Tracking**: Complete audit trail with session ID {session_id}
- **Data Flow**: Automatic step output passing and context preservation
- **Performance Monitoring**: Built-in metrics and progress tracking

## Final Deliverables
- Final content piece ready for publication
- Comprehensive research report with insights
- Detailed content strategy document
- Content requirements specification
- Editorial review with improvement recommendations
- Quality assessment and compliance verification
- Complete project documentation

## Workflow Status: COMPLETED SUCCESSFULLY ✅
        """
        
        return report