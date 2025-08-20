"""Project Manager Agent for coordinating workflows and managing deliverables."""

from agno.agent import Agent
from agno.models.anthropic import Claude
from demo.content_creation.tools.project_tools import task_manager_tool, progress_tracker_tool, communication_tool
from demo.models.ai_model import sonnet_4, openai_gpt_4

class ProjectManagerAgent:
    """Agent specialized in project coordination and workflow management."""
    
    def __init__(self, model=None):
        self.model = openai_gpt_4
        
        self.agent = Agent(
            name="Project Manager",
            role="Project Coordinator and Workflow Manager",
            model=self.model,
            tools=[
                task_manager_tool,
                progress_tracker_tool,
                communication_tool
            ],
            instructions="""
            You are a Project Manager Agent responsible for coordinating content creation workflows.
            
            Your responsibilities:
            1. Plan and organize content creation projects
            2. Create and assign tasks to appropriate team members
            3. Track progress and manage timelines
            4. Coordinate communication between team members and clients
            5. Ensure deliverables meet quality standards and deadlines
            6. Manage project resources and workflow optimization
            
            Project management approach:
            - Break down complex projects into manageable tasks
            - Assign tasks based on agent capabilities and availability
            - Set realistic timelines with appropriate buffers
            - Monitor progress and identify potential bottlenecks
            - Facilitate clear communication between all stakeholders
            - Ensure quality standards are maintained throughout
            
            Communication standards:
            - Keep all stakeholders informed of progress
            - Escalate issues promptly when they arise
            - Provide regular status updates and milestone reports
            - Maintain professional and clear communication
            - Document decisions and changes for transparency
            
            Always prioritize project success while maintaining team collaboration and client satisfaction.
            """,
            show_tool_calls=True,
            debug_mode=False
        )
    
    def initiate_project(self, project_name: str, client_requirements: str, deadline: str = None) -> str:
        """Initialize a new content creation project."""
        prompt = f"""
        Initialize a new content creation project with the following details:
        
        Project Name: {project_name}
        Client Requirements: {client_requirements}
        Deadline: {deadline or 'To be determined'}
        
        Please:
        1. Create a project plan with key milestones
        2. Break down the project into specific tasks
        3. Assign estimated timeframes for each task
        4. Identify which agents should handle each task
        5. Set up progress tracking for the project
        6. Send initial communication to the team about project kickoff
        
        Use the task manager and progress tracker tools to organize the project structure.
        """
        
        return self.agent.run(prompt)
    
    def assign_tasks(self, project_id: str, task_assignments: dict) -> str:
        """Assign specific tasks to team members."""
        assignments_text = "\n".join([f"- {agent}: {task}" for agent, task in task_assignments.items()])
        
        prompt = f"""
        Assign the following tasks for project {project_id}:
        
        Task Assignments:
        {assignments_text}
        
        For each assignment:
        1. Create the task in the task management system
        2. Assign it to the appropriate agent
        3. Set priority and estimated completion time
        4. Send notification to the assigned agent
        
        Use the task manager and communication tools to handle these assignments.
        """
        
        return self.agent.run(prompt)
    
    def track_progress(self, project_id: str, completed_tasks: list = None, current_milestone: str = None) -> str:
        """Track project progress and generate status report."""
        completed_text = ""
        if completed_tasks:
            completed_text = f"Recently completed tasks: {', '.join(completed_tasks)}"
        
        milestone_text = ""
        if current_milestone:
            milestone_text = f"Current milestone: {current_milestone}"
        
        prompt = f"""
        Generate a progress report for project {project_id}.
        
        {completed_text}
        {milestone_text}
        
        Please:
        1. Update progress tracking with current status
        2. Calculate overall completion percentage
        3. Identify any delays or blockers
        4. Generate status report for stakeholders
        5. Recommend next steps and priorities
        6. Send progress update to relevant team members
        
        Use the progress tracker and communication tools to provide comprehensive updates.
        """
        
        return self.agent.run(prompt)
    
    def coordinate_handoffs(self, from_agent: str, to_agent: str, deliverable: str, instructions: str = "") -> str:
        """Coordinate handoffs between agents."""
        prompt = f"""
        Coordinate a handoff from {from_agent} to {to_agent} for the following deliverable:
        
        Deliverable: {deliverable}
        Special Instructions: {instructions}
        
        Please:
        1. Update task status for the completed work
        2. Create new task for the receiving agent  
        3. Send handoff communication with all necessary details
        4. Ensure both agents understand expectations
        5. Update project progress tracking
        6. Set appropriate deadlines for the next phase
        
        Use task management and communication tools to facilitate smooth handoffs.
        """
        
        return self.agent.run(prompt)
    
    def generate_client_update(self, project_id: str, progress_summary: str, next_steps: str) -> str:
        """Generate client progress update."""
        prompt = f"""
        Generate a professional client update for project {project_id}:
        
        Progress Summary: {progress_summary}
        Next Steps: {next_steps}
        
        The update should include:
        1. Current project status and completed milestones
        2. Summary of work completed since last update
        3. Upcoming deliverables and timelines
        4. Any adjustments to scope or timeline
        5. Next steps and expected delivery dates
        6. Opportunity for client feedback or questions
        
        Use the communication tool to send the update and track it in the project records.
        Make the communication professional, clear, and reassuring.
        """
        
        return self.agent.run(prompt)
    
    def handle_project_completion(self, project_id: str, final_deliverables: list, client_feedback: str = "") -> str:
        """Handle project completion and final delivery."""
        deliverables_text = "\n".join([f"- {deliverable}" for deliverable in final_deliverables])
        
        prompt = f"""
        Handle completion of project {project_id} with the following deliverables:
        
        Final Deliverables:
        {deliverables_text}
        
        Client Feedback: {client_feedback or 'Pending'}
        
        Please:
        1. Mark project as completed in progress tracking
        2. Compile final deliverables package
        3. Send completion notification to client
        4. Gather feedback and lessons learned
        5. Archive project files and documentation
        6. Send thank you and completion summary to team
        
        Use all project management tools to properly close out the project.
        """
        
        return self.agent.run(prompt)