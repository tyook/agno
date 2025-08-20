"""Content Creation Workflow orchestrating multiple agents."""

import json
from typing import Dict, Any, Optional
from agno.team import Team
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
    
    def run_complete_workflow(self, 
                            topic: str, 
                            content_type: str = "blog_post",
                            target_audience: str = "general",
                            deadline: Optional[str] = None) -> Dict[str, Any]:
        """
        Run the complete content creation workflow.
        
        Args:
            topic: The main topic for content creation
            content_type: Type of content (blog_post, article, social_media)
            target_audience: Target audience description
            deadline: Optional deadline for the project
            
        Returns:
            Dict containing all workflow outputs and final deliverables
        """
        
        workflow_results = {
            "project_info": {
                "topic": topic,
                "content_type": content_type,
                "target_audience": target_audience,
                "deadline": deadline
            },
            "workflow_outputs": {},
            "final_deliverables": {}
        }
        
        try:
            # Step 1: Project Initialization
            print("🚀 Step 1: Project Initialization")
            project_init = self.project_manager.initiate_project(
                project_name=f"Content Creation: {topic}",
                client_requirements=f"Create {content_type} about {topic} for {target_audience}",
                deadline=deadline
            )
            workflow_results["workflow_outputs"]["project_initialization"] = project_init
            print("✅ Project initialized successfully")
            
            # Step 2: Research Phase
            print("\\n🔍 Step 2: Research Phase")
            research_results = self.research_agent.research_topic(topic, depth="comprehensive")
            workflow_results["workflow_outputs"]["research"] = research_results
            print("✅ Research completed")
            
            # Step 3: Content Strategy Development
            print("\\n📋 Step 3: Content Strategy Development")
            content_strategy = self.strategist_agent.create_content_strategy(
                topic=topic,
                research_insights=research_results,
                target_audience=target_audience
            )
            workflow_results["workflow_outputs"]["strategy"] = content_strategy
            print("✅ Content strategy developed")
            
            # Step 4: Content Requirements Definition
            print("\\n📝 Step 4: Content Requirements Definition")
            content_requirements = self.strategist_agent.define_content_requirements(content_strategy)
            workflow_results["workflow_outputs"]["requirements"] = content_requirements
            print("✅ Content requirements defined")
            
            # Step 5: Content Writing
            print("\\n✍️ Step 5: Content Writing")
            initial_draft = self.writer_agent.write_content(
                outline=content_strategy,
                requirements=content_requirements,
                research_data=research_results
            )
            workflow_results["workflow_outputs"]["initial_draft"] = initial_draft
            print("✅ Initial draft completed")
            
            # Step 6: Editorial Review
            print("\\n📖 Step 6: Editorial Review")
            editorial_review = self.editor_agent.comprehensive_review(
                content=initial_draft,
                requirements=content_requirements,
                seo_keywords=[topic.lower(), f"{topic} guide", f"{topic} benefits"]
            )
            workflow_results["workflow_outputs"]["editorial_review"] = editorial_review
            print("✅ Editorial review completed")
            
            # Step 7: Final Quality Check
            print("\\n🔍 Step 7: Final Quality Check")
            final_quality_check = self.editor_agent.final_quality_check(
                content=initial_draft,
                original_requirements=content_requirements
            )
            workflow_results["workflow_outputs"]["quality_check"] = final_quality_check
            print("✅ Quality check completed")
            
            # Step 8: Project Completion
            print("\\n🎉 Step 8: Project Completion")
            project_completion = self.project_manager.handle_project_completion(
                project_id="PROJ-001",
                final_deliverables=[
                    f"Final {content_type} about {topic}",
                    "Research report and insights",
                    "Content strategy document",
                    "Editorial review and recommendations"
                ]
            )
            workflow_results["workflow_outputs"]["project_completion"] = project_completion
            print("✅ Project completed successfully")
            
            # Compile final deliverables
            workflow_results["final_deliverables"] = {
                "final_content": initial_draft,
                "research_report": research_results,
                "content_strategy": content_strategy,
                "editorial_feedback": editorial_review,
                "quality_assessment": final_quality_check,
                "project_summary": project_completion
            }
            
            return workflow_results
            
        except Exception as e:
            print(f"❌ Workflow error: {str(e)}")
            workflow_results["error"] = str(e)
            return workflow_results
    
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
        
        if "error" in workflow_results:
            return f"Workflow encountered an error: {workflow_results['error']}"
        
        report = f"""
# Content Creation Workflow Report

## Project Information
- **Topic**: {workflow_results['project_info']['topic']}
- **Content Type**: {workflow_results['project_info']['content_type']}
- **Target Audience**: {workflow_results['project_info']['target_audience']}
- **Deadline**: {workflow_results['project_info'].get('deadline', 'Not specified')}

## Workflow Summary
The content creation workflow was completed successfully with all phases executed:

1. ✅ **Project Initialization** - Project setup and planning
2. ✅ **Research Phase** - Comprehensive topic research and analysis  
3. ✅ **Strategy Development** - Content strategy and planning
4. ✅ **Requirements Definition** - Specific content requirements
5. ✅ **Content Writing** - Initial draft creation
6. ✅ **Editorial Review** - Quality review and optimization
7. ✅ **Quality Check** - Final quality assurance
8. ✅ **Project Completion** - Final delivery and wrap-up

## Final Deliverables
- Final content piece ready for publication
- Comprehensive research report with insights
- Detailed content strategy document
- Editorial review with improvement recommendations
- Quality assessment and compliance verification
- Complete project documentation

## Workflow Status: COMPLETED SUCCESSFULLY ✅
        """
        
        return report