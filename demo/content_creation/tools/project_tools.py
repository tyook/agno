"""Project management and coordination tools."""

import json
from datetime import datetime, timedelta
from typing import Dict, List, Any
from agno.tools import tool


# Global state for task management (in a real app, this would be a database)
_task_storage = {}
_task_counter = 1
_project_storage = {}
_message_log = []


@tool(
    name="task_manager",
    description="Create, assign, and track project tasks",
)
def task_manager_tool(action: str, task_id: str = None, task_details: Dict = None) -> Dict[str, Any]:
    """
    Create, assign, and track project tasks.
    
    Args:
        action: Action to perform (create, assign, update, list)
        task_id: Task ID for update actions
        task_details: Task details for create/update actions
        
    Returns:
        Dictionary with task management results
    """
    global _task_storage, _task_counter
    
    if task_details is None:
        task_details = {}
    
    if action == "create":
        new_task_id = f"TASK-{_task_counter:03d}"
        _task_counter += 1
        
        task = {
            "id": new_task_id,
            "title": task_details.get("title", "Untitled Task"),
            "description": task_details.get("description", ""),
            "assignee": task_details.get("assignee", "unassigned"),
            "status": "pending",
            "priority": task_details.get("priority", "medium"),
            "created_at": datetime.now().isoformat(),
            "due_date": task_details.get("due_date"),
            "estimated_hours": task_details.get("estimated_hours", 2)
        }
        
        _task_storage[new_task_id] = task
        return {"status": "created", "task": task}
    
    elif action == "assign":
        if task_id and task_id in _task_storage:
            _task_storage[task_id]["assignee"] = task_details.get("assignee", "unassigned")
            _task_storage[task_id]["status"] = "assigned"
            return {"status": "assigned", "task": _task_storage[task_id]}
        return {"status": "error", "message": "Task not found"}
    
    elif action == "update":
        if task_id and task_id in _task_storage:
            for key, value in task_details.items():
                if key in _task_storage[task_id]:
                    _task_storage[task_id][key] = value
            return {"status": "updated", "task": _task_storage[task_id]}
        return {"status": "error", "message": "Task not found"}
    
    elif action == "list":
        return {"status": "success", "tasks": list(_task_storage.values())}
    
    return {"status": "error", "message": "Unknown action"}


@tool(
    name="progress_tracker",
    description="Track progress on projects and generate status reports",
)
def progress_tracker_tool(project_id: str, milestone: str = None, completion_percentage: float = None) -> Dict[str, Any]:
    """
    Track progress on projects and generate status reports.
    
    Args:
        project_id: Project identifier
        milestone: Milestone or phase name
        completion_percentage: Completion percentage (0-100)
        
    Returns:
        Dictionary with progress tracking results
    """
    global _project_storage
    
    if project_id not in _project_storage:
        _project_storage[project_id] = {
            "id": project_id,
            "created_at": datetime.now().isoformat(),
            "milestones": [],
            "overall_progress": 0,
            "status": "in_progress"
        }
    
    project = _project_storage[project_id]
    
    if milestone:
        milestone_data = {
            "name": milestone,
            "completed_at": datetime.now().isoformat(),
            "completion_percentage": completion_percentage or 0
        }
        project["milestones"].append(milestone_data)
    
    if completion_percentage is not None:
        project["overall_progress"] = completion_percentage
        if completion_percentage >= 100:
            project["status"] = "completed"
        elif completion_percentage >= 75:
            project["status"] = "near_completion"
    
    # Generate status report
    def _estimate_completion(progress: float) -> str:
        if progress >= 100:
            return "Project completed"
        elif progress >= 75:
            return "1-2 days remaining"
        elif progress >= 50:
            return "3-5 days remaining"
        elif progress >= 25:
            return "1-2 weeks remaining"
        else:
            return "2-4 weeks remaining"
    
    def _get_next_steps(progress: float) -> List[str]:
        if progress < 25:
            return ["Complete initial research phase", "Finalize project scope", "Begin content creation"]
        elif progress < 50:
            return ["Continue content development", "Review and refine approach", "Gather stakeholder feedback"]
        elif progress < 75:
            return ["Complete content draft", "Begin editing and review process", "Prepare for final delivery"]
        elif progress < 100:
            return ["Final quality review", "Client presentation preparation", "Delivery and handoff"]
        else:
            return ["Project completed", "Archive project files", "Conduct post-project review"]
    
    status_report = {
        "project_id": project_id,
        "current_progress": project["overall_progress"],
        "status": project["status"],
        "milestones_completed": len(project["milestones"]),
        "latest_milestone": project["milestones"][-1] if project["milestones"] else None,
        "estimated_completion": _estimate_completion(project["overall_progress"]),
        "next_steps": _get_next_steps(project["overall_progress"])
    }
    
    return status_report


@tool(
    name="communication",
    description="Send updates and manage communications",
)
def communication_tool(recipient: str, message_type: str, content: str, priority: str = "medium") -> Dict[str, Any]:
    """
    Send updates and manage communications.
    
    Args:
        recipient: Recipient of the communication (client, team, stakeholder)
        message_type: Type of message (update, request, notification)
        content: Message content
        priority: Message priority (low, medium, high)
        
    Returns:
        Dictionary with communication results
    """
    global _message_log
    
    message = {
        "id": f"MSG-{len(_message_log) + 1:03d}",
        "recipient": recipient,
        "type": message_type,
        "content": content,
        "priority": priority,
        "sent_at": datetime.now().isoformat(),
        "status": "sent"
    }
    
    _message_log.append(message)
    
    # Simulate different responses based on recipient
    if recipient == "client":
        response = "Message sent to client. Expect response within 24-48 hours."
    elif recipient == "team":
        response = "Team notification sent. All members have been updated."
    else:
        response = f"Message sent to {recipient}."
    
    return {
        "message_id": message["id"],
        "status": "delivered",
        "response": response,
        "delivery_time": datetime.now().isoformat()
    }